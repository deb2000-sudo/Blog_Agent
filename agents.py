from crewai import Agent

## Create a senior blog content researcher
from dotenv import load_dotenv
load_dotenv()
import os
os.environ["OPENAI_MODEL_NAME"]=os.getenv("OPENAI_MODEL_NAME")
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")


from tools import YT_Tool

blog_researcher=Agent(
    role='Blog Researcher from youtube videos',
    goal="get the relevant video content for the topic{topic} from YT cahnel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding flutter and dart, React Framework"
    ),
    tools=[YT_Tool],
    allow_delegataion=True,
)

## create a senior writer agent with YT tool
blog_writer=Agent(
    role='Blog Writer',
    goal="Narrate compelling tech stories about the video {topic} from YT channel",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narraties that captivate and educate, bringing new"
        "discoveries to light in an accessible manner. "
    ),
    tools=[YT_Tool],
    allow_delegataion=False,
)