Capy – AI-Powered Student Support Web Application

Capy is a web application designed to support current and prospective university students in improving their academic journey and navigating university processes. Unlike apps like Notion, which provide general student tools, Capy offers personalized and continuous support, focusing not only on organizational tools but also on enhancing soft skills and providing actionable guidance for students.

Features

Personalized support for current and future students

AI-powered chatbot to assist with university processes and queries

Tools to improve soft skills and academic productivity

Context-aware responses leveraging embeddings for better understanding

Technology Stack

Backend: Python Django

Integrates OpenAI API for AI-driven chatbot functionality

Uses embeddings to maintain context in conversations

Frontend: Bootstrap for responsive and user-friendly interface

How It Works

Students interact with the Capy chatbot via the web interface.

User queries are sent to the backend, which processes them using OpenAI API and embeddings to provide contextual and accurate responses.

Students receive guidance, tips, and tools tailored to their needs.

Getting Started
Prerequisites

Python 3.10+

Django 4.x

Access to OpenAI API key

Installation
# Clone the repository
git clone https://github.com/yourusername/capy.git
cd capy

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver


Open your browser at http://127.0.0.1:8000 to see Capy in action.
