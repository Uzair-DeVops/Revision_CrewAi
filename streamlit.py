import streamlit as st
from .src.project20.agents import BookWriterAgents
from .src.project20.tasks import MyTasks
from crewai import Crew

# Streamlit App
def main():
    st.title("AI-Powered Book Writer")
    topic = st.text_input("Enter the book topic:", "Machine learning")
    
    if st.button("Generate Book"):
        agents = BookWriterAgents()
        tasks = MyTasks()

        out_liner = agents.Out_liner()
        Book_Writer = agents.Book_Writer()

        out_liner_T = tasks.Out_liner_T(
            agent=out_liner,
            topic=topic
        )

        Book_Writer_T = tasks.Book_Writer_T(
            agent=Book_Writer,
            context=[out_liner_T]
        )

        crew = Crew(
            tasks=[out_liner_T, Book_Writer_T],
            agents=[out_liner, Book_Writer],
            verbose=True,
        )

        result = crew.kickoff()
        st.success("Book outline generated successfully!")
        st.text_area("Generated Outline:", result, height=300)

if __name__ == "__main__":
    main()
