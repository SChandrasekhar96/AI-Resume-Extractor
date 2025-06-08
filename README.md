# Resume Skill Extractor

A web application that extracts skills and relevant information from PDF resumes using AI. The application uses advanced NLP techniques to parse and analyze resumes, extracting key information such as skills, education, and experience.

## Features

- Upload PDF resumes
- Extracts skills and relevant information using NLP
- Web-based interface using Streamlit
- Docker support for easy deployment
- GitHub repository available for cloning and deployment
- Open-source project with MIT License

## Requirements

- Python 3.8
- Docker (for containerized deployment)

## Installation

### Using Docker (Recommended)

1. Build the Docker image:
```bash
docker build -t resume-skill-extractor .
```

2. Run the container:
```bash
docker run -p 8501:8501 resume-skill-extractor
```

3. Open your browser and navigate to `http://localhost:8501`

### Local Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Upload a PDF resume file
2. The application will automatically extract skills and relevant information
3. View the extracted information in the web interface

## Project Structure

- `app.py`: Main Streamlit application
- `extract3.py`: Skill extraction logic
- `requirements.txt`: Project dependencies
- `Dockerfile`: Container configuration

## Technologies Used

- Streamlit: For web interface
- PDFPlumber: For PDF processing
- Transformers: For NLP tasks
- PyTorch: Deep learning framework
- GitHub: For source code hosting and version control

## GitHub Deployment

1. Clone the repository:
```bash
git clone https://github.com/SChandrasekhar96/AI-Resume-Extractor.git
```

2. Navigate to the project directory:
```bash
cd AI-Resume-Extractor
```

3. Follow the installation instructions in the [Installation](#installation) section to set up the application locally.

4. To contribute or deploy:
   - Fork the repository
   - Create a new branch for your changes
   - Push your changes to your fork
   - Create a Pull Request to the main repository

## Project Structure

- `app.py`: Main Streamlit application
- `extract3.py`: Skill extraction logic
- `requirements.txt`: Project dependencies
- `Dockerfile`: Container configuration
- `.gitignore`: Git ignore rules
- `netlify.toml`: Configuration for deployment (experimental)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support or questions, please open an issue in the GitHub repository.

## Acknowledgments

- Built with Streamlit and Python
- Uses Hugging Face Transformers for NLP tasks
- Inspired by the need for better resume processing tools

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
