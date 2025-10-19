import os
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define a generic researcher agent
researcher = Agent(
    role='Researcher',
    goal='Research and gather information on the given topic',
    backstory='An expert researcher with skills in gathering and analyzing information.',
    verbose=True,
    allow_delegation=False
)

# Define a generic writer agent
writer = Agent(
    role='Writer',
    goal='Write clear and concise content based on research findings',
    backstory='A skilled writer who can transform complex information into readable content.',
    verbose=True,
    allow_delegation=False
)

# Define a research task
research_task = Task(
    description='Research the latest trends in artificial intelligence',
    agent=researcher,
    expected_output='A list of 5 key AI trends with brief descriptions'
)

# Define a writing task that uses the research output
writing_task = Task(
    description='Write a short article based on the AI trends research',
    agent=writer,
    expected_output='A 300-word article summarizing the AI trends'
)

# Create the crew with both agents and tasks
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)

# Execute the crew
if __name__ == "__main__":
    result = crew.kickoff()
    print("Crew execution result:")
    print(result)
