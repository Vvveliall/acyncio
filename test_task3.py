import asyncio
import http.client
from unittest.mock import patch
import pytest

from task3 import send_request, throttled_requests, MAX_CONCURRENT_REQUESTS

@pytest.mark.asyncio
async def test_send_request():
    with patch('http.client.HTTPConnection.getresponse') as mock_response:
        mock_response.return_value.status = 200
        await send_request()
        mock_response.assert_called_once()

@pytest.mark.asyncio
async def test_throttled_requests():
    with patch('your_script.send_request') as mock_send_request:
        tasks = [throttled_requests() for _ in range(MAX_CONCURRENT_REQUESTS + 1)]
        await asyncio.gather(*tasks)
        assert mock_send_request.call_count == MAX_CONCURRENT_REQUESTS