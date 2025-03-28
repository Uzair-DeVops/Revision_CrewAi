from crewai import Agent , LLM
from dotenv import load_dotenv


load_dotenv()

from crewai_tools import SerperDevTool ,ScrapeWebsiteTool



InternetSearchTool = SerperDevTool()
WebsiteScraper = ScrapeWebsiteTool()
model = LLM(model="gemini/gemini-2.0-flash-exp")



class BookWriterAgents:

    def Out_liner(self):
        return Agent(
            role = "Out_liner",
            goal = "develop a detailed outline for the book",
            backstory = "i am a expert in writing book outlines and i have 10+ years of experience in writing book outlines",
            verbose=True,
            llm=model,
        
        )
    
    def Book_Writer(self):
        return Agent(
            role = "Book_Writer",
            goal = "develop a detailed Book on provided outline",
            backstory = "i am a expert in writing books and i have 10+ years of experience in writing books",
            verbose=True,
            llm=model,
        
        )