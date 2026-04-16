from datetime import datetime, date, time
from typing import Any, List, Optional, Union, Set
from enum import Enum
from pydantic import BaseModel, field_validator


############################################
# Enumerations are defined here
############################################

class PriorityLevel(Enum):
    High = "High"
    Medium = "Medium"
    Low = "Low"

class TaskStatus(Enum):
    Pending = "Pending"
    InProgress = "InProgress"
    Completed = "Completed"
    Cancelled = "Cancelled"

############################################
# Classes are defined here
############################################
class TaskCreate(BaseModel):
    updatedAt: Optional[date] = None
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.Pending
    priority: PriorityLevel = PriorityLevel.Medium
    title: str
    taskId: str
    dueDate: Optional[date] = None
    createdAt: date
    contains: int  # N:1 Relationship (mandatory)


class ToDoListCreate(BaseModel):
    listId: str
    description: Optional[str] = None
    title: str
    updatedAt: Optional[date] = None
    createdAt: date
    user: int  # N:1 Relationship (mandatory)
    task: Optional[List[int]] = None  # 1:N Relationship


class UserCreate(BaseModel):
    email: str
    username: str
    userId: str
    passwordHash: str
    createdAt: date
    owns: Optional[List[int]] = None  # 1:N Relationship


