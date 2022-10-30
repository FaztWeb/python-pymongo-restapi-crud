from dataclasses import dataclass, field
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Task:
    projectstageid = None
    managerid = None
    ownerid = None
    notes: List[str] = field(default_factory=lambda: [])
    keywords: List[str] = field(default_factory=lambda: [])
    taskstage: str = None
    description: str = None
    type_task: str = None
    subject: str = None
    isblock: bool = False
