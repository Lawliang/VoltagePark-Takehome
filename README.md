### GENERAL

Hello Voltage Park Team, thank you for giving me the opportunity to work on this takehome! It was pretty fun.

Let me know if you have any questions/inquiries for me. Any addtl feedback is always appreciated as well! Thanks.

### SETUP

1. Setup & run backend environment + install modules:
    a. Open new terminal.
    b. Create a virtual environment via running CLI 'python -m venv .venv' in terminal
    c. Run 'source .venv/bin/activate' (mac) or '.\.venv\Scripts\activate' (windows)
    d. Navigate to 'backend' subdirectory and run 'pip install -r requirements.txt'
    e. Run 'python manage.py runserver' to spin up backend API server.

2. Setup & run frontend environment + install modules:
    a. Navigate to 'frontend' subdirectory
    b. Run 'npm install' to install all modules.
    c. Run 'npm run dev' to spin up frontend development server.

3. Tests have been included for the three critical backend endpoints. Use CLI command 'python manage.py test' to initiate testing sequence.

4. Move validation is happening on the backend after each move- therefore, I decided to use Redis to persist data + retrieve the latest game state. I made this decision in hopes of optimize network response times in case of high traffic to avoid unnecessary database reads/writes after each move on every game.
    a. Confirm that Redis has been installed on your machine. Run 'brew install Redis' and 'brew services start redis'. 
    b. Verify that Redis is running with the CLI 'redis-cli ping'. You should see a pong response.
