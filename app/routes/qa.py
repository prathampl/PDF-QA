from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from app.services import nlp, rate_limiter, session_manager

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint with rate limiting for real-time question answering.
    """
    await websocket.accept()
    session_id = session_manager.create_session()  # Create session for the client
    try:
        while True:
            # Enforce rate limiting
            await rate_limiter.limit_websocket(session_id)
            
            # Receive question from client
            question = await websocket.receive_text()
            
            # Process and generate response
            response = nlp.answer_question(session_id, question)
            await websocket.send_text(response)  # Send response back to the client
    except WebSocketDisconnect:
        print("WebSocket disconnected.")
        session_manager.end_session(session_id)
    except Exception as e:
        # Send error message to the client
        await websocket.send_text(f"Error: {str(e)}")
