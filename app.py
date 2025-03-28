import streamlit as st
from src.project20.agents import BookWriterAgents
from src.project20.tasks import MyTasks
from crewai import Crew

def main():
    st.title("📘 AI Book Writing Crew")
    
    # User input for book topic
    topic = st.text_input("Enter the book topic:", placeholder="Machine Learning")
    
    if st.button("Write Book"):
        if not topic:
            st.warning("Please enter a book topic!")
            return
            
        with st.spinner("🧠 Generating your book... This might take a moment"):
            try:
                # Initialize agents and tasks
                agents = BookWriterAgents()
                tasks = MyTasks()

                # Create agents
                outliner = agents.Out_liner()
                writer = agents.Book_Writer()

                # Create tasks
                outline_task = tasks.Out_liner_T(
                    agent=outliner,
                    topic=topic
                )

                writing_task = tasks.Book_Writer_T(
                    agent=writer,
                    context=[outline_task]
                )

                # Create and run crew
                crew = Crew(
                    agents=[outliner, writer],
                    tasks=[outline_task, writing_task],
                    verbose=True
                )

                result = crew.kickoff()
                
                # Display results
                st.subheader("Generated Book Content")
                st.markdown(result)  # Escape markdown formatting
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()