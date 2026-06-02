import os
import json
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	DirectoryReadTool,
	FileReadTool,
	ScrapeWebsiteTool,
	SerperDevTool
)


from pydantic import BaseModel
from jambo import SchemaConverter


@CrewBase
class InstagramMultiAccountPublisherCrew:
    """InstagramMultiAccountPublisher crew"""

    
    @agent
    def instagram_multi_account_publishing_coordinator(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["instagram_multi_account_publishing_coordinator"],
            from_repository="instagram-multi-account-publishing-coordinator",
            
            
            tools=[				DirectoryReadTool(),
				FileReadTool(),
				ScrapeWebsiteTool(),
				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    

    
    @task
    def publish_instagram_content(self) -> Task:
        return Task(
            config=self.tasks_config["publish_instagram_content"],
            markdown=True,
            output_json=self._load_response_format("publish_instagram_content"),
            guardrail="Ensure the output contains publishing status, account names, success count, failure count, timestamps, and error details. Do not expose access tokens, passwords, or sensitive account information.",
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the InstagramMultiAccountPublisher crew"""

        # Custom manager agent for hierarchical process
        manager_agent = Agent(
            role="Crew Manager",
            goal="Manage Instagram content publishing workflows, validate user inputs, coordinate account selection, track publishing requests, and generate publishing reports.",
            backstory="You are an experienced social media automation manager responsible for coordinating Instagram publishing operations across multiple accounts. You ensure content is validated, publishing requests are processed correctly, failures are tracked, and users receive accurate status updates.",
            llm=LLM(model="openai/gpt-4.1"),
            allow_delegation=True,
        )

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.hierarchical,
            verbose=True,


            manager_agent=manager_agent,


            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)

