from crewai import Task
from tools import YT_Tool
from agents import blog_researcher, blog_writer

##Research Task

research_task=Task(
    description=(
        "Identify the video {topic}."
        "Get detailed information about the video from the channel"
    ),
    expected_output="A compprehensive 3 paragraphs long report on the {topic} of video content",
    tools=[YT_Tool],
    agent=blog_researcher,
    
)

writing_task=Task(
    description=(
        "get the info from the youtube channel on the topic {topic}."
        
    ),
    expected_output="Summarize the info from the youtube channel video on the topic {topic} and create the content for the blog",
    tools=[YT_Tool],
    agent=blog_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)