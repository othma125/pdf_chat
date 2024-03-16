# PDF Chat Web Application

## Overview
Welcome to the PDF Chat Web Application repository. This innovative application is designed to enhance user interaction with digital documents. It leverages the power of OpenAI's API to enable users to chat with the application, much like conversing with a virtual assistant. The core functionality includes reading and scanning PDF documents, extracting relevant information, and engaging in an interactive chat powered by OpenAI's advanced language models.

## Features
- **PDF Reading**: Upload and read PDF documents.
- **PDF Scanning**: Scan and extract text from PDFs using OCR technology.
- **OpenAI Chat Integration**: Interactive chat feature utilizing OpenAI's API to simulate conversational experiences based on the content of the PDF.

## Installation

### Prerequisites
- Python 3.x
- Node.js (for the frontend)
- Access to OpenAI API (API key required)

### Backend Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/othma125/pdf_chat.git
   cd pdf-chat-app
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```sh
   cd chatpdfweb
   ```

2. Install necessary Node.js packages:
   ```sh
   npm install
   ```

3. Build the frontend application:
   ```sh
   npm run build
   ```

## Usage
1. Start the backend server:
   ```sh
   ./run_backend.sh
   ```

2. Launch the frontend (if it's a separate service):
   ```sh
   npm start
   ```

3. Open your web browser and navigate to `http://localhost:3000` (or the appropriate URL).

4. Upload a PDF and use the chat feature to interact with the content extracted from your document.

## Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
