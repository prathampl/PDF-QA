import os
from fastapi import status

def test_upload_pdf_success(test_client):
    """
    Tests successful upload of a valid PDF file.
    """
    file_path = "sample.pdf"  # Provide a sample PDF file for testing
    with open(file_path, "rb") as pdf_file:
        response = test_client.post(
            "/api/upload/",
            files={"file": ("sample.pdf", pdf_file, "application/pdf")}
        )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "File uploaded successfully"

def test_upload_invalid_file(test_client):
    """
    Tests uploading a non-PDF file and expects an error.
    """
    file_path = "sample.txt"  # Non-PDF file
    with open(file_path, "rb") as non_pdf_file:
        response = test_client.post(
            "/api/upload/",
            files={"file": ("sample.txt", non_pdf_file, "text/plain")}
        )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "Only PDF files are allowed."
