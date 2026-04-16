import uvicorn
import os, json
import time as time_module
import logging
from fastapi import Depends, FastAPI, HTTPException, Request, status, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from pydantic_classes import *
from sql_alchemy import *

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

############################################
#
#   Initialize the database
#
############################################

def init_db():
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/Class_Diagram.db")
    # Ensure local SQLite directory exists (safe no-op for other DBs)
    os.makedirs("data", exist_ok=True)
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
        echo=False
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    return SessionLocal

app = FastAPI(
    title="Class_Diagram API",
    description="Auto-generated REST API with full CRUD operations, relationship management, and advanced features",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_tags=[
        {"name": "System", "description": "System health and statistics"},
        {"name": "Task", "description": "Operations for Task entities"},
        {"name": "Task Relationships", "description": "Manage Task relationships"},
        {"name": "Task Methods", "description": "Execute Task methods"},
        {"name": "ToDoList", "description": "Operations for ToDoList entities"},
        {"name": "ToDoList Relationships", "description": "Manage ToDoList relationships"},
        {"name": "ToDoList Methods", "description": "Execute ToDoList methods"},
        {"name": "User", "description": "Operations for User entities"},
        {"name": "User Relationships", "description": "Manage User relationships"},
        {"name": "User Methods", "description": "Execute User methods"},
    ]
)

# Enable CORS for all origins (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

############################################
#
#   Middleware
#
############################################

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all incoming requests and responses."""
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

# Request timing middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Add processing time header to all responses."""
    start_time = time_module.time()
    response = await call_next(request)
    process_time = time_module.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

############################################
#
#   Exception Handlers
#
############################################

# Global exception handlers
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    """Handle ValueError exceptions."""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "Bad Request",
            "message": str(exc),
            "detail": "Invalid input data provided"
        }
    )


@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    """Handle database integrity errors."""
    logger.error(f"Database integrity error: {exc}")

    # Extract more detailed error information
    error_detail = str(exc.orig) if hasattr(exc, 'orig') else str(exc)

    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "error": "Conflict",
            "message": "Data conflict occurred",
            "detail": error_detail
        }
    )


@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError):
    """Handle general SQLAlchemy errors."""
    logger.error(f"Database error: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal Server Error",
            "message": "Database operation failed",
            "detail": "An internal database error occurred"
        }
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions with consistent format."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail if isinstance(exc.detail, str) else "HTTP Error",
            "message": exc.detail,
            "detail": f"HTTP {exc.status_code} error occurred"
        }
    )

# Initialize database session
SessionLocal = init_db()
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        logger.error("Database session rollback due to exception")
        raise
    finally:
        db.close()

############################################
#
#   Global API endpoints
#
############################################

@app.get("/", tags=["System"])
def root():
    """Root endpoint - API information"""
    return {
        "name": "Class_Diagram API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health", tags=["System"])
def health_check():
    """Health check endpoint for monitoring"""
    from datetime import datetime
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "database": "connected"
    }


@app.get("/statistics", tags=["System"])
def get_statistics(database: Session = Depends(get_db)):
    """Get database statistics for all entities"""
    stats = {}
    stats["task_count"] = database.query(Task).count()
    stats["todolist_count"] = database.query(ToDoList).count()
    stats["user_count"] = database.query(User).count()
    stats["total_entities"] = sum(stats.values())
    return stats


############################################
#
#   BESSER Action Language standard lib
#
############################################


async def BAL_size(sequence:list) -> int:
    return len(sequence)

async def BAL_is_empty(sequence:list) -> bool:
    return len(sequence) == 0

async def BAL_add(sequence:list, elem) -> None:
    sequence.append(elem)

async def BAL_remove(sequence:list, elem) -> None:
    sequence.remove(elem)

async def BAL_contains(sequence:list, elem) -> bool:
    return elem in sequence

async def BAL_filter(sequence:list, predicate) -> list:
    return [elem for elem in sequence if predicate(elem)]

async def BAL_forall(sequence:list, predicate) -> bool:
    for elem in sequence:
        if not predicate(elem):
            return False
    return True

