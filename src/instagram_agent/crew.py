from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, task, crew

@CrewBase
class InstagramAgent:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self):
        return Agent(
            config=self.agents_config["researcher"]
        )

    @task
    def research_task(self):
        return Task(
            config=self.tasks_config["research_task"]
        )

    @crew
    def crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True
        )
