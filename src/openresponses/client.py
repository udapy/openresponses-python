import json
from typing import AsyncGenerator, Generator, List, Optional, Union
import httpx
from .models import OpenResponsesRequest, OpenResponsesOutput, StreamEvent, MessageItem

class OpenResponsesClient:
    """
    Async/Sync Client for Open Responses API.
    """
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.headers = {"Content-Type": "application/json"}
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"

    def create(
        self,
        model: str,
        input: Union[str, List[MessageItem]],
        stream: bool = False,
        max_tool_calls: Optional[int] = None
    ) -> Union[OpenResponsesOutput, Generator[StreamEvent, None, None]]:
        """
        Synchronous request to create a response.
        """
        request = OpenResponsesRequest(
            model=model,
            input=input,
            stream=stream,
            max_tool_calls=max_tool_calls
        )
        
        url = f"{self.base_url}/v1/responses"
        
        if stream:
            return self._stream_request(url, request)
        else:
            with httpx.Client() as client:
                resp = client.post(url, json=request.model_dump(), headers=self.headers, timeout=60.0)
                resp.raise_for_status()
                return OpenResponsesOutput(**resp.json())

    def _stream_request(self, url: str, request: OpenResponsesRequest) -> Generator[StreamEvent, None, None]:
        with httpx.Client() as client:
            with client.stream("POST", url, json=request.model_dump(), headers=self.headers, timeout=60.0) as resp:
                resp.raise_for_status()
                for line in resp.iter_lines():
                    if line.startswith("event:"):
                        event_type = line.split(": ", 1)[1]
                    elif line.startswith("data:"):
                        data_str = line.split(": ", 1)[1]
                        data = json.loads(data_str)
                        yield StreamEvent(event=event_type, data=data)

class AsyncOpenResponsesClient:
    """
    Async Client for Open Responses API.
    """
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.headers = {"Content-Type": "application/json"}
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"
            
    async def create(
        self,
        model: str,
        input: Union[str, List[MessageItem]],
        stream: bool = False,
        max_tool_calls: Optional[int] = None
    ) -> Union[OpenResponsesOutput, AsyncGenerator[StreamEvent, None]]:
        request = OpenResponsesRequest(
            model=model,
            input=input,
            stream=stream,
            max_tool_calls=max_tool_calls
        )
        
        url = f"{self.base_url}/v1/responses"

        if stream:
            return self._stream_request(url, request)
        else:
            async with httpx.AsyncClient() as client:
                resp = await client.post(url, json=request.model_dump(), headers=self.headers, timeout=60.0)
                resp.raise_for_status()
                return OpenResponsesOutput(**resp.json())

    async def _stream_request(self, url: str, request: OpenResponsesRequest) -> AsyncGenerator[StreamEvent, None]:
        async with httpx.AsyncClient() as client:
            async with client.stream("POST", url, json=request.model_dump(), headers=self.headers, timeout=60.0) as resp:
                resp.raise_for_status()
                async for line in resp.aiter_lines():
                    if line.startswith("event:"):
                        event_type = line.split(": ", 1)[1]
                    elif line.startswith("data:"):
                        data_str = line.split(": ", 1)[1]
                        # Handle potential keeping of newlines or empty data
                        try:
                            data = json.loads(data_str)
                            yield StreamEvent(event=event_type, data=data)
                        except json.JSONDecodeError:
                            continue
