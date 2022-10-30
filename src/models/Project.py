from dataclasses import dataclass, field
from typing import List

from dataclasses_json import dataclass_json

from models.Person import Person
from models.Task import Task


@dataclass_json
@dataclass
class Project:
    managerid = None
    teams: List[Person] = field(default_factory=lambda: [])
    tasks: List[Task] = field(default_factory=lambda: [])
    name: str = None
    state: str = None
    start_date: str = None
    end_date: str = None
    stages: List[str] = field(
        default_factory=lambda: ["PLANNING", "DESIGN", "TODO", "TEST", "END"]
    )
    types_task: List[str] = field(default_factory=lambda: ["TASK", "INCIDENT"])
