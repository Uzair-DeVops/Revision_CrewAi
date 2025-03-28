from .agents import BookWriterAgents
from .tasks import MyTasks
from crewai import Crew

# initialize

agents = BookWriterAgents()
tasks = MyTasks()



out_liner = agents.Out_liner()
Book_Writer = agents.Book_Writer()

out_liner_T = tasks.Out_liner_T(
    agent=out_liner,
    topic="Machine learning"
)

Book_Writer_T = tasks.Book_Writer_T(
    agent=Book_Writer,
    context=[out_liner_T]
)


crew = Crew(        
    tasks=[out_liner_T , Book_Writer_T],
    agents=[out_liner , Book_Writer],
    verbose = True,
)

def Writer():
    result = crew.kickoff()
    print(f"Final Result: {result}")