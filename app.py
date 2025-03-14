import streamlit as st
import os
from crew import crew  # Importing the CrewAI pipeline

def main():
    st.title("AI-Powered Blog Generator")
    
    # Input field for topic
    topic = st.text_input("Enter a topic for your blog:")
    
    if st.button("Generate Blog"):  
        if topic.strip():
            with st.spinner("Generating content..."):
                result = crew.kickoff(inputs={'topic': topic})  # Running CrewAI
                
                # Extract actual content from CrewOutput
                blog_content = str(result)  # Convert CrewOutput to string
                
                # Save result to session state (local storage alternative in Streamlit)
                st.session_state['blog_content'] = blog_content  
                
                # Write content to a file
                with open("new-blog-post.md", "w", encoding="utf-8") as f:
                    f.write(blog_content)
                
                st.success("Blog generated successfully!")
        else:
            st.warning("Please enter a topic before generating.")
    
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
