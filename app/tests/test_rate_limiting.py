def test_websocket_rate_limiting(test_client):
    """
    Tests WebSocket rate limiting by sending messages in quick succession.
    """
    with test_client.websocket_connect("/api/qa/ws") as websocket:
        for _ in range(12):  # Exceed rate limit
            websocket.send_text("Test question?")
            response = websocket.receive_text()
        assert "Rate limit exceeded" in response
