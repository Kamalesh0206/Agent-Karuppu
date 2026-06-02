from pathlib import Path
import yaml

from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai import Agent, Task, Crew

@CrewBase
class InstagramAgent:

    @agent
    def researcher(self) -> Agent:
        ...

    @task
    def research_task(self) -> Task:
        ...

    @crew
    def crew(self) -> Crew:
        ...

class InstagramAgent:

    def __init__(self):
        config_dir = Path(__file__).parent / "config"

        with open(config_dir / "agents.yaml", "r", encoding="utf-8") as f:
            self.agents_config = yaml.safe_load(f)

        with open(config_dir / "tasks.yaml", "r", encoding="utf-8") as f:
            self.tasks_config = yaml.safe_load(f)

    def researcher(self):
        return Agent(
            config=self.agents_config["researcher"]
        )

    def research_task(self):
        return Task(
            config=self.tasks_config["research_task"],
            agent=self.researcher()
        )

    def crew(self):
        return Crew(
            agents=[self.researcher()],
            tasks=[self.research_task()],
            process=Process.sequential,
            verbose=True
        )
