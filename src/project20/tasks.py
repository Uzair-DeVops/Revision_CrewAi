from crewai import Task 
from crewai_tools import SerperDevTool ,ScrapeWebsiteTool



InternetSearchTool = SerperDevTool()
# WebsiteScraper = ScrapeWebsiteTool()

from dotenv import load_dotenv

load_dotenv()


class MyTasks:
    def Out_liner_T(self ,agent ,topic):
        return Task(
            description= f"""  
              write a detailed outline for a book on the mentioned topic it must contain 10 chapters and each chapter headlines should be descriptive u must use all the available  tools 
                               
            parameter:
            topic: {topic}      
                                  """,
            agent= agent, 
            tools=[InternetSearchTool],
            expected_output= f""" your output should be according to the following mentioned structure

                                1. Introduction (500words)
                                2. Theoretical Framework(200words)
                                3. Literature Review(1000words)
                                4. Research Methodology(500words)
                                5. Data Analysis(200words)
                                6. Results and Conclusion(500words)
                                7. Discussion(400words)
                                8. References
                                9. Appendices
                                10. Future Work
                                """,
        )
    
    def Book_Writer_T(self ,agent ,context):
        return Task(
            description= f"""  
              write a detailed book on the provided outline it should be descriptive
                               
         
                                  """,
            agent= agent,
            async_execution=True,
            context = context,
            expected_output= f""" your output should be according to the following mentioned structure
            1. Introduction (500words)
            2. Theoretical Framework(200words)
            3. Literature Review(1000words)
            4. Research Methodology(500words)
            5. Data Analysis(200words)
            6. Results and Conclusion(500words)
            7. Discussion(400words)
            8. References
            9. Appendices
            10. Future Work


            make a professionally  formatted Book according to the international standards
                                """,
        )