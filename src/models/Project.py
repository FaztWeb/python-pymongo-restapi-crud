from asyncio import tasks
from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json
from models.Task import Task
from models.Person import Person


@dataclass_json
@dataclass
class Project:
    managerid = None
    teams: List[Person] = None
    tasks: List[Task] = None
    name: str = None
    state: str = None
    start_date: str = None
    end_date: str = None
    stages = ["PLANNING", "DESIGN", "TODO", "TEST", "END"]
    types_task = ["TASK", "INCIDENT"]