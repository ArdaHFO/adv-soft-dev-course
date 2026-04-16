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


###############
#  GUI MODEL  #
###############

from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen,
    ViewComponent, ViewContainer,
    Button, ButtonType, ButtonActionType,
    Text, Image, Link, InputField, InputFieldType,
    Form, Menu, MenuItem, DataList,
    DataSource, DataSourceElement, EmbeddedContent,
    Styling, Size, Position, Color, Layout, LayoutType,
    UnitSize, PositionType, Alignment
)
from besser.BUML.metamodel.gui.dashboard import (
    LineChart, BarChart, PieChart, RadarChart, RadialBarChart, Table, AgentComponent,
    Column, FieldColumn, LookupColumn, ExpressionColumn, MetricCard, Series
)
from besser.BUML.metamodel.gui.events_actions import (
    Event, EventType, Transition, Create, Read, Update, Delete, Parameter
)
from besser.BUML.metamodel.gui.binding import DataBinding

# Module: GUI_Module

# Screen: i9fzj
i9fzj = Screen(name="i9fzj", description="ToDoList Detail", view_elements=set(), route_path="/todolist-detail", screen_size="Medium")
i9fzj_styling_size = Size(font_family="\'Inter\', \'Segoe UI\', system-ui, -apple-system, sans-serif", min_height="100vh")
i9fzj_styling_pos = Position()
i9fzj_styling_color = Color(background_color="#f8fafc", text_color="#1e293b", color_palette="default")
i9fzj_styling = Styling(size=i9fzj_styling_size, position=i9fzj_styling_pos, color=i9fzj_styling_color)
i9fzj.styling = i9fzj_styling
i9fzj.component_id = "GjDawjQkKgmDfrtEdh"
ibb9n = Text(
    name="ibb9n",
    content="ToDoList App",
    description="Text element",
    styling=Styling(size=Size(font_size="1.25rem", font_weight="700", letter_spacing="-0.01em"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="ibb9n",
    display_order=0,
    custom_attributes={"id": "ibb9n"}
)
iyx6g = Link(
    name="iyx6g",
    description="Link element",
    label="Home",
    url="/home",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="500", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="transparent", text_color="#64748b", color_palette="default", border_radius="8px")),
    component_id="iyx6g",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/home", "data-navigate-to": "home", "id": "iyx6g"}
)
i486d = Link(
    name="i486d",
    description="Link element",
    label="Dashboard",
    url="/dashboard",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="500", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="transparent", text_color="#64748b", color_palette="default", border_radius="8px")),
    component_id="i486d",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/dashboard", "data-navigate-to": "dashboard", "id": "i486d"}
)
ikoe7 = Link(
    name="ikoe7",
    description="Link element",
    label="ToDoList Detail",
    url="/todolist-detail",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="600", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="#eff6ff", text_color="#2563eb", color_palette="default", border_radius="8px")),
    component_id="ikoe7",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/todolist-detail", "data-navigate-to": "todolist-detail", "id": "ikoe7"}
)
i54lf = Link(
    name="i54lf",
    description="Link element",
    label="User Profile",
    url="/user-profile",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="500", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="transparent", text_color="#64748b", color_palette="default", border_radius="8px")),
    component_id="i54lf",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/user-profile", "data-navigate-to": "user-profile", "id": "i54lf"}
)
ikw5o = ViewContainer(
    name="ikw5o",
    description=" component",
    view_elements={iyx6g, i486d, ikoe7, i54lf},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center", gap="4px")),
    component_id="ikw5o",
    display_order=1,
    custom_attributes={"id": "ikw5o"}
)
ikw5o_layout = Layout(layout_type=LayoutType.FLEX, align_items="center", gap="4px")
ikw5o.layout = ikw5o_layout
irooz = ViewContainer(
    name="irooz",
    description="nav container",
    view_elements={ibb9n, ikw5o},
    styling=Styling(size=Size(height="64px", padding="0 32px", font_family="\'Inter\', \'Segoe UI\', system-ui, -apple-system, sans-serif"), position=Position(p_type=PositionType.STICKY, top="0", z_index=50, display="flex"), color=Color(background_color="#ffffff", color_palette="default", border_bottom="1px solid #e2e8f0", box_shadow="0 1px 3px rgba(0,0,0,0.06)"), layout=Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")),
    component_id="irooz",
    tag_name="nav",
    display_order=0,
    css_classes=["assistant-nav-header"],
    custom_attributes={"id": "irooz"}
)
irooz_layout = Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")
irooz.layout = irooz_layout
iwgsv = Text(
    name="iwgsv",
    content="Work Projects",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 12px 0", font_size="1.35rem", font_weight="700"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="iwgsv",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "iwgsv"}
)
ig5ph = Text(
    name="ig5ph",
    content="Tasks related to ongoing work projects. Manage your tasks below.",
    description="Text element",
    styling=Styling(size=Size(margin="0", line_height="1.6"), color=Color(text_color="#475569", color_palette="default")),
    component_id="ig5ph",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "ig5ph"}
)
i7izo = ViewContainer(
    name="i7izo",
    description="section container",
    view_elements={iwgsv, ig5ph},
    styling=Styling(size=Size(padding="32px", margin="12px 24px"), color=Color(background_color="#ffffff", color_palette="default", border_radius="14px", border="1px solid #f1f5f9", box_shadow="0 1px 4px rgba(0,0,0,0.06)")),
    component_id="i7izo",
    tag_name="section",
    display_order=0,
    css_classes=["assistant-content"],
    custom_attributes={"id": "i7izo"}
)
i1ft3v = Text(
    name="i1ft3v",
    content="Tasks and Status",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 8px 0", font_size="1.35rem", font_weight="700"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="i1ft3v",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "i1ft3v"}
)
iai5of = Text(
    name="iai5of",
    content="Tasks in List",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 16px 0", font_size="1.25rem", font_weight="700"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="iai5of",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "iai5of"}
)
i8kwjh_col_0 = FieldColumn(label="Taskid", field=Task_taskId)
i8kwjh_col_1 = FieldColumn(label="Title", field=Task_title)
i8kwjh_col_2 = FieldColumn(label="Description", field=Task_description)
i8kwjh_col_3 = FieldColumn(label="Duedate", field=Task_dueDate)
i8kwjh_col_4 = FieldColumn(label="Priority", field=Task_priority)
i8kwjh_col_5 = FieldColumn(label="Status", field=Task_status)
i8kwjh_col_6 = FieldColumn(label="Createdat", field=Task_createdAt)
i8kwjh_col_7 = FieldColumn(label="Updatedat", field=Task_updatedAt)
i8kwjh = Table(
    name="i8kwjh",
    title="Tasks in List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[i8kwjh_col_0, i8kwjh_col_1, i8kwjh_col_2, i8kwjh_col_3, i8kwjh_col_4, i8kwjh_col_5, i8kwjh_col_6, i8kwjh_col_7],
    styling=Styling(size=Size(width="100%", margin="12px 0", min_height="300px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50", border_radius="12px")),
    component_id="i8kwjh",
    display_order=1,
    css_classes=["table-component"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Tasks in List", "data-source": "class_v10e1nt5o_mo156c3g_432", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": "[{\"field\": \"taskId\", \"label\": \"Taskid\", \"columnType\": \"field\", \"_expanded\": false}, {\"field\": \"title\", \"label\": \"Title\", \"columnType\": \"field\", \"_expanded\": false}, {\"field\": \"description\", \"label\": \"Description\", \"columnType\": \"field\", \"_expanded\": false}, {\"field\": \"dueDate\", \"label\": \"Duedate\", \"columnType\": \"field\", \"_expanded\": false}, {\"field\": \"priority\", \"label\": \"Priority\", \"columnType\": \"field\", \"_expanded\": false}, {\"field\": \"status\", \"label\": \"Status\", \"columnType\": \"field\", \"_expanded\": false}, {\"field\": \"createdAt\", \"label\": \"Createdat\", \"columnType\": \"field\", \"_expanded\": false}, {\"field\": \"updatedAt\", \"label\": \"Updatedat\", \"columnType\": \"field\", \"_expanded\": false}, {\"field\": \"ToDoList\", \"label\": \"Todolist\", \"columnType\": \"lookup\", \"lookupEntity\": \"class_cvm5nzqm6_mo156c3f_sfx\", \"lookupField\": \"listId\", \"_expanded\": false}]", "id": "i8kwjh"}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
i8kwjh_binding_domain = None
if domain_model_ref is not None:
    i8kwjh_binding_domain = domain_model_ref.get_class_by_name("Task")
if i8kwjh_binding_domain:
    i8kwjh_binding = DataBinding(domain_concept=i8kwjh_binding_domain, name="TaskDataBinding")
else:
    # Domain class 'Task' not resolved; data binding skipped.
    i8kwjh_binding = None
if i8kwjh_binding:
    i8kwjh.data_binding = i8kwjh_binding
iix4xi = ViewContainer(
    name="iix4xi",
    description="section container",
    view_elements={iai5of, i8kwjh},
    styling=Styling(size=Size(padding="28px", margin="0"), color=Color(background_color="#ffffff", color_palette="default", border_radius="14px", border="1px solid #f1f5f9", box_shadow="0 1px 4px rgba(0,0,0,0.06)")),
    component_id="iix4xi",
    tag_name="section",
    display_order=1,
    css_classes=["assistant-card"],
    custom_attributes={"id": "iix4xi"}
)
iwc1jk = Text(
    name="iwc1jk",
    content="Task Priority Distribution",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 16px 0", font_size="1.25rem", font_weight="700"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="iwc1jk",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "iwc1jk"}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
i5453j_series_0_binding_domain = None
if domain_model_ref is not None:
    i5453j_series_0_binding_domain = domain_model_ref.get_class_by_name("Task")
if i5453j_series_0_binding_domain:
    i5453j_series_0_binding = DataBinding(domain_concept=i5453j_series_0_binding_domain, name="TaskDataBinding")
else:
    # Domain class 'Task' not resolved; data binding skipped.
    i5453j_series_0_binding = None
i5453j_series_0 = Series(name="Task", label="Task", data_binding=i5453j_series_0_binding, styling=None)
i5453j = PieChart(
    name="i5453j",
    series=[i5453j_series_0],
    title="Task Priority Distribution",
    show_legend=True,
    legend_position=Alignment.BOTTOM,
    show_labels=True,
    label_position=Alignment.INSIDE,
    padding_angle=0,
    inner_radius=0,
    outer_radius=80,
    start_angle=0,
    end_angle=360,
    styling=Styling(size=Size(width="100%", margin="12px 0", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", border_radius="12px")),
    component_id="i5453j",
    display_order=1,
    css_classes=["pie-chart-component"],
    custom_attributes={"chart-title": "Task Priority Distribution", "show-legend": "true", "legend-position": "bottom", "show-labels": "true", "label-position": "inside", "padding-angle": "0", "series": "[{\"name\": \"Task\", \"data-source\": \"class_v10e1nt5o_mo156c3g_432\", \"color\": \"#00C49F\", \"data\": [{\"name\": \"High\", \"value\": 2, \"color\": \"#EF4444\"}, {\"name\": \"Medium\", \"value\": 1, \"color\": \"#F59E0B\"}, {\"name\": \"Low\", \"value\": 1, \"color\": \"#22C55E\"}]}]", "show-grid": "true", "data-source": "class_v10e1nt5o_mo156c3g_432", "label-field": "attr_tc4t48klu_mo156c3g_cvq", "data-field": "attr_tc4t48klu_mo156c3g_cvq", "id": "i5453j"}
)
i3jd8l = ViewContainer(
    name="i3jd8l",
    description="section container",
    view_elements={iwc1jk, i5453j},
    styling=Styling(size=Size(padding="28px", margin="0"), color=Color(background_color="#ffffff", color_palette="default", border_radius="14px", border="1px solid #f1f5f9", box_shadow="0 1px 4px rgba(0,0,0,0.06)")),
    component_id="i3jd8l",
    tag_name="section",
    display_order=2,
    css_classes=["assistant-card"],
    custom_attributes={"id": "i3jd8l"}
)
iv2sze = ViewContainer(
    name="iv2sze",
    description="section container",
    view_elements={i1ft3v, iix4xi, i3jd8l},
    styling=Styling(size=Size(margin="12px 24px"), position=Position(display="grid"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.GRID, grid_template_columns="1fr 1fr", gap="20px")),
    component_id="iv2sze",
    tag_name="section",
    display_order=1,
    css_classes=["assistant-two-column"],
    custom_attributes={"id": "iv2sze"}
)
iv2sze_layout = Layout(layout_type=LayoutType.GRID, grid_template_columns="1fr 1fr", gap="20px")
iv2sze.layout = iv2sze_layout
i86yvj = Text(
    name="i86yvj",
    content="Add New Task",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 20px 0", font_size="1.35rem", font_weight="700"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="i86yvj",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "i86yvj"}
)
i2w6jw = InputField(
    name="i2w6jw",
    description="Text input",
    field_type=InputFieldType.Text,
    styling=Styling(size=Size(padding="12px 14px", font_size="0.95rem"), color=Color(background_color="#f8fafc", color_palette="default", border_radius="10px", border="1px solid #e2e8f0")),
    component_id="i2w6jw",
    tag_name="input",
    display_order=0,
    custom_attributes={"type": "text", "name": "title", "placeholder": "title", "id": "i2w6jw"}
)
i471qn = InputField(
    name="i471qn",
    description="Text input",
    field_type=InputFieldType.Text,
    styling=Styling(size=Size(padding="12px 14px", font_size="0.95rem"), color=Color(background_color="#f8fafc", color_palette="default", border_radius="10px", border="1px solid #e2e8f0")),
    component_id="i471qn",
    tag_name="input",
    display_order=4,
    custom_attributes={"type": "text", "name": "status", "placeholder": "status", "id": "i471qn"}
)
idpiwg = InputField(
    name="idpiwg",
    description="Text input",
    field_type=InputFieldType.Text,
    styling=Styling(size=Size(padding="12px 14px", font_size="0.95rem"), color=Color(background_color="#f8fafc", color_palette="default", border_radius="10px", border="1px solid #e2e8f0")),
    component_id="idpiwg",
    tag_name="input",
    display_order=2,
    custom_attributes={"type": "text", "name": "duedate", "placeholder": "dueDate", "id": "idpiwg"}
)
i0z3e1 = InputField(
    name="i0z3e1",
    description="Text input",
    field_type=InputFieldType.Text,
    styling=Styling(size=Size(padding="12px 14px", font_size="0.95rem"), color=Color(background_color="#f8fafc", color_palette="default", border_radius="10px", border="1px solid #e2e8f0")),
    component_id="i0z3e1",
    tag_name="input",
    display_order=3,
    custom_attributes={"type": "text", "name": "priority", "placeholder": "priority", "id": "i0z3e1"}
)
i54sfh = InputField(
    name="i54sfh",
    description="Text input",
    field_type=InputFieldType.Text,
    styling=Styling(size=Size(padding="12px 14px", font_size="0.95rem"), color=Color(background_color="#f8fafc", color_palette="default", border_radius="10px", border="1px solid #e2e8f0")),
    component_id="i54sfh",
    tag_name="input",
    display_order=1,
    custom_attributes={"type": "text", "name": "description", "placeholder": "description", "id": "i54sfh"}
)
form = Form(
    name="form",
    description="Form component",
    inputFields={i2w6jw, i471qn, idpiwg, i0z3e1, i54sfh},
    tag_name="form",
    display_order=1
)
iqugvf = ViewContainer(
    name="iqugvf",
    description="section container",
    view_elements={i86yvj, form},
    styling=Styling(size=Size(padding="32px", margin="12px 24px"), color=Color(background_color="#ffffff", color_palette="default", border_radius="14px", border="1px solid #f1f5f9", box_shadow="0 1px 4px rgba(0,0,0,0.06)")),
    component_id="iqugvf",
    tag_name="section",
    display_order=2,
    css_classes=["assistant-form"],
    custom_attributes={"id": "iqugvf"}
)
ij4xh = ViewContainer(
    name="ij4xh",
    description="main container",
    view_elements={i7izo, iv2sze, iqugvf},
    styling=Styling(size=Size(padding="24px 16px", margin="0 auto", max_width="1200px"), color=Color(color_palette="default")),
    component_id="ij4xh",
    tag_name="main",
    display_order=1,
    css_classes=["assistant-main"],
    custom_attributes={"id": "ij4xh"}
)
imu91j = ViewComponent(name="imu91j", description=" component")
i7rrlj = ViewComponent(name="i7rrlj", description=" component")
component_3 = ViewContainer(
    name="Component_3",
    description=" component",
    view_elements={imu91j, i7rrlj},
    display_order=0
)
ihdcrl = Link(
    name="ihdcrl",
    description="Link element",
    label="Privacy",
    url="#",
    styling=Styling(size=Size(font_size="0.85rem", text_decoration="none"), position=Position(transition="color 0.2s"), color=Color(text_color="#94a3b8", color_palette="default")),
    component_id="ihdcrl",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "#", "id": "ihdcrl"}
)
iqpp08 = Link(
    name="iqpp08",
    description="Link element",
    label="Terms",
    url="#",
    styling=Styling(size=Size(font_size="0.85rem", text_decoration="none"), position=Position(transition="color 0.2s"), color=Color(text_color="#94a3b8", color_palette="default")),
    component_id="iqpp08",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "#", "id": "iqpp08"}
)
i8yflw = Link(
    name="i8yflw",
    description="Link element",
    label="Contact",
    url="#",
    styling=Styling(size=Size(font_size="0.85rem", text_decoration="none"), position=Position(transition="color 0.2s"), color=Color(text_color="#94a3b8", color_palette="default")),
    component_id="i8yflw",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "#", "id": "i8yflw"}
)
ixia4g = ViewContainer(
    name="ixia4g",
    description=" component",
    view_elements={ihdcrl, iqpp08, i8yflw},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, gap="20px")),
    component_id="ixia4g",
    display_order=1,
    custom_attributes={"id": "ixia4g"}
)
ixia4g_layout = Layout(layout_type=LayoutType.FLEX, gap="20px")
ixia4g.layout = ixia4g_layout
iatiwl = ViewContainer(
    name="iatiwl",
    description="footer container",
    view_elements={component_3, ixia4g},
    styling=Styling(size=Size(padding="32px 48px", font_family="\'Inter\', \'Segoe UI\', system-ui, -apple-system, sans-serif", margin_top="24px"), position=Position(display="flex"), color=Color(background_color="#0f172a", text_color="#94a3b8", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")),
    component_id="iatiwl",
    tag_name="footer",
    display_order=2,
    css_classes=["assistant-footer"],
    custom_attributes={"id": "iatiwl"}
)
iatiwl_layout = Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")
iatiwl.layout = iatiwl_layout
i9fzj.view_elements = {irooz, ij4xh, iatiwl}


# Screen: ibqnl
ibqnl = Screen(name="ibqnl", description="Dashboard", view_elements=set(), route_path="/dashboard", screen_size="Medium")
ibqnl_styling_size = Size(font_family="\'Inter\', \'Segoe UI\', system-ui, -apple-system, sans-serif", min_height="100vh")
ibqnl_styling_pos = Position()
ibqnl_styling_color = Color(background_color="#f8fafc", text_color="#1e293b", color_palette="default")
ibqnl_styling = Styling(size=ibqnl_styling_size, position=ibqnl_styling_pos, color=ibqnl_styling_color)
ibqnl.styling = ibqnl_styling
ibqnl.component_id = "qWyJqLGyYzWfFcOlz"
ii626 = Text(
    name="ii626",
    content="ToDoList App",
    description="Text element",
    styling=Styling(size=Size(font_size="1.25rem", font_weight="700", letter_spacing="-0.01em"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="ii626",
    display_order=0,
    custom_attributes={"id": "ii626"}
)
ih3kq = Link(
    name="ih3kq",
    description="Link element",
    label="Home",
    url="/home",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="500", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="transparent", text_color="#64748b", color_palette="default", border_radius="8px")),
    component_id="ih3kq",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/home", "data-navigate-to": "home", "id": "ih3kq"}
)
i9t6i = Link(
    name="i9t6i",
    description="Link element",
    label="Dashboard",
    url="/dashboard",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="600", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="#eff6ff", text_color="#2563eb", color_palette="default", border_radius="8px")),
    component_id="i9t6i",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/dashboard", "data-navigate-to": "dashboard", "id": "i9t6i"}
)
itd5g = Link(
    name="itd5g",
    description="Link element",
    label="ToDoList Detail",
    url="/todolist-detail",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="500", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="transparent", text_color="#64748b", color_palette="default", border_radius="8px")),
    component_id="itd5g",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/todolist-detail", "data-navigate-to": "todolist-detail", "id": "itd5g"}
)
i8pjc = Link(
    name="i8pjc",
    description="Link element",
    label="User Profile",
    url="/user-profile",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="500", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="transparent", text_color="#64748b", color_palette="default", border_radius="8px")),
    component_id="i8pjc",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/user-profile", "data-navigate-to": "user-profile", "id": "i8pjc"}
)
ifqwm = ViewContainer(
    name="ifqwm",
    description=" component",
    view_elements={ih3kq, i9t6i, itd5g, i8pjc},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center", gap="4px")),
    component_id="ifqwm",
    display_order=1,
    custom_attributes={"id": "ifqwm"}
)
ifqwm_layout = Layout(layout_type=LayoutType.FLEX, align_items="center", gap="4px")
ifqwm.layout = ifqwm_layout
idcnd = ViewContainer(
    name="idcnd",
    description="nav container",
    view_elements={ii626, ifqwm},
    styling=Styling(size=Size(height="64px", padding="0 32px", font_family="\'Inter\', \'Segoe UI\', system-ui, -apple-system, sans-serif"), position=Position(p_type=PositionType.STICKY, top="0", z_index=50, display="flex"), color=Color(background_color="#ffffff", color_palette="default", border_bottom="1px solid #e2e8f0", box_shadow="0 1px 3px rgba(0,0,0,0.06)"), layout=Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")),
    component_id="idcnd",
    tag_name="nav",
    display_order=0,
    css_classes=["assistant-nav-header"],
    custom_attributes={"id": "idcnd"}
)
idcnd_layout = Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")
idcnd.layout = idcnd_layout
i37zm = Text(
    name="i37zm",
    content="Your Task Overview",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 16px 0", font_size="2.25rem", line_height="1.2", font_weight="800", letter_spacing="-0.02em"), color=Color(color_palette="default")),
    component_id="i37zm",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "i37zm"}
)
il0hg = Text(
    name="il0hg",
    content="Quickly see your lists and tasks status at a glance.",
    description="Text element",
    styling=Styling(size=Size(margin="0 auto 28px auto", font_size="1.1rem", line_height="1.6", max_width="600px"), color=Color(opacity="0.9", color_palette="default")),
    component_id="il0hg",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "il0hg"}
)
ipbj4 = Button(
    name="ipbj4",
    description="Button component",
    label="Continue",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(size=Size(padding="12px 28px", font_size="1rem", font_weight="600"), position=Position(cursor="pointer"), color=Color(background_color="#ffffff", text_color="#2563eb", color_palette="default", border_radius="10px", border="none", box_shadow="0 2px 8px rgba(0,0,0,0.15)")),
    component_id="ipbj4",
    tag_name="button",
    display_order=2,
    css_classes=["assistant-cta"],
    custom_attributes={"id": "ipbj4"}
)
i39kd = ViewContainer(
    name="i39kd",
    description="section container",
    view_elements={i37zm, il0hg, ipbj4},
    styling=Styling(size=Size(padding="64px 48px", margin="24px"), position=Position(alignment=Alignment.CENTER), color=Color(background_color="linear-gradient(135deg, #1e3a5f 0%, #2563eb 100%)", text_color="#ffffff", color_palette="default", border_radius="16px")),
    component_id="i39kd",
    tag_name="section",
    display_order=1,
    css_classes=["assistant-hero"],
    custom_attributes={"id": "i39kd"}
)
izlom = Text(
    name="izlom",
    content="Key Metrics",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 4px 0", font_size="1.25rem", font_weight="700"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="izlom",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "izlom"}
)
iuodc = MetricCard(
    name="iuodc",
    metric_title="Total Lists",
    format="number",
    value_color="#2c3e50",
    value_size=32,
    show_trend=True,
    positive_color="#27ae60",
    negative_color="#e74c3c",
    primary_color="#2c3e50",
    styling=Styling(size=Size(width="100%", min_height="140px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default")),
    component_id="iuodc",
    display_order=1,
    css_classes=["metric-card-component"],
    custom_attributes={"metric-title": "Total Lists", "data-source": "class_klgcpmeal_mo156c3f_2j9", "data-field": "attr_g59r7v3s8_mo156c3f_9ix", "format": "number", "value-color": "#2c3e50", "value-size": "32", "show-trend": "true", "positive-color": "#27ae60", "negative-color": "#e74c3c", "id": "iuodc"}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
iuodc_binding_domain = None
if domain_model_ref is not None:
    iuodc_binding_domain = domain_model_ref.get_class_by_name("User")
if iuodc_binding_domain:
    iuodc_binding = DataBinding(domain_concept=iuodc_binding_domain, name="Total_Lists_binding")
    iuodc_binding.data_field = next((attr for attr in iuodc_binding_domain.attributes if attr.name == "userId"), None)
else:
    # Domain class 'User' not resolved; data binding skipped.
    iuodc_binding = None
if iuodc_binding:
    iuodc.data_binding = iuodc_binding
i4h26 = MetricCard(
    name="i4h26",
    metric_title="Tasks Due Today",
    format="number",
    value_color="#2c3e50",
    value_size=32,
    show_trend=True,
    positive_color="#27ae60",
    negative_color="#e74c3c",
    primary_color="#2c3e50",
    styling=Styling(size=Size(width="100%", min_height="140px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default")),
    component_id="i4h26",
    display_order=2,
    css_classes=["metric-card-component"],
    custom_attributes={"metric-title": "Tasks Due Today", "data-source": "class_klgcpmeal_mo156c3f_2j9", "data-field": "attr_g59r7v3s8_mo156c3f_9ix", "format": "number", "value-color": "#2c3e50", "value-size": "32", "show-trend": "true", "positive-color": "#27ae60", "negative-color": "#e74c3c", "id": "i4h26"}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
i4h26_binding_domain = None
if domain_model_ref is not None:
    i4h26_binding_domain = domain_model_ref.get_class_by_name("User")
if i4h26_binding_domain:
    i4h26_binding = DataBinding(domain_concept=i4h26_binding_domain, name="Tasks_Due_Today_binding")
    i4h26_binding.data_field = next((attr for attr in i4h26_binding_domain.attributes if attr.name == "userId"), None)
else:
    # Domain class 'User' not resolved; data binding skipped.
    i4h26_binding = None
if i4h26_binding:
    i4h26.data_binding = i4h26_binding
iutbk = MetricCard(
    name="iutbk",
    metric_title="Completed Tasks This Week",
    format="number",
    value_color="#2c3e50",
    value_size=32,
    show_trend=True,
    positive_color="#27ae60",
    negative_color="#e74c3c",
    primary_color="#2c3e50",
    styling=Styling(size=Size(width="100%", min_height="140px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default")),
    component_id="iutbk",
    display_order=3,
    css_classes=["metric-card-component"],
    custom_attributes={"metric-title": "Completed Tasks This Week", "data-source": "class_klgcpmeal_mo156c3f_2j9", "data-field": "attr_g59r7v3s8_mo156c3f_9ix", "format": "number", "value-color": "#2c3e50", "value-size": "32", "show-trend": "true", "positive-color": "#27ae60", "negative-color": "#e74c3c", "id": "iutbk"}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
iutbk_binding_domain = None
if domain_model_ref is not None:
    iutbk_binding_domain = domain_model_ref.get_class_by_name("User")
if iutbk_binding_domain:
    iutbk_binding = DataBinding(domain_concept=iutbk_binding_domain, name="Completed_Tasks_This_Week_binding")
    iutbk_binding.data_field = next((attr for attr in iutbk_binding_domain.attributes if attr.name == "userId"), None)
else:
    # Domain class 'User' not resolved; data binding skipped.
    iutbk_binding = None
if iutbk_binding:
    iutbk.data_binding = iutbk_binding
ihilc = ViewContainer(
    name="ihilc",
    description="section container",
    view_elements={izlom, iuodc, i4h26, iutbk},
    styling=Styling(size=Size(margin="12px 24px"), position=Position(display="grid"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.GRID, grid_template_columns="repeat(3, 1fr)", gap="16px")),
    component_id="ihilc",
    tag_name="section",
    display_order=0,
    css_classes=["assistant-stats-grid"],
    custom_attributes={"id": "ihilc"}
)
ihilc_layout = Layout(layout_type=LayoutType.GRID, grid_template_columns="repeat(3, 1fr)", gap="16px")
ihilc.layout = ihilc_layout
iuwsl = Text(
    name="iuwsl",
    content="ToDoLists Overview",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 8px 0", font_size="1.35rem", font_weight="700"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="iuwsl",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "iuwsl"}
)
ip8t2 = Text(
    name="ip8t2",
    content="Your ToDoLists",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 16px 0", font_size="1.25rem", font_weight="700"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="ip8t2",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ip8t2"}
)
idhxc_col_0 = FieldColumn(label="Listid", field=ToDoList_listId)
idhxc_col_1 = FieldColumn(label="Title", field=ToDoList_title)
idhxc_col_2 = FieldColumn(label="Description", field=ToDoList_description)
idhxc_col_3 = FieldColumn(label="Createdat", field=ToDoList_createdAt)
idhxc_col_4 = FieldColumn(label="Updatedat", field=ToDoList_updatedAt)
idhxc = Table(
    name="idhxc",
    title="Your ToDoLists",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[idhxc_col_0, idhxc_col_1, idhxc_col_2, idhxc_col_3, idhxc_col_4],
    styling=Styling(size=Size(width="100%", margin="12px 0", min_height="300px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50", border_radius="12px")),
    component_id="idhxc",
    display_order=1,
    css_classes=["table-component"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Your ToDoLists", "data-source": "class_cvm5nzqm6_mo156c3f_sfx", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": "[{\"field\": \"listId\", \"label\": \"Listid\", \"columnType\": \"field\", \"_expanded\": false}, {\"field\": \"title\", \"label\": \"Title\", \"columnType\": \"field\", \"_expanded\": false}, {\"field\": \"description\", \"label\": \"Description\", \"columnType\": \"field\", \"_expanded\": false}, {\"field\": \"createdAt\", \"label\": \"Createdat\", \"columnType\": \"field\", \"_expanded\": false}, {\"field\": \"updatedAt\", \"label\": \"Updatedat\", \"columnType\": \"field\", \"_expanded\": false}]", "id": "idhxc"}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
idhxc_binding_domain = None
if domain_model_ref is not None:
    idhxc_binding_domain = domain_model_ref.get_class_by_name("ToDoList")
if idhxc_binding_domain:
    idhxc_binding = DataBinding(domain_concept=idhxc_binding_domain, name="ToDoListDataBinding")
else:
    # Domain class 'ToDoList' not resolved; data binding skipped.
    idhxc_binding = None
if idhxc_binding:
    idhxc.data_binding = idhxc_binding
iv1gz = ViewContainer(
    name="iv1gz",
    description="section container",
    view_elements={ip8t2, idhxc},
    styling=Styling(size=Size(padding="28px", margin="0"), color=Color(background_color="#ffffff", color_palette="default", border_radius="14px", border="1px solid #f1f5f9", box_shadow="0 1px 4px rgba(0,0,0,0.06)")),
    component_id="iv1gz",
    tag_name="section",
    display_order=1,
    css_classes=["assistant-card"],
    custom_attributes={"id": "iv1gz"}
)
ib8ek = Text(
    name="ib8ek",
    content="Tasks Status Distribution",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 16px 0", font_size="1.25rem", font_weight="700"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="ib8ek",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ib8ek"}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
ij85g_series_0_binding_domain = None
if domain_model_ref is not None:
    ij85g_series_0_binding_domain = domain_model_ref.get_class_by_name("Task")
if ij85g_series_0_binding_domain:
    ij85g_series_0_binding = DataBinding(domain_concept=ij85g_series_0_binding_domain, name="TaskDataBinding")
    ij85g_series_0_binding.label_field = next((attr for attr in ij85g_series_0_binding_domain.attributes if attr.name == "taskId"), None)
    ij85g_series_0_binding.data_field = next((attr for attr in ij85g_series_0_binding_domain.attributes if attr.name == "taskId"), None)
else:
    # Domain class 'Task' not resolved; data binding skipped.
    ij85g_series_0_binding = None
ij85g_series_0_styling_size = Size()
ij85g_series_0_styling_pos = Position()
ij85g_series_0_styling_color = Color(background_color="#3498db", bar_color="#3498db", color_palette="default", primary_color="#3498db")
ij85g_series_0_styling = Styling(size=ij85g_series_0_styling_size, position=ij85g_series_0_styling_pos, color=ij85g_series_0_styling_color)
ij85g_series_0 = Series(name="Taskid", label="Taskid", data_binding=ij85g_series_0_binding, styling=ij85g_series_0_styling)
ij85g = BarChart(
    name="ij85g",
    series=[ij85g_series_0],
    title="Tasks Status Distribution",
    bar_width=30,
    orientation="vertical",
    show_grid=True,
    show_legend=True,
    show_tooltip=True,
    stacked=False,
    animate=True,
    legend_position="top",
    grid_color="#e0e0e0",
    bar_gap=4,
    styling=Styling(size=Size(width="100%", margin="12px 0", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", border_radius="12px")),
    component_id="ij85g",
    display_order=1,
    css_classes=["bar-chart-component"],
    custom_attributes={"chart-title": "Tasks Status Distribution", "bar-width": "30", "orientation": "vertical", "show-grid": "true", "show-legend": "true", "stacked": "false", "series": "[{\"name\": \"Taskid\", \"data-source\": \"class_v10e1nt5o_mo156c3g_432\", \"color\": \"#3498db\", \"data\": [{\"name\": \"Completed\", \"value\": 45}, {\"name\": \"In Progress\", \"value\": 30}, {\"name\": \"Pending\", \"value\": 20}, {\"name\": \"Overdue\", \"value\": 5}], \"label-field\": \"attr_tc4t48klu_mo156c3g_cvq\", \"data-field\": \"attr_tc4t48klu_mo156c3g_cvq\"}]", "id": "ij85g"}
)
ieh2y = ViewContainer(
    name="ieh2y",
    description="section container",
    view_elements={ib8ek, ij85g},
    styling=Styling(size=Size(padding="28px", margin="0"), color=Color(background_color="#ffffff", color_palette="default", border_radius="14px", border="1px solid #f1f5f9", box_shadow="0 1px 4px rgba(0,0,0,0.06)")),
    component_id="ieh2y",
    tag_name="section",
    display_order=2,
    css_classes=["assistant-card"],
    custom_attributes={"id": "ieh2y"}
)
icj0c = ViewContainer(
    name="icj0c",
    description="section container",
    view_elements={iuwsl, iv1gz, ieh2y},
    styling=Styling(size=Size(margin="12px 24px"), position=Position(display="grid"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.GRID, grid_template_columns="1fr 1fr", gap="20px")),
    component_id="icj0c",
    tag_name="section",
    display_order=1,
    css_classes=["assistant-two-column"],
    custom_attributes={"id": "icj0c"}
)
icj0c_layout = Layout(layout_type=LayoutType.GRID, grid_template_columns="1fr 1fr", gap="20px")
icj0c.layout = icj0c_layout
ina4j = ViewContainer(
    name="ina4j",
    description="main container",
    view_elements={ihilc, icj0c},
    styling=Styling(size=Size(padding="24px 16px", margin="0 auto", max_width="1200px"), color=Color(color_palette="default")),
    component_id="ina4j",
    tag_name="main",
    display_order=2,
    css_classes=["assistant-main"],
    custom_attributes={"id": "ina4j"}
)
i4985 = ViewComponent(name="i4985", description=" component")
i4bbu = ViewComponent(name="i4bbu", description=" component")
component_2 = ViewContainer(
    name="Component_2",
    description=" component",
    view_elements={i4985, i4bbu},
    display_order=0
)
i1arl = Link(
    name="i1arl",
    description="Link element",
    label="Privacy",
    url="#",
    styling=Styling(size=Size(font_size="0.85rem", text_decoration="none"), position=Position(transition="color 0.2s"), color=Color(text_color="#94a3b8", color_palette="default")),
    component_id="i1arl",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "#", "id": "i1arl"}
)
ieq0l = Link(
    name="ieq0l",
    description="Link element",
    label="Terms",
    url="#",
    styling=Styling(size=Size(font_size="0.85rem", text_decoration="none"), position=Position(transition="color 0.2s"), color=Color(text_color="#94a3b8", color_palette="default")),
    component_id="ieq0l",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "#", "id": "ieq0l"}
)
ioopv = Link(
    name="ioopv",
    description="Link element",
    label="Contact",
    url="#",
    styling=Styling(size=Size(font_size="0.85rem", text_decoration="none"), position=Position(transition="color 0.2s"), color=Color(text_color="#94a3b8", color_palette="default")),
    component_id="ioopv",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "#", "id": "ioopv"}
)
itr8v = ViewContainer(
    name="itr8v",
    description=" component",
    view_elements={i1arl, ieq0l, ioopv},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, gap="20px")),
    component_id="itr8v",
    display_order=1,
    custom_attributes={"id": "itr8v"}
)
itr8v_layout = Layout(layout_type=LayoutType.FLEX, gap="20px")
itr8v.layout = itr8v_layout
ixyxj = ViewContainer(
    name="ixyxj",
    description="footer container",
    view_elements={component_2, itr8v},
    styling=Styling(size=Size(padding="32px 48px", font_family="\'Inter\', \'Segoe UI\', system-ui, -apple-system, sans-serif", margin_top="24px"), position=Position(display="flex"), color=Color(background_color="#0f172a", text_color="#94a3b8", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")),
    component_id="ixyxj",
    tag_name="footer",
    display_order=3,
    css_classes=["assistant-footer"],
    custom_attributes={"id": "ixyxj"}
)
ixyxj_layout = Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")
ixyxj.layout = ixyxj_layout
ibqnl.view_elements = {idcnd, i39kd, ina4j, ixyxj}


# Screen: ikyv
ikyv = Screen(name="ikyv", description="Home", view_elements=set(), is_main_page=True, route_path="/home", screen_size="Medium")
ikyv_styling_size = Size(font_family="\'Inter\', \'Segoe UI\', system-ui, -apple-system, sans-serif", min_height="100vh")
ikyv_styling_pos = Position()
ikyv_styling_color = Color(background_color="#f8fafc", text_color="#1e293b", color_palette="default")
ikyv_styling = Styling(size=ikyv_styling_size, position=ikyv_styling_pos, color=ikyv_styling_color)
ikyv.styling = ikyv_styling
ikyv.component_id = "yi9G1RujaWDf9ofo"
i70f = Text(
    name="i70f",
    content="ToDoList App",
    description="Text element",
    styling=Styling(size=Size(font_size="1.25rem", font_weight="700", letter_spacing="-0.01em"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="i70f",
    display_order=0,
    custom_attributes={"id": "i70f"}
)
iqoz = Link(
    name="iqoz",
    description="Link element",
    label="Home",
    url="/home",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="600", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="#eff6ff", text_color="#2563eb", color_palette="default", border_radius="8px")),
    component_id="iqoz",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/home", "data-navigate-to": "home", "id": "iqoz"}
)
ign47 = Link(
    name="ign47",
    description="Link element",
    label="Dashboard",
    url="/dashboard",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="500", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="transparent", text_color="#64748b", color_palette="default", border_radius="8px")),
    component_id="ign47",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/dashboard", "data-navigate-to": "dashboard", "id": "ign47"}
)
iuydy = Link(
    name="iuydy",
    description="Link element",
    label="ToDoList Detail",
    url="/todolist-detail",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="500", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="transparent", text_color="#64748b", color_palette="default", border_radius="8px")),
    component_id="iuydy",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/todolist-detail", "data-navigate-to": "todolist-detail", "id": "iuydy"}
)
ik8z7 = Link(
    name="ik8z7",
    description="Link element",
    label="User Profile",
    url="/user-profile",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="500", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="transparent", text_color="#64748b", color_palette="default", border_radius="8px")),
    component_id="ik8z7",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/user-profile", "data-navigate-to": "user-profile", "id": "ik8z7"}
)
i47y = ViewContainer(
    name="i47y",
    description=" component",
    view_elements={iqoz, ign47, iuydy, ik8z7},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center", gap="4px")),
    component_id="i47y",
    display_order=1,
    custom_attributes={"id": "i47y"}
)
i47y_layout = Layout(layout_type=LayoutType.FLEX, align_items="center", gap="4px")
i47y.layout = i47y_layout
ivd9 = ViewContainer(
    name="ivd9",
    description="nav container",
    view_elements={i70f, i47y},
    styling=Styling(size=Size(height="64px", padding="0 32px", font_family="\'Inter\', \'Segoe UI\', system-ui, -apple-system, sans-serif"), position=Position(p_type=PositionType.STICKY, top="0", z_index=50, display="flex"), color=Color(background_color="#ffffff", color_palette="default", border_bottom="1px solid #e2e8f0", box_shadow="0 1px 3px rgba(0,0,0,0.06)"), layout=Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")),
    component_id="ivd9",
    tag_name="nav",
    display_order=0,
    css_classes=["assistant-nav-header"],
    custom_attributes={"id": "ivd9"}
)
ivd9_layout = Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")
ivd9.layout = ivd9_layout
iu3aj = Text(
    name="iu3aj",
    content="Organize your tasks effortlessly",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 16px 0", font_size="2.25rem", line_height="1.2", font_weight="800", letter_spacing="-0.02em"), color=Color(color_palette="default")),
    component_id="iu3aj",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "iu3aj"}
)
ijbp3 = Text(
    name="ijbp3",
    content="Manage your ToDo lists and tasks with ease. Stay productive and never miss a deadline.",
    description="Text element",
    styling=Styling(size=Size(margin="0 auto 28px auto", font_size="1.1rem", line_height="1.6", max_width="600px"), color=Color(opacity="0.9", color_palette="default")),
    component_id="ijbp3",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "ijbp3"}
)
izgtd = Button(
    name="izgtd",
    description="Button component",
    label="Get Started",
    buttonType=ButtonType.CustomizableButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(size=Size(padding="12px 28px", font_size="1rem", font_weight="600"), position=Position(cursor="pointer"), color=Color(background_color="#ffffff", text_color="#2563eb", color_palette="default", border_radius="10px", border="none", box_shadow="0 2px 8px rgba(0,0,0,0.15)")),
    component_id="izgtd",
    tag_name="button",
    display_order=2,
    css_classes=["assistant-cta"],
    custom_attributes={"id": "izgtd"}
)
iamyn = ViewContainer(
    name="iamyn",
    description="section container",
    view_elements={iu3aj, ijbp3, izgtd},
    styling=Styling(size=Size(padding="64px 48px", margin="24px"), position=Position(alignment=Alignment.CENTER), color=Color(background_color="linear-gradient(135deg, #1e3a5f 0%, #2563eb 100%)", text_color="#ffffff", color_palette="default", border_radius="16px")),
    component_id="iamyn",
    tag_name="section",
    display_order=1,
    css_classes=["assistant-hero"],
    custom_attributes={"id": "iamyn"}
)
izg2j = Text(
    name="izg2j",
    content="Features",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 18px 0", font_size="1.35rem", font_weight="700"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="izg2j",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "izg2j"}
)
i7kld = ViewContainer(
    name="i7kld",
    description="li container",
    view_elements=set(),
    styling=Styling(size=Size(margin="10px 0", line_height="1.5"), color=Color(text_color="#334155", color_palette="default")),
    component_id="i7kld",
    tag_name="li",
    display_order=0,
    custom_attributes={"id": "i7kld"}
)
ijk5o = ViewContainer(
    name="ijk5o",
    description="li container",
    view_elements=set(),
    styling=Styling(size=Size(margin="10px 0", line_height="1.5"), color=Color(text_color="#334155", color_palette="default")),
    component_id="ijk5o",
    tag_name="li",
    display_order=1,
    custom_attributes={"id": "ijk5o"}
)
iy29g = ViewContainer(
    name="iy29g",
    description="li container",
    view_elements=set(),
    styling=Styling(size=Size(margin="10px 0", line_height="1.5"), color=Color(text_color="#334155", color_palette="default")),
    component_id="iy29g",
    tag_name="li",
    display_order=2,
    custom_attributes={"id": "iy29g"}
)
i76cr = ViewContainer(
    name="i76cr",
    description="li container",
    view_elements=set(),
    styling=Styling(size=Size(margin="10px 0", line_height="1.5"), color=Color(text_color="#334155", color_palette="default")),
    component_id="i76cr",
    tag_name="li",
    display_order=3,
    custom_attributes={"id": "i76cr"}
)
i842i = ViewContainer(
    name="i842i",
    description="ul container",
    view_elements={i7kld, ijk5o, iy29g, i76cr},
    styling=Styling(size=Size(margin="0", padding_left="20px"), color=Color(color_palette="default")),
    component_id="i842i",
    tag_name="ul",
    display_order=1,
    custom_attributes={"id": "i842i"}
)
id7pm = ViewContainer(
    name="id7pm",
    description="section container",
    view_elements={izg2j, i842i},
    styling=Styling(size=Size(padding="32px", margin="12px 24px"), color=Color(background_color="#ffffff", color_palette="default", border_radius="14px", border="1px solid #f1f5f9", box_shadow="0 1px 4px rgba(0,0,0,0.06)")),
    component_id="id7pm",
    tag_name="section",
    display_order=0,
    css_classes=["assistant-features"],
    custom_attributes={"id": "id7pm"}
)
ihjeg = ViewContainer(
    name="ihjeg",
    description="main container",
    view_elements={id7pm},
    styling=Styling(size=Size(padding="24px 16px", margin="0 auto", max_width="1200px"), color=Color(color_palette="default")),
    component_id="ihjeg",
    tag_name="main",
    display_order=2,
    css_classes=["assistant-main"],
    custom_attributes={"id": "ihjeg"}
)
iji2j = ViewComponent(name="iji2j", description=" component")
ia4n6 = ViewComponent(name="ia4n6", description=" component")
component = ViewContainer(
    name="Component",
    description=" component",
    view_elements={iji2j, ia4n6},
    display_order=0
)
ipbdr = Link(
    name="ipbdr",
    description="Link element",
    label="Privacy",
    url="#",
    styling=Styling(size=Size(font_size="0.85rem", text_decoration="none"), position=Position(transition="color 0.2s"), color=Color(text_color="#94a3b8", color_palette="default")),
    component_id="ipbdr",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "#", "id": "ipbdr"}
)
ijsdy = Link(
    name="ijsdy",
    description="Link element",
    label="Terms",
    url="#",
    styling=Styling(size=Size(font_size="0.85rem", text_decoration="none"), position=Position(transition="color 0.2s"), color=Color(text_color="#94a3b8", color_palette="default")),
    component_id="ijsdy",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "#", "id": "ijsdy"}
)
izs2h = Link(
    name="izs2h",
    description="Link element",
    label="Contact",
    url="#",
    styling=Styling(size=Size(font_size="0.85rem", text_decoration="none"), position=Position(transition="color 0.2s"), color=Color(text_color="#94a3b8", color_palette="default")),
    component_id="izs2h",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "#", "id": "izs2h"}
)
i2032 = ViewContainer(
    name="i2032",
    description=" component",
    view_elements={ipbdr, ijsdy, izs2h},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, gap="20px")),
    component_id="i2032",
    display_order=1,
    custom_attributes={"id": "i2032"}
)
i2032_layout = Layout(layout_type=LayoutType.FLEX, gap="20px")
i2032.layout = i2032_layout
i6ozb = ViewContainer(
    name="i6ozb",
    description="footer container",
    view_elements={component, i2032},
    styling=Styling(size=Size(padding="32px 48px", font_family="\'Inter\', \'Segoe UI\', system-ui, -apple-system, sans-serif", margin_top="24px"), position=Position(display="flex"), color=Color(background_color="#0f172a", text_color="#94a3b8", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")),
    component_id="i6ozb",
    tag_name="footer",
    display_order=3,
    css_classes=["assistant-footer"],
    custom_attributes={"id": "i6ozb"}
)
i6ozb_layout = Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")
i6ozb.layout = i6ozb_layout
ikyv.view_elements = {ivd9, iamyn, ihjeg, i6ozb}


# Screen: io4xn1
io4xn1 = Screen(name="io4xn1", description="User Profile", view_elements=set(), route_path="/user-profile", screen_size="Medium")
io4xn1_styling_size = Size(font_family="\'Inter\', \'Segoe UI\', system-ui, -apple-system, sans-serif", min_height="100vh")
io4xn1_styling_pos = Position()
io4xn1_styling_color = Color(background_color="#f8fafc", text_color="#1e293b", color_palette="default")
io4xn1_styling = Styling(size=io4xn1_styling_size, position=io4xn1_styling_pos, color=io4xn1_styling_color)
io4xn1.styling = io4xn1_styling
io4xn1.component_id = "CX39jw4B8Ahc328pzWR"
invmw6 = Text(
    name="invmw6",
    content="ToDoList App",
    description="Text element",
    styling=Styling(size=Size(font_size="1.25rem", font_weight="700", letter_spacing="-0.01em"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="invmw6",
    display_order=0,
    custom_attributes={"id": "invmw6"}
)
ibview = Link(
    name="ibview",
    description="Link element",
    label="Home",
    url="/home",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="500", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="transparent", text_color="#64748b", color_palette="default", border_radius="8px")),
    component_id="ibview",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/home", "data-navigate-to": "home", "id": "ibview"}
)
i51yup = Link(
    name="i51yup",
    description="Link element",
    label="Dashboard",
    url="/dashboard",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="500", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="transparent", text_color="#64748b", color_palette="default", border_radius="8px")),
    component_id="i51yup",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/dashboard", "data-navigate-to": "dashboard", "id": "i51yup"}
)
i3fho2 = Link(
    name="i3fho2",
    description="Link element",
    label="ToDoList Detail",
    url="/todolist-detail",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="500", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="transparent", text_color="#64748b", color_palette="default", border_radius="8px")),
    component_id="i3fho2",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/todolist-detail", "data-navigate-to": "todolist-detail", "id": "i3fho2"}
)
ialbvb = Link(
    name="ialbvb",
    description="Link element",
    label="User Profile",
    url="/user-profile",
    styling=Styling(size=Size(padding="8px 16px", font_size="0.9rem", font_weight="600", text_decoration="none"), position=Position(transition="all 0.2s"), color=Color(background_color="#eff6ff", text_color="#2563eb", color_palette="default", border_radius="8px")),
    component_id="ialbvb",
    tag_name="a",
    display_order=3,
    custom_attributes={"href": "/user-profile", "data-navigate-to": "user-profile", "id": "ialbvb"}
)
i9ac1g = ViewContainer(
    name="i9ac1g",
    description=" component",
    view_elements={ibview, i51yup, i3fho2, ialbvb},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, align_items="center", gap="4px")),
    component_id="i9ac1g",
    display_order=1,
    custom_attributes={"id": "i9ac1g"}
)
i9ac1g_layout = Layout(layout_type=LayoutType.FLEX, align_items="center", gap="4px")
i9ac1g.layout = i9ac1g_layout
iemxdf = ViewContainer(
    name="iemxdf",
    description="nav container",
    view_elements={invmw6, i9ac1g},
    styling=Styling(size=Size(height="64px", padding="0 32px", font_family="\'Inter\', \'Segoe UI\', system-ui, -apple-system, sans-serif"), position=Position(p_type=PositionType.STICKY, top="0", z_index=50, display="flex"), color=Color(background_color="#ffffff", color_palette="default", border_bottom="1px solid #e2e8f0", box_shadow="0 1px 3px rgba(0,0,0,0.06)"), layout=Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")),
    component_id="iemxdf",
    tag_name="nav",
    display_order=0,
    css_classes=["assistant-nav-header"],
    custom_attributes={"id": "iemxdf"}
)
iemxdf_layout = Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")
iemxdf.layout = iemxdf_layout
iapeak = Text(
    name="iapeak",
    content="User Profile",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 12px 0", font_size="1.35rem", font_weight="700"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="iapeak",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "iapeak"}
)
i1q1v5 = Text(
    name="i1q1v5",
    content="Manage your account information and preferences.",
    description="Text element",
    styling=Styling(size=Size(margin="0", line_height="1.6"), color=Color(text_color="#475569", color_palette="default")),
    component_id="i1q1v5",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "i1q1v5"}
)
ipar9f = ViewContainer(
    name="ipar9f",
    description="section container",
    view_elements={iapeak, i1q1v5},
    styling=Styling(size=Size(padding="32px", margin="12px 24px"), color=Color(background_color="#ffffff", color_palette="default", border_radius="14px", border="1px solid #f1f5f9", box_shadow="0 1px 4px rgba(0,0,0,0.06)")),
    component_id="ipar9f",
    tag_name="section",
    display_order=0,
    css_classes=["assistant-content"],
    custom_attributes={"id": "ipar9f"}
)
is809d = Text(
    name="is809d",
    content="Edit Profile",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 20px 0", font_size="1.35rem", font_weight="700"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="is809d",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "is809d"}
)
ixpqsg = InputField(
    name="ixpqsg",
    description="Text input",
    field_type=InputFieldType.Text,
    styling=Styling(size=Size(padding="12px 14px", font_size="0.95rem"), color=Color(background_color="#f8fafc", color_palette="default", border_radius="10px", border="1px solid #e2e8f0")),
    component_id="ixpqsg",
    tag_name="input",
    display_order=1,
    custom_attributes={"type": "text", "name": "email", "placeholder": "email", "id": "ixpqsg"}
)
i7tcib = InputField(
    name="i7tcib",
    description="Text input",
    field_type=InputFieldType.Text,
    styling=Styling(size=Size(padding="12px 14px", font_size="0.95rem"), color=Color(background_color="#f8fafc", color_palette="default", border_radius="10px", border="1px solid #e2e8f0")),
    component_id="i7tcib",
    tag_name="input",
    display_order=0,
    custom_attributes={"type": "text", "name": "username", "placeholder": "username", "id": "i7tcib"}
)
form_2 = Form(
    name="form_2",
    description="Form component",
    inputFields={ixpqsg, i7tcib},
    tag_name="form",
    display_order=1
)
ievjlj = ViewContainer(
    name="ievjlj",
    description="section container",
    view_elements={is809d, form_2},
    styling=Styling(size=Size(padding="32px", margin="12px 24px"), color=Color(background_color="#ffffff", color_palette="default", border_radius="14px", border="1px solid #f1f5f9", box_shadow="0 1px 4px rgba(0,0,0,0.06)")),
    component_id="ievjlj",
    tag_name="section",
    display_order=1,
    css_classes=["assistant-form"],
    custom_attributes={"id": "ievjlj"}
)
ib13m9 = Text(
    name="ib13m9",
    content="Change Password",
    description="Text element",
    styling=Styling(size=Size(margin="0 0 20px 0", font_size="1.35rem", font_weight="700"), color=Color(text_color="#0f172a", color_palette="default")),
    component_id="ib13m9",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ib13m9"}
)
iq17jy = InputField(
    name="iq17jy",
    description="Text input",
    field_type=InputFieldType.Text,
    styling=Styling(size=Size(padding="12px 14px", font_size="0.95rem"), color=Color(background_color="#f8fafc", color_palette="default", border_radius="10px", border="1px solid #e2e8f0")),
    component_id="iq17jy",
    tag_name="input",
    display_order=2,
    custom_attributes={"type": "text", "name": "confirmnewpassword", "placeholder": "confirmNewPassword", "id": "iq17jy"}
)
ia7cip = InputField(
    name="ia7cip",
    description="Text input",
    field_type=InputFieldType.Text,
    styling=Styling(size=Size(padding="12px 14px", font_size="0.95rem"), color=Color(background_color="#f8fafc", color_palette="default", border_radius="10px", border="1px solid #e2e8f0")),
    component_id="ia7cip",
    tag_name="input",
    display_order=1,
    custom_attributes={"type": "text", "name": "newpassword", "placeholder": "newPassword", "id": "ia7cip"}
)
ikyuvx = InputField(
    name="ikyuvx",
    description="Text input",
    field_type=InputFieldType.Text,
    styling=Styling(size=Size(padding="12px 14px", font_size="0.95rem"), color=Color(background_color="#f8fafc", color_palette="default", border_radius="10px", border="1px solid #e2e8f0")),
    component_id="ikyuvx",
    tag_name="input",
    display_order=0,
    custom_attributes={"type": "text", "name": "currentpassword", "placeholder": "currentPassword", "id": "ikyuvx"}
)
form_3 = Form(
    name="form_3",
    description="Form component",
    inputFields={iq17jy, ia7cip, ikyuvx},
    tag_name="form",
    display_order=1
)
igbdhq = ViewContainer(
    name="igbdhq",
    description="section container",
    view_elements={ib13m9, form_3},
    styling=Styling(size=Size(padding="32px", margin="12px 24px"), color=Color(background_color="#ffffff", color_palette="default", border_radius="14px", border="1px solid #f1f5f9", box_shadow="0 1px 4px rgba(0,0,0,0.06)")),
    component_id="igbdhq",
    tag_name="section",
    display_order=2,
    css_classes=["assistant-form"],
    custom_attributes={"id": "igbdhq"}
)
io9uso = ViewContainer(
    name="io9uso",
    description="main container",
    view_elements={ipar9f, ievjlj, igbdhq},
    styling=Styling(size=Size(padding="24px 16px", margin="0 auto", max_width="1200px"), color=Color(color_palette="default")),
    component_id="io9uso",
    tag_name="main",
    display_order=1,
    css_classes=["assistant-main"],
    custom_attributes={"id": "io9uso"}
)
is0n1t = ViewComponent(name="is0n1t", description=" component")
iw1b9j = ViewComponent(name="iw1b9j", description=" component")
component_4 = ViewContainer(
    name="Component_4",
    description=" component",
    view_elements={is0n1t, iw1b9j},
    display_order=0
)
ia9o4u = Link(
    name="ia9o4u",
    description="Link element",
    label="Privacy",
    url="#",
    styling=Styling(size=Size(font_size="0.85rem", text_decoration="none"), position=Position(transition="color 0.2s"), color=Color(text_color="#94a3b8", color_palette="default")),
    component_id="ia9o4u",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "#", "id": "ia9o4u"}
)
il637e = Link(
    name="il637e",
    description="Link element",
    label="Terms",
    url="#",
    styling=Styling(size=Size(font_size="0.85rem", text_decoration="none"), position=Position(transition="color 0.2s"), color=Color(text_color="#94a3b8", color_palette="default")),
    component_id="il637e",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "#", "id": "il637e"}
)
izgide = Link(
    name="izgide",
    description="Link element",
    label="Contact",
    url="#",
    styling=Styling(size=Size(font_size="0.85rem", text_decoration="none"), position=Position(transition="color 0.2s"), color=Color(text_color="#94a3b8", color_palette="default")),
    component_id="izgide",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "#", "id": "izgide"}
)
ih9mrr = ViewContainer(
    name="ih9mrr",
    description=" component",
    view_elements={ia9o4u, il637e, izgide},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, gap="20px")),
    component_id="ih9mrr",
    display_order=1,
    custom_attributes={"id": "ih9mrr"}
)
ih9mrr_layout = Layout(layout_type=LayoutType.FLEX, gap="20px")
ih9mrr.layout = ih9mrr_layout
isoi5a = ViewContainer(
    name="isoi5a",
    description="footer container",
    view_elements={component_4, ih9mrr},
    styling=Styling(size=Size(padding="32px 48px", font_family="\'Inter\', \'Segoe UI\', system-ui, -apple-system, sans-serif", margin_top="24px"), position=Position(display="flex"), color=Color(background_color="#0f172a", text_color="#94a3b8", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")),
    component_id="isoi5a",
    tag_name="footer",
    display_order=2,
    css_classes=["assistant-footer"],
    custom_attributes={"id": "isoi5a"}
)
isoi5a_layout = Layout(layout_type=LayoutType.FLEX, justify_content="space-between", align_items="center")
isoi5a.layout = isoi5a_layout
io4xn1.view_elements = {iemxdf, io9uso, isoi5a}

gui_module = Module(
    name="GUI_Module",
    screens={i9fzj, ibqnl, ikyv, io4xn1}
)

# GUI Model
gui_model = GUIModel(
    name="GUI",
    package="",
    versionCode="1.0",
    versionName="1.0",
    modules={gui_module},
    description="GUI"
)
