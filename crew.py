from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, writing_task



# Configure Crew
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Start execution
# result = crew.kickoff(inputs={'topic': 'flutter'})
# print(result)
