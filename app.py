import streamlit as st
import os
from crew import create_crew  # Import the modified create_crew function
from tools import YT_Tool
from crewai_tools import YoutubeChannelSearchTool
from agents import blog_researcher, blog_writer  # importing agents 


def update_yt_tool(channel_handle):
    """Dynamically update the YouTube channel handle"""
    global YT_Tool
    # Create a new instance and update the global variable
    YT_Tool = YoutubeChannelSearchTool(youtube_channel_handle=channel_handle)
    
    # Update the tools for both agents
    blog_researcher.tools = [YT_Tool]
    blog_writer.tools = [YT_Tool]
    
def main():
    st.title("AI-Powered Blog Generator")
    
    # Input fields for YouTube channel handle and topic
    channel_handle = st.text_input("Enter the YouTube channel handle (e.g., @flutterguys):")
    topic = st.text_input("Enter a topic for your blog:")

    if st.button("Generate Blog"):  
        if channel_handle.strip() and topic.strip():
            with st.spinner("Generating content..."):
                # Update the YT_Tool dynamically with the new channel handle
                update_yt_tool(channel_handle)

                # Create and run crew with the given topic
                crew = create_crew(topic)
                result = crew.kickoff()

                # Extract actual content from CrewOutput
                blog_content = str(result)

                # Save result to session state
                st.session_state['blog_content'] = blog_content
                
                # Write content to a file
                with open("new-blog-post.md", "w", encoding="utf-8") as f:
                    f.write(blog_content)
                
                st.success("Blog generated successfully!")
        else:
            st.warning("Please enter both the YouTube channel handle and topic before generating.")
    
    # Display stored content if available
    if 'blog_content' in st.session_state:
        st.subheader("Generated Blog Content:")
        st.write(st.session_state['blog_content'])
        
        # Provide download option
        with open("new-blog-post.md", "r", encoding="utf-8") as f:
            blog_file_content = f.read()
        
        st.download_button(
            label="Download Blog as Markdown",
            data=blog_file_content,
            file_name="new-blog-post.md",
            mime="text/markdown"
        )

if __name__ == "__main__":
    main()
