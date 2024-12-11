# PDFReader with Real-Time Q&A

PDFReader is a FastAPI-based application that allows users to upload PDF files, extract their content, and interactively query the content in real time via WebSockets. Built with modern tools like LangChain, OpenAI API, and FAISS, it ensures efficient and accurate information retrieval.

## Features

- **PDF Upload**: Upload PDF files and extract their content for analysis.
- **Real-Time Q&A**: Ask questions about the PDF content using WebSockets for real-time responses.
- **Session Management**: Each user interaction is tracked with session-based context for personalized responses.
- **Rate Limiting**: Protects the application from overuse with rate limiting.
- **NLP Integration**: Uses LangChain and OpenAI API for natural language processing and question answering.
- **Efficient Retrieval**: FAISS integration ensures fast and accurate information retrieval from document embeddings.

## Technologies Used

- **Backend**: FastAPI
- **WebSocket Communication**: FastAPI WebSockets
- **NLP**: LangChain, OpenAI API
- **Document Embedding**: FAISS
- **PDF Processing**: PyPDF2
- **Session Management**: Custom service for handling sessions
- **Rate Limiting**: Custom rate-limiting logic
- **Storage**: Local file storage for uploaded PDFs

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/prathampl/pdfreader-qa.git
   cd pdfreader-qa
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables for OpenAI API key and other configurations.

5. Start the application:
   ```bash
   uvicorn app.main:app --reload
   ```

6. Access the application at `http://127.0.0.1:8000`.

## Endpoints

- `POST /upload` - Upload a PDF file.
- `GET /ws` - WebSocket endpoint for real-time Q&A.

## Usage

1. Use the `/upload` endpoint to upload a PDF file.
2. Establish a WebSocket connection at `/ws`.
3. Ask questions about the uploaded document, and get instant responses.

## Future Enhancements

- Add support for more file formats.
- Integrate advanced analytics for document insights.
- Deploy on cloud platforms for scalability.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any changes or improvements.

---

Start exploring your PDFs like never before!
