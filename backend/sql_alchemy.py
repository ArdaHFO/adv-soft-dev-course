import enum
from typing import List as List_, Optional as Optional_
from sqlalchemy import (
    create_engine, Column as Column_, ForeignKey as ForeignKey_, Table as Table_, 
    Text as Text_, Boolean as Boolean_, String as String_, Date as Date_, 
    Time as Time_, DateTime as DateTime_, Float as Float_, Integer as Integer_, Enum
)
from sqlalchemy.orm import (
    column_property, DeclarativeBase, Mapped as Mapped_, mapped_column, relationship
)
from datetime import datetime as dt_datetime, time as dt_time, date as dt_date

class Base(DeclarativeBase):
    pass

# Definitions of Enumerations
class PriorityLevel(enum.Enum):
    High = "High"
    Medium = "Medium"
    Low = "Low"

class TaskStatus(enum.Enum):
    Pending = "Pending"
    InProgress = "InProgress"
    Completed = "Completed"
    Cancelled = "Cancelled"


# Tables definition for many-to-many relationships

# Tables definition
class Task(Base):
    __tablename__ = "task"
    id: Mapped_[int] = mapped_column(primary_key=True)
    taskId: Mapped_[str] = mapped_column(String_(100))
    title: Mapped_[str] = mapped_column(String_(100))
    description: Mapped_[Optional_[str]] = mapped_column(String_(100), nullable=True)
    dueDate: Mapped_[Optional_[dt_date]] = mapped_column(Date_, nullable=True)
    priority: Mapped_[PriorityLevel] = mapped_column(Enum(PriorityLevel), default=PriorityLevel.Medium)
    status: Mapped_[TaskStatus] = mapped_column(Enum(TaskStatus), default=TaskStatus.Pending)
    createdAt: Mapped_[dt_date] = mapped_column(Date_)
    updatedAt: Mapped_[Optional_[dt_date]] = mapped_column(Date_, nullable=True)
    contains_id: Mapped_[int] = mapped_column(ForeignKey_("todolist.id"))

class ToDoList(Base):
    __tablename__ = "todolist"
    id: Mapped_[int] = mapped_column(primary_key=True)
    listId: Mapped_[str] = mapped_column(String_(100))
    title: Mapped_[str] = mapped_column(String_(100))
    description: Mapped_[Optional_[str]] = mapped_column(String_(100), nullable=True)
    createdAt: Mapped_[dt_date] = mapped_column(Date_)
    updatedAt: Mapped_[Optional_[dt_date]] = mapped_column(Date_, nullable=True)
    user_id: Mapped_[int] = mapped_column(ForeignKey_("user.id"))

class User(Base):
    __tablename__ = "user"
    id: Mapped_[int] = mapped_column(primary_key=True)
    userId: Mapped_[str] = mapped_column(String_(100))
    username: Mapped_[str] = mapped_column(String_(100))
    email: Mapped_[str] = mapped_column(String_(100))
    passwordHash: Mapped_[str] = mapped_column(String_(100))
    createdAt: Mapped_[dt_date] = mapped_column(Date_)


#--- Relationships of the task table
Task.contains: Mapped_["ToDoList"] = relationship("ToDoList", back_populates="task", foreign_keys=[Task.contains_id])

#--- Relationships of the todolist table
ToDoList.user: Mapped_["User"] = relationship("User", back_populates="owns", foreign_keys=[ToDoList.user_id])
ToDoList.task: Mapped_[List_["Task"]] = relationship("Task", back_populates="contains", foreign_keys=[Task.contains_id])

#--- Relationships of the user table
User.owns: Mapped_[List_["ToDoList"]] = relationship("ToDoList", back_populates="user", foreign_keys=[ToDoList.user_id])

# Database connection
DATABASE_URL = "sqlite:///Class_Diagram.db"  # SQLite connection
engine = create_engine(DATABASE_URL, echo=True)

# Create tables in the database
Base.metadata.create_all(engine, checkfirst=True)