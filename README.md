# Apartment Social Networking Application: Resi-Connect
This project is a simple social networking application designed for apartment dwellers to help them connect and converse about topics relevant to their living situation.
## Features
- Feed showing all posts from residents, sorted in reverse chronological order.
- Residents identifiable by name and apartment number.
- Ability to view posts by a specific resident or from a specific apartment.
- Minimal and mobile-responsive design.
## Tech Stack
- **Backend**: Django
- **Frontend**: Next.js
## Getting Started
Follow the instructions below to set up the project locally.
### Prerequisites
- Python (3.7 or higher)
- Node.js (10.13 or higher)
### Backend Setup
1. **Clone the repository:**
    ```bash
    git clone https://github.com/Arslan2591/assignment.git
    cd assignment
    ```
2. **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
3. **Create a Python virtual environment:**
    ```bash
    python -m venv env
    ```
4. **Activate the virtual environment:**
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source env/bin/activate
        ```
5. **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
6. **Run the Django development server:**
    ```bash
    python manage.py runserver
    ```
### Frontend Setup
1. **Navigate to the frontend directory:**
    ```bash
    cd ../frontend
    ```
2. **Install the required Node.js packages:**
    ```bash
    npm install
    ```
3. **Run the Next.js development server:**
    ```bash
    npm run dev
    ```
Now, both the backend and frontend servers are running. You can access the application at [http://localhost:3000](http://localhost:3000).
## Contributing
If you want to contribute, feel free to open a pull request.
## License
This project is open-source and available under the MIT License.