async def BAL_exists(sequence:list, predicate) -> bool:
    for elem in sequence:
        if predicate(elem):
            return True
    return False

async def BAL_one(sequence:list, predicate) -> bool:
    found = False
    for elem in sequence:
        if predicate(elem):
            if found:
                return False
            found = True
    return found

async def BAL_is_unique(sequence:list, mapping) -> bool:
    mapped = [mapping(elem) for elem in sequence]
    return len(set(mapped)) == len(mapped)

async def BAL_map(sequence:list, mapping) -> list:
    return [mapping(elem) for elem in sequence]

async def BAL_reduce(sequence:list, reduce_fn, aggregator) -> any:
    for elem in sequence:
        aggregator = reduce_fn(aggregator, elem)
    return aggregator


############################################
#
#   Task functions
#
############################################

@app.get("/task/", response_model=None, tags=["Task"])
def get_all_task(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(Task)
        query = query.options(joinedload(Task.contains))
        task_list = query.all()

        # Serialize with relationships included
        result = []
        for task_item in task_list:
            item_dict = task_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if task_item.contains:
                related_obj = task_item.contains
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['contains'] = related_dict
            else:
                item_dict['contains'] = None


            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(Task).all()


@app.get("/task/count/", response_model=None, tags=["Task"])
def get_count_task(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Task entities"""
    count = database.query(Task).count()
    return {"count": count}


@app.get("/task/paginated/", response_model=None, tags=["Task"])
def get_paginated_task(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Task entities"""
    total = database.query(Task).count()
    task_list = database.query(Task).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": task_list
    }


@app.get("/task/search/", response_model=None, tags=["Task"])
def search_task(
    database: Session = Depends(get_db)
) -> list:
    """Search Task entities by attributes"""
    query = database.query(Task)


    results = query.all()
    return results


@app.get("/task/{task_id}/", response_model=None, tags=["Task"])
async def get_task(task_id: int, database: Session = Depends(get_db)) -> Task:
    db_task = database.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    response_data = {
        "task": db_task,
}
    return response_data



@app.post("/task/", response_model=None, tags=["Task"])
async def create_task(task_data: TaskCreate, database: Session = Depends(get_db)) -> Task:

    if task_data.contains is not None:
        db_contains = database.query(ToDoList).filter(ToDoList.id == task_data.contains).first()
        if not db_contains:
            raise HTTPException(status_code=400, detail="ToDoList not found")
    else:
        raise HTTPException(status_code=400, detail="ToDoList ID is required")

    db_task = Task(
        updatedAt=task_data.updatedAt,        description=task_data.description,        status=task_data.status.value,        priority=task_data.priority.value,        title=task_data.title,        taskId=task_data.taskId,        dueDate=task_data.dueDate,        createdAt=task_data.createdAt,        contains_id=task_data.contains        )

    database.add(db_task)
    database.commit()
    database.refresh(db_task)




    return db_task


@app.post("/task/bulk/", response_model=None, tags=["Task"])
async def bulk_create_task(items: list[TaskCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Task entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item
            if not item_data.contains:
                raise ValueError("ToDoList ID is required")

            db_task = Task(
                updatedAt=item_data.updatedAt,                description=item_data.description,                status=item_data.status.value,                priority=item_data.priority.value,                title=item_data.title,                taskId=item_data.taskId,                dueDate=item_data.dueDate,                createdAt=item_data.createdAt,                contains_id=item_data.contains            )
            database.add(db_task)
            database.flush()  # Get ID without committing
            created_items.append(db_task.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Task entities"
    }


@app.delete("/task/bulk/", response_model=None, tags=["Task"])
async def bulk_delete_task(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Task entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_task = database.query(Task).filter(Task.id == item_id).first()
        if db_task:
            database.delete(db_task)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Task entities"
    }

@app.put("/task/{task_id}/", response_model=None, tags=["Task"])
async def update_task(task_id: int, task_data: TaskCreate, database: Session = Depends(get_db)) -> Task:
    db_task = database.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    setattr(db_task, 'updatedAt', task_data.updatedAt)
    setattr(db_task, 'description', task_data.description)
    setattr(db_task, 'status', task_data.status.value)
    setattr(db_task, 'priority', task_data.priority.value)
    setattr(db_task, 'title', task_data.title)
    setattr(db_task, 'taskId', task_data.taskId)
    setattr(db_task, 'dueDate', task_data.dueDate)
    setattr(db_task, 'createdAt', task_data.createdAt)
    if task_data.contains is not None:
        db_contains = database.query(ToDoList).filter(ToDoList.id == task_data.contains).first()
        if not db_contains:
            raise HTTPException(status_code=400, detail="ToDoList not found")
        setattr(db_task, 'contains_id', task_data.contains)
    database.commit()
    database.refresh(db_task)

    return db_task


@app.delete("/task/{task_id}/", response_model=None, tags=["Task"])
async def delete_task(task_id: int, database: Session = Depends(get_db)):
    db_task = database.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    database.delete(db_task)
    database.commit()
    return db_task



############################################
#   Task Method Endpoints
############################################




@app.post("/task/{task_id}/methods/markComplete/", response_model=None, tags=["Task Methods"])
async def execute_task_markComplete(
    task_id: int,
    params: dict = Body(default=None, embed=True),
    database: Session = Depends(get_db)
):
    """
    Execute the markComplete method on a Task instance.
    """
    # Retrieve the entity from the database
    _task_object = database.query(Task).filter(Task.id == task_id).first()
    if _task_object is None:
        raise HTTPException(status_code=404, detail="Task not found")

    # Prepare method parameters

    # Execute the method
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        async def wrapper(_task_object):
            _task_object.status = TaskStatus.COMPLETED
            _task_object.updatedAt = datetime.now()  # assuming datetime is imported
            

        result = await wrapper(_task_object)
        # Commit DB
        database.commit()
        database.refresh(_task_object)

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        return {
            "task_id": task_id,
            "method": "markComplete",
            "status": "executed",
            "result": str(result) if result is not None else None,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")



############################################
#
#   ToDoList functions
#
############################################

@app.get("/todolist/", response_model=None, tags=["ToDoList"])
def get_all_todolist(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(ToDoList)
        query = query.options(joinedload(ToDoList.user))
        todolist_list = query.all()

        # Serialize with relationships included
        result = []
        for todolist_item in todolist_list:
            item_dict = todolist_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if todolist_item.user:
                related_obj = todolist_item.user
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['user'] = related_dict
            else:
                item_dict['user'] = None

            # Add many-to-many and one-to-many relationship objects (full details)
            task_list = database.query(Task).filter(Task.contains_id == todolist_item.id).all()
            item_dict['task'] = []
            for task_obj in task_list:
                task_dict = task_obj.__dict__.copy()
                task_dict.pop('_sa_instance_state', None)
                item_dict['task'].append(task_dict)

            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(ToDoList).all()


@app.get("/todolist/count/", response_model=None, tags=["ToDoList"])
def get_count_todolist(database: Session = Depends(get_db)) -> dict:
    """Get the total count of ToDoList entities"""
    count = database.query(ToDoList).count()
    return {"count": count}


@app.get("/todolist/paginated/", response_model=None, tags=["ToDoList"])
def get_paginated_todolist(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of ToDoList entities"""
    total = database.query(ToDoList).count()
    todolist_list = database.query(ToDoList).offset(skip).limit(limit).all()
    # By default, return flat entities (for charts/widgets)
    # Use detailed=true to get entities with relationships
    if not detailed:
        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "data": todolist_list
        }

    result = []
    for todolist_item in todolist_list:
        task_ids = database.query(Task.id).filter(Task.contains_id == todolist_item.id).all()
        item_data = {
            "todolist": todolist_item,
            "task_ids": [x[0] for x in task_ids]        }
        result.append(item_data)
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": result
    }


@app.get("/todolist/search/", response_model=None, tags=["ToDoList"])
def search_todolist(
    database: Session = Depends(get_db)
) -> list:
    """Search ToDoList entities by attributes"""
    query = database.query(ToDoList)


    results = query.all()
    return results


@app.get("/todolist/{todolist_id}/", response_model=None, tags=["ToDoList"])
async def get_todolist(todolist_id: int, database: Session = Depends(get_db)) -> ToDoList:
    db_todolist = database.query(ToDoList).filter(ToDoList.id == todolist_id).first()
    if db_todolist is None:
        raise HTTPException(status_code=404, detail="ToDoList not found")

    task_ids = database.query(Task.id).filter(Task.contains_id == db_todolist.id).all()
    response_data = {
        "todolist": db_todolist,
        "task_ids": [x[0] for x in task_ids]}
    return response_data



@app.post("/todolist/", response_model=None, tags=["ToDoList"])
async def create_todolist(todolist_data: ToDoListCreate, database: Session = Depends(get_db)) -> ToDoList:

    if todolist_data.user is not None:
        db_user = database.query(User).filter(User.id == todolist_data.user).first()
        if not db_user:
            raise HTTPException(status_code=400, detail="User not found")
    else:
        raise HTTPException(status_code=400, detail="User ID is required")

    db_todolist = ToDoList(
        listId=todolist_data.listId,        description=todolist_data.description,        title=todolist_data.title,        updatedAt=todolist_data.updatedAt,        createdAt=todolist_data.createdAt,        user_id=todolist_data.user        )

    database.add(db_todolist)
    database.commit()
    database.refresh(db_todolist)

    if todolist_data.task:
        # Validate that all Task IDs exist
        for task_id in todolist_data.task:
            db_task = database.query(Task).filter(Task.id == task_id).first()
            if not db_task:
                raise HTTPException(status_code=400, detail=f"Task with id {task_id} not found")

        # Update the related entities with the new foreign key
        database.query(Task).filter(Task.id.in_(todolist_data.task)).update(
            {Task.contains_id: db_todolist.id}, synchronize_session=False
        )
        database.commit()



    task_ids = database.query(Task.id).filter(Task.contains_id == db_todolist.id).all()
    response_data = {
        "todolist": db_todolist,
        "task_ids": [x[0] for x in task_ids]    }
    return response_data


@app.post("/todolist/bulk/", response_model=None, tags=["ToDoList"])
async def bulk_create_todolist(items: list[ToDoListCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple ToDoList entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item
            if not item_data.user:
                raise ValueError("User ID is required")

            db_todolist = ToDoList(
                listId=item_data.listId,                description=item_data.description,                title=item_data.title,                updatedAt=item_data.updatedAt,                createdAt=item_data.createdAt,                user_id=item_data.user            )
            database.add(db_todolist)
            database.flush()  # Get ID without committing
            created_items.append(db_todolist.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} ToDoList entities"
    }


@app.delete("/todolist/bulk/", response_model=None, tags=["ToDoList"])
async def bulk_delete_todolist(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple ToDoList entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_todolist = database.query(ToDoList).filter(ToDoList.id == item_id).first()
        if db_todolist:
            database.delete(db_todolist)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} ToDoList entities"
    }

@app.put("/todolist/{todolist_id}/", response_model=None, tags=["ToDoList"])
async def update_todolist(todolist_id: int, todolist_data: ToDoListCreate, database: Session = Depends(get_db)) -> ToDoList:
    db_todolist = database.query(ToDoList).filter(ToDoList.id == todolist_id).first()
    if db_todolist is None:
        raise HTTPException(status_code=404, detail="ToDoList not found")

    setattr(db_todolist, 'listId', todolist_data.listId)
    setattr(db_todolist, 'description', todolist_data.description)
    setattr(db_todolist, 'title', todolist_data.title)
    setattr(db_todolist, 'updatedAt', todolist_data.updatedAt)
    setattr(db_todolist, 'createdAt', todolist_data.createdAt)
    if todolist_data.user is not None:
        db_user = database.query(User).filter(User.id == todolist_data.user).first()
        if not db_user:
            raise HTTPException(status_code=400, detail="User not found")
        setattr(db_todolist, 'user_id', todolist_data.user)
    if todolist_data.task is not None:
        # Clear all existing relationships (set foreign key to NULL)
        database.query(Task).filter(Task.contains_id == db_todolist.id).update(
            {Task.contains_id: None}, synchronize_session=False
        )

        # Set new relationships if list is not empty
        if todolist_data.task:
            # Validate that all IDs exist
            for task_id in todolist_data.task:
                db_task = database.query(Task).filter(Task.id == task_id).first()
                if not db_task:
                    raise HTTPException(status_code=400, detail=f"Task with id {task_id} not found")

            # Update the related entities with the new foreign key
            database.query(Task).filter(Task.id.in_(todolist_data.task)).update(
                {Task.contains_id: db_todolist.id}, synchronize_session=False
            )
    database.commit()
    database.refresh(db_todolist)

    task_ids = database.query(Task.id).filter(Task.contains_id == db_todolist.id).all()
    response_data = {
        "todolist": db_todolist,
        "task_ids": [x[0] for x in task_ids]    }
    return response_data


@app.delete("/todolist/{todolist_id}/", response_model=None, tags=["ToDoList"])
async def delete_todolist(todolist_id: int, database: Session = Depends(get_db)):
    db_todolist = database.query(ToDoList).filter(ToDoList.id == todolist_id).first()
    if db_todolist is None:
        raise HTTPException(status_code=404, detail="ToDoList not found")
    database.delete(db_todolist)
    database.commit()
    return db_todolist



############################################
#   ToDoList Method Endpoints
############################################




@app.post("/todolist/{todolist_id}/methods/goToTask/", response_model=None, tags=["ToDoList Methods"])
async def execute_todolist_goToTask(
    todolist_id: int,
    params: dict = Body(default=None, embed=True),
    database: Session = Depends(get_db)
):
    """
    Execute the goToTask method on a ToDoList instance.

    Parameters:
    - taskId: str    """
    # Retrieve the entity from the database
    _todolist_object = database.query(ToDoList).filter(ToDoList.id == todolist_id).first()
    if _todolist_object is None:
        raise HTTPException(status_code=404, detail="ToDoList not found")

    # Prepare method parameters
    taskId = params.get('taskId')

    # Execute the method
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        async def wrapper(_todolist_object):
            # Logic to navigate to Task detail page in GUI
            print(f"Navigating to Task with id: {taskId}")
            

        result = await wrapper(_todolist_object)
        # Commit DB
        database.commit()
        database.refresh(_todolist_object)

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        return {
            "todolist_id": todolist_id,
            "method": "goToTask",
            "status": "executed",
            "result": str(result) if result is not None else None,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")





@app.post("/todolist/{todolist_id}/methods/addTask/", response_model=None, tags=["ToDoList Methods"])
async def execute_todolist_addTask(
    todolist_id: int,
    params: dict = Body(default=None, embed=True),
    database: Session = Depends(get_db)
):
    """
    Execute the addTask method on a ToDoList instance.

    Parameters:
    - task: Task    """
    # Retrieve the entity from the database
    _todolist_object = database.query(ToDoList).filter(ToDoList.id == todolist_id).first()
    if _todolist_object is None:
        raise HTTPException(status_code=404, detail="ToDoList not found")

    # Prepare method parameters
    task = await get_task(params.get('task'), database)

    # Execute the method
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        async def wrapper(_todolist_object):
            # Add task to the ToDoList
            _todolist_object.tasks.append(task)
            _todolist_object.updatedAt = datetime.now()  # assuming datetime is imported
            

        result = await wrapper(_todolist_object)
        # Commit DB
        database.commit()
        database.refresh(_todolist_object)

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        return {
            "todolist_id": todolist_id,
            "method": "addTask",
            "status": "executed",
            "result": str(result) if result is not None else None,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")



############################################
#
#   User functions
#
############################################

@app.get("/user/", response_model=None, tags=["User"])
def get_all_user(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(User)
        user_list = query.all()

        # Serialize with relationships included
        result = []
        for user_item in user_list:
            item_dict = user_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)

            # Add many-to-many and one-to-many relationship objects (full details)
            todolist_list = database.query(ToDoList).filter(ToDoList.user_id == user_item.id).all()
            item_dict['owns'] = []
            for todolist_obj in todolist_list:
                todolist_dict = todolist_obj.__dict__.copy()
                todolist_dict.pop('_sa_instance_state', None)
                item_dict['owns'].append(todolist_dict)

            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(User).all()


@app.get("/user/count/", response_model=None, tags=["User"])
def get_count_user(database: Session = Depends(get_db)) -> dict:
    """Get the total count of User entities"""
    count = database.query(User).count()
    return {"count": count}


@app.get("/user/paginated/", response_model=None, tags=["User"])
def get_paginated_user(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of User entities"""
    total = database.query(User).count()
    user_list = database.query(User).offset(skip).limit(limit).all()
    # By default, return flat entities (for charts/widgets)
    # Use detailed=true to get entities with relationships
    if not detailed:
        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "data": user_list
        }

    result = []
    for user_item in user_list:
        owns_ids = database.query(ToDoList.id).filter(ToDoList.user_id == user_item.id).all()
        item_data = {
            "user": user_item,
            "owns_ids": [x[0] for x in owns_ids]        }
        result.append(item_data)
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": result
    }


@app.get("/user/search/", response_model=None, tags=["User"])
def search_user(
    database: Session = Depends(get_db)
) -> list:
    """Search User entities by attributes"""
    query = database.query(User)


    results = query.all()
    return results


@app.get("/user/{user_id}/", response_model=None, tags=["User"])
async def get_user(user_id: int, database: Session = Depends(get_db)) -> User:
    db_user = database.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    owns_ids = database.query(ToDoList.id).filter(ToDoList.user_id == db_user.id).all()
    response_data = {
        "user": db_user,
        "owns_ids": [x[0] for x in owns_ids]}
    return response_data



@app.post("/user/", response_model=None, tags=["User"])
async def create_user(user_data: UserCreate, database: Session = Depends(get_db)) -> User:


    db_user = User(
        email=user_data.email,        username=user_data.username,        userId=user_data.userId,        passwordHash=user_data.passwordHash,        createdAt=user_data.createdAt        )

    database.add(db_user)
    database.commit()
    database.refresh(db_user)

    if user_data.owns:
        # Validate that all ToDoList IDs exist
        for todolist_id in user_data.owns:
            db_todolist = database.query(ToDoList).filter(ToDoList.id == todolist_id).first()
            if not db_todolist:
                raise HTTPException(status_code=400, detail=f"ToDoList with id {todolist_id} not found")

        # Update the related entities with the new foreign key
        database.query(ToDoList).filter(ToDoList.id.in_(user_data.owns)).update(
            {ToDoList.user_id: db_user.id}, synchronize_session=False
        )
        database.commit()



    owns_ids = database.query(ToDoList.id).filter(ToDoList.user_id == db_user.id).all()
    response_data = {
        "user": db_user,
        "owns_ids": [x[0] for x in owns_ids]    }
    return response_data


@app.post("/user/bulk/", response_model=None, tags=["User"])
async def bulk_create_user(items: list[UserCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple User entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item

            db_user = User(
                email=item_data.email,                username=item_data.username,                userId=item_data.userId,                passwordHash=item_data.passwordHash,                createdAt=item_data.createdAt            )
            database.add(db_user)
            database.flush()  # Get ID without committing
            created_items.append(db_user.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} User entities"
    }


@app.delete("/user/bulk/", response_model=None, tags=["User"])
async def bulk_delete_user(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple User entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_user = database.query(User).filter(User.id == item_id).first()
        if db_user:
            database.delete(db_user)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} User entities"
    }

@app.put("/user/{user_id}/", response_model=None, tags=["User"])
async def update_user(user_id: int, user_data: UserCreate, database: Session = Depends(get_db)) -> User:
    db_user = database.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    setattr(db_user, 'email', user_data.email)
    setattr(db_user, 'username', user_data.username)
    setattr(db_user, 'userId', user_data.userId)
    setattr(db_user, 'passwordHash', user_data.passwordHash)
    setattr(db_user, 'createdAt', user_data.createdAt)
    if user_data.owns is not None:
        # Clear all existing relationships (set foreign key to NULL)
        database.query(ToDoList).filter(ToDoList.user_id == db_user.id).update(
            {ToDoList.user_id: None}, synchronize_session=False
        )

        # Set new relationships if list is not empty
        if user_data.owns:
            # Validate that all IDs exist
            for todolist_id in user_data.owns:
                db_todolist = database.query(ToDoList).filter(ToDoList.id == todolist_id).first()
                if not db_todolist:
                    raise HTTPException(status_code=400, detail=f"ToDoList with id {todolist_id} not found")

            # Update the related entities with the new foreign key
            database.query(ToDoList).filter(ToDoList.id.in_(user_data.owns)).update(
                {ToDoList.user_id: db_user.id}, synchronize_session=False
            )
    database.commit()
    database.refresh(db_user)

    owns_ids = database.query(ToDoList.id).filter(ToDoList.user_id == db_user.id).all()
    response_data = {
        "user": db_user,
        "owns_ids": [x[0] for x in owns_ids]    }
    return response_data


@app.delete("/user/{user_id}/", response_model=None, tags=["User"])
async def delete_user(user_id: int, database: Session = Depends(get_db)):
    db_user = database.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    database.delete(db_user)
    database.commit()
    return db_user



############################################
#   User Method Endpoints
############################################




@app.post("/user/{user_id}/methods/authenticate/", response_model=None, tags=["User Methods"])
async def execute_user_authenticate(
    user_id: int,
    params: dict = Body(default=None, embed=True),
    database: Session = Depends(get_db)
):
    """
    Execute the authenticate method on a User instance.

    Parameters:
    - password: str    """
    # Retrieve the entity from the database
    _user_object = database.query(User).filter(User.id == user_id).first()
    if _user_object is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Prepare method parameters
    password = params.get('password')

    # Execute the method
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        async def wrapper(_user_object):
            # Implement password verification logic here
            # For example, compare hashed password
            return verify_password_hash(password, _user_object.passwordHash)  # assuming verify_password_hash is defined elsewhere
            

        result = await wrapper(_user_object)
        # Commit DB
        database.commit()
        database.refresh(_user_object)

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        return {
            "user_id": user_id,
            "method": "authenticate",
            "status": "executed",
            "result": str(result) if result is not None else None,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")





@app.post("/user/{user_id}/methods/goToToDoList/", response_model=None, tags=["User Methods"])
async def execute_user_goToToDoList(
    user_id: int,
    params: dict = Body(default=None, embed=True),
    database: Session = Depends(get_db)
):
    """
    Execute the goToToDoList method on a User instance.

    Parameters:
    - listId: str    """
    # Retrieve the entity from the database
    _user_object = database.query(User).filter(User.id == user_id).first()
    if _user_object is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Prepare method parameters
    listId = params.get('listId')

    # Execute the method
    try:
        # Capture stdout to include print outputs in the response
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        async def wrapper(_user_object):
            # Logic to navigate to ToDoList page in GUI
            print(f"Navigating to ToDoList with id: {listId}")
            

        result = await wrapper(_user_object)
        # Commit DB
        database.commit()
        database.refresh(_user_object)

        # Restore stdout
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        return {
            "user_id": user_id,
            "method": "goToToDoList",
            "status": "executed",
            "result": str(result) if result is not None else None,
            "output": output if output else None
        }
    except Exception as e:
        sys.stdout = sys.__stdout__
        raise HTTPException(status_code=500, detail=f"Method execution failed: {str(e)}")





############################################
# Maintaining the server
############################################
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



