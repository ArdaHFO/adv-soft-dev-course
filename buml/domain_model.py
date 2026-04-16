####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata, MethodImplementationType
)

# Enumerations
TaskStatus: Enumeration = Enumeration(
    name="TaskStatus",
    literals={
            EnumerationLiteral(name="Cancelled"),
			EnumerationLiteral(name="Pending"),
			EnumerationLiteral(name="InProgress"),
			EnumerationLiteral(name="Completed")
    }
)

PriorityLevel: Enumeration = Enumeration(
    name="PriorityLevel",
    literals={
            EnumerationLiteral(name="Low"),
			EnumerationLiteral(name="Medium"),
			EnumerationLiteral(name="High")
    }
)

# Classes
User = Class(name="User")
ToDoList = Class(name="ToDoList")
Task = Class(name="Task")

# User class attributes and methods
User_userId: Property = Property(name="userId", type=StringType, visibility="private")
User_username: Property = Property(name="username", type=StringType, visibility="private")
User_email: Property = Property(name="email", type=StringType, visibility="private")
User_passwordHash: Property = Property(name="passwordHash", type=StringType, visibility="private")
User_createdAt: Property = Property(name="createdAt", type=DateType, visibility="private")
User_m_authenticate: Method = Method(name="authenticate", parameters={Parameter(name='password', type=StringType)}, type=BooleanType, implementation_type=MethodImplementationType.CODE)
User_m_authenticate.code = """def authenticate(self, password: str) -> bool:
    # Implement password verification logic here
    # For example, compare hashed password
    return verify_password_hash(password, self.passwordHash)  # assuming verify_password_hash is defined elsewhere
    """
User_m_goToToDoList: Method = Method(name="goToToDoList", parameters={Parameter(name='listId', type=StringType)}, implementation_type=MethodImplementationType.CODE)
User_m_goToToDoList.code = """def goToToDoList(self, listId: str) -> None:
    # Logic to navigate to ToDoList page in GUI
    print(f"Navigating to ToDoList with id: {listId}")
    """
User.attributes={User_createdAt, User_email, User_passwordHash, User_userId, User_username}
User.methods={User_m_authenticate, User_m_goToToDoList}

# ToDoList class attributes and methods
ToDoList_listId: Property = Property(name="listId", type=StringType, visibility="private")
ToDoList_title: Property = Property(name="title", type=StringType, visibility="private")
ToDoList_description: Property = Property(name="description", type=StringType, visibility="private", is_optional=True)
ToDoList_createdAt: Property = Property(name="createdAt", type=DateType, visibility="private")
ToDoList_updatedAt: Property = Property(name="updatedAt", type=DateType, visibility="private", is_optional=True)
ToDoList_m_addTask: Method = Method(name="addTask", parameters={Parameter(name='task', type=Task)}, type=AnyType, implementation_type=MethodImplementationType.CODE)
ToDoList_m_addTask.code = """def addTask(self, task: Task) -> None:
    # Add task to the ToDoList
    self.tasks.append(task)
    self.updatedAt = datetime.now()  # assuming datetime is imported
    """
ToDoList_m_goToTask: Method = Method(name="goToTask", parameters={Parameter(name='taskId', type=StringType)}, implementation_type=MethodImplementationType.CODE)
ToDoList_m_goToTask.code = """def goToTask(self, taskId: str) -> None:
    # Logic to navigate to Task detail page in GUI
    print(f"Navigating to Task with id: {taskId}")
    """
ToDoList.attributes={ToDoList_createdAt, ToDoList_description, ToDoList_listId, ToDoList_title, ToDoList_updatedAt}
ToDoList.methods={ToDoList_m_addTask, ToDoList_m_goToTask}

# Task class attributes and methods
Task_taskId: Property = Property(name="taskId", type=StringType, visibility="private")
Task_title: Property = Property(name="title", type=StringType, visibility="private")
Task_description: Property = Property(name="description", type=StringType, visibility="private", is_optional=True)
Task_dueDate: Property = Property(name="dueDate", type=DateType, visibility="private", is_optional=True)
Task_priority: Property = Property(name="priority", type=PriorityLevel, visibility="private", default_value="Medium")
Task_status: Property = Property(name="status", type=TaskStatus, visibility="private", default_value="Pending")
Task_createdAt: Property = Property(name="createdAt", type=DateType, visibility="private")
Task_updatedAt: Property = Property(name="updatedAt", type=DateType, visibility="private", is_optional=True)
Task_m_markComplete: Method = Method(name="markComplete", parameters={}, implementation_type=MethodImplementationType.CODE)
Task_m_markComplete.code = """def markComplete(self) -> None:
    self.status = TaskStatus.COMPLETED
    self.updatedAt = datetime.now()  # assuming datetime is imported
    """
Task.attributes={Task_createdAt, Task_description, Task_dueDate, Task_priority, Task_status, Task_taskId, Task_title, Task_updatedAt}
Task.methods={Task_m_markComplete}

# Relationships
owns: BinaryAssociation = BinaryAssociation(
    name="owns",
    ends={
        Property(name="user", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="owns", type=ToDoList, multiplicity=Multiplicity(0, 9999))
    }
)
contains: BinaryAssociation = BinaryAssociation(
    name="contains",
    ends={
        Property(name="task", type=Task, multiplicity=Multiplicity(0, 9999)),
        Property(name="contains", type=ToDoList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Class_Diagram",
    types={User, ToDoList, Task, TaskStatus, PriorityLevel},
    associations={owns, contains},
    generalizations={},
    metadata=None
)
