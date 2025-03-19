from crewai import Crew, Process, Task
from agents import blog_researcher, blog_writer
from tasks import research_task, writing_task

def create_crew(topic):
    # Configure Crew with dynamic topic
    research = Task(
        description=research_task.description.format(topic=topic),
        expected_output=research_task.expected_output.format(topic=topic),
        tools=research_task.tools,
        agent=research_task.agent
    )
    
    writing = Task(
        description=writing_task.description.format(topic=topic),
        expected_output=writing_task.expected_output.format(topic=topic),
        tools=writing_task.tools,
        agent=writing_task.agent,
        async_execution=writing_task.async_execution,
        output_file=writing_task.output_file
    )

    crew = Crew(
        agents=[blog_researcher, blog_writer],
        tasks=[research, writing],
        process=Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        share_crew=True
    )
    return crew

# Start execution
# result = crew.kickoff(inputs={'topic': 'flutter'})
# print(result)
