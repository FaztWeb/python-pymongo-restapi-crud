from dataclasses import dataclass
from dataclasses_json import dataclass_json

# from .Alias import Alias


@dataclass_json
@dataclass(kw_only=True)
class Person:
    _id = None
    document_number: str = None
    name: str = None
    mail_address: str = None
    phone_number: str = None
    type_document: str = None
    gender: str = None


# @dataclass_json
# @dataclass
# class Project:
#     _id = Alias("projectid")
#     projectid: str = None
#     name: str = None
#     managerid: str = None
#     state: str = None
#     start_date: str = None
#     end_date: str = None


# @dataclass_json
# @dataclass
# class ProjectTeams:
#     _id = Alias("projectteamsid")
#     projectteamsid: int
#     projectid: str = None
#     personid: str = None


# @dataclass_json
# @dataclass
# class ProjectFiles:
#     _id = Alias("projectfilesid")
#     projectfilesid: int
#     projectid: str = None
#     path: str = None


# @dataclass_json
# @dataclass
# class TaskStages:
#     _id = Alias("projectstagesid")
#     projectstagesid: int
#     order: int
#     name: str = None
#     taskid: str = None


# @dataclass_json
# @dataclass
# class Task:
#     _id = Alias("taskid")
#     taskid: str = None
#     type: str = None
#     subject: str = None
#     ownerid: str = None
#     projectstageid: int
#     managerid: str = None
#     description: str = None
#     isblock: bool


# @dataclass_json
# @dataclass
# class TaskNotes:
#     _id = Alias("tasknotesid")
#     tasknotesid: int
#     taskid: str = None
#     note: str = None
#     state: str = None


# @dataclass_json
# @dataclass
# class RelationTask:
#     _id = Alias("relationtaskid")
#     relationtaskid: int
#     taskid: str = None
#     parenttaskid: str = None


# @dataclass_json
# @dataclass
# class ProjectTasks:
#     _id = Alias("projecttasksid")
#     projecttasksid: int
#     projectid: str = None
#     taskid: str = None


# @dataclass_json
# @dataclass
# class Keyword:
#     _id = Alias("keywordid")
#     keywordid: str = None
#     name: str = None


# @dataclass_json
# @dataclass
# class TaskKeywords:
#     _id = Alias("taskkeywordsid")
#     taskkeywordsid: int
#     taskid: str = None
#     keywordid: str = None