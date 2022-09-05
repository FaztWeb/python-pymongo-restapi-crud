from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Task:
    projectstageid = None
    managerid = None
    ownerid = None
    tasknotes: List = None
    keywords: List = None
    taskstage: str = None
    description: str = None
    type_task: str = None
    subject: str = None
    isblock: bool = False