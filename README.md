PDF Search

PDF Search is a simple tool that allows users to upload a PDF file and search for specific information within the document using natural language. The tool uses the LangChain library and OpenAI models to perform similarity search and question answering on the uploaded PDF file.

Before using PDF Search, ensure that the following dependencies are installed:

    Streamlit
    PyPDF2
    LangChain
    Dotenv

These dependencies can be installed using pip:

pip install streamlit PyPDF2 LangChain python-dotenv

You will also need to obtain an OpenAI API key to use the tool. To obtain a key, visit the OpenAI website, sign up for an account, and generate an API key.

Next, create a new file in the same directory as the main.py file, called .env, and write your OpenAI API key using the following format:

OPENAI_API_KEY= < YOUR KEY HERE >

Usage


To run the tool, navigate to the project directory and execute the following command:

streamlit run app.py

The tool will launch in the browser, and users can begin using it immediately.

    Upload a PDF file: Users can upload a PDF file by clicking on the "Upload a PDF file" button and selecting the file from their local file system.

    Ask a question: Once the PDF file has been uploaded, users can enter a natural language question related to the content of the PDF file. For example, a user may ask "What is the capital city of France?" if the PDF file contains information about French geography.

    Get an answer: After entering a question, the tool will search the PDF file for relevant information and return the answer to the user's question. If the tool is unable to find an answer, it will return a message indicating that it was unable to find an answer.

Implementation

The PDF Search tool is implemented using the following technologies:

    Streamlit: Streamlit is a Python library that makes it easy to build web applications for machine learning and data science. The tool uses Streamlit to create a simple web interface for users to upload PDF files and ask questions.
    PyPDF2: PyPDF2 is a Python library that allows developers to read and manipulate PDF files. The tool uses PyPDF2 to extract text from the uploaded PDF file.
    LangChain: LangChain is a Python library that provides a framework for building language models and performing natural language processing tasks. The tool uses LangChain to perform similarity search and question answering on the text extracted from the PDF file.

The tool is implemented in Python and consists of a single file, app.py, which contains the code to launch the tool and perform the necessary processing tasks. The code is well-documented and easy to understand, making it easy for developers to modify and extend the tool to meet their needs.
Contributions

Contributions to the PDF Search tool are welcome and encouraged. If you find a bug or have a feature request, please submit an issue on GitHub. If you would like to contribute code, please fork the repository, create a new branch, and submit a pull request.
