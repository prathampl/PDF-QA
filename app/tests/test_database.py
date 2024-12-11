from app.models.database import init_db, SessionLocal, DocumentMetadata

def test_database_initialization():
    """
    Tests that the database initializes correctly.
    """
    init_db()
    assert os.path.exists("pdf_qa.db")

def test_document_metadata_storage():
    """
    Tests storing and retrieving document metadata in the database.
    """
    session = SessionLocal()
    document = DocumentMetadata(
        id="test123",
        filename="test.pdf",
        upload_date="2024-11-24",
        text_content="This is a test content."
    )
    session.add(document)
    session.commit()

    # Retrieve the stored document
    retrieved_document = session.query(DocumentMetadata).filter_by(id="test123").first()
    assert retrieved_document.filename == "test.pdf"
    assert retrieved_document.text_content == "This is a test content."
    session.close()
