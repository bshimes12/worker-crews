# CrewAI Example Project

This is a simple example of how to set up and run a CrewAI project with proper virtual environment isolation and environment variable management.

## Setup Instructions

1. **Create and activate virtual environment:**
   ```bash
   python3 -m venv crewai_env
   source crewai_env/bin/activate  # On Windows: crewai_env\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API keys:**
   - Edit the `.env` file and replace `your_openai_api_key_here` with your actual OpenAI API key
   - You can also add other API keys as needed (e.g., SERPER_API_KEY for search)

4. **Run the example:**
   ```bash
   python main.py
   ```

## Project Structure

- `main.py`: Contains the CrewAI example with generic agent and task names
- `requirements.txt`: Lists the required Python packages
- `.env`: Stores API keys (not committed to version control)
- `.gitignore`: Excludes sensitive files from version control
- `crewai_env/`: Virtual environment directory (not committed to version control)

## Customization

To customize this example for your own use:
1. Modify the agent roles, goals, and backstories in `main.py`
2. Adjust the task descriptions and expected outputs
3. Add new agents and tasks as needed
4. Update the `.env` file with any additional API keys
