import uuid

# Mock in-memory storage for sessions
sessions = {}

def create_session() -> str:
    """
    Creates a new session with a unique ID.
    """
    session_id = str(uuid.uuid4())
    sessions[session_id] = {"document_text": ""}
    return session_id

def get_session_data(session_id: str) -> str:
    """
    Retrieves document text associated with a session.

    :param session_id: Unique session identifier.
    :return: Document text.
    """
    return sessions.get(session_id, {}).get("document_text", "")

def set_session_data(session_id: str, document_text: str):
    """
    Sets document text for a session.

    :param session_id: Unique session identifier.
    :param document_text: Text extracted from the PDF.
    """
    if session_id in sessions:
        sessions[session_id]["document_text"] = document_text

def end_session(session_id: str):
    """
    Ends a session and removes its data.

    :param session_id: Unique session identifier.
    """
    if session_id in sessions:
        del sessions[session_id]
