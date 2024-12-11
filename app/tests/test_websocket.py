def test_websocket_connection(test_client):
    """
    Tests establishing and closing a WebSocket connection.
    """
    with test_client.websocket_connect("/api/qa/ws") as websocket:
        assert websocket is not None
        websocket.close()

def test_websocket_question_answering(test_client):
    """
    Tests sending a question via WebSocket and receiving a response.
    """
    with test_client.websocket_connect("/api/qa/ws") as websocket:
        websocket.send_text("What is the content of the PDF?")
        response = websocket.receive_text()
        assert response is not None
        assert "No document loaded" in response  # Expected without loaded document
