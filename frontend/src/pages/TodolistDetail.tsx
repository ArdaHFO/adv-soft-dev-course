import React from "react";
import { ChartBlock } from "../components/runtime/ChartBlock";
import { TableBlock } from "../components/runtime/TableBlock";

const TodolistDetail: React.FC = () => {
  return (
    <div id="GjDawjQkKgmDfrtEdh" style={{"fontFamily": "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif", "minHeight": "100vh", "background": "#f8fafc", "color": "#1e293b", "--chart-color-palette": "default"}}>
    <nav id="irooz" className="assistant-nav-header" style={{"height": "64px", "padding": "0 32px", "fontFamily": "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif", "position": "sticky", "top": "0", "zIndex": 50, "display": "flex", "background": "#ffffff", "borderBottom": "1px solid #e2e8f0", "boxShadow": "0 1px 3px rgba(0,0,0,0.06)", "--chart-color-palette": "default", "justifyContent": "space-between", "alignItems": "center"}}>
      <p id="ibb9n" style={{"fontSize": "1.25rem", "fontWeight": "700", "letterSpacing": "-0.01em", "color": "#0f172a", "--chart-color-palette": "default"}}>{"ToDoList App"}</p>
      <div id="ikw5o" style={{"display": "flex", "--chart-color-palette": "default", "alignItems": "center", "gap": "4px"}}>
        <a id="iyx6g" style={{"padding": "8px 16px", "fontSize": "0.9rem", "fontWeight": "500", "textDecoration": "none", "transition": "all 0.2s", "background": "transparent", "color": "#64748b", "borderRadius": "8px", "--chart-color-palette": "default"}} href="/home" {...{"data-navigate-to": "home"}}>{"Home"}</a>
        <a id="i486d" style={{"padding": "8px 16px", "fontSize": "0.9rem", "fontWeight": "500", "textDecoration": "none", "transition": "all 0.2s", "background": "transparent", "color": "#64748b", "borderRadius": "8px", "--chart-color-palette": "default"}} href="/dashboard" {...{"data-navigate-to": "dashboard"}}>{"Dashboard"}</a>
        <a id="ikoe7" style={{"padding": "8px 16px", "fontSize": "0.9rem", "fontWeight": "600", "textDecoration": "none", "transition": "all 0.2s", "background": "#eff6ff", "color": "#2563eb", "borderRadius": "8px", "--chart-color-palette": "default"}} href="/todolist-detail" {...{"data-navigate-to": "todolist-detail"}}>{"ToDoList Detail"}</a>
        <a id="i54lf" style={{"padding": "8px 16px", "fontSize": "0.9rem", "fontWeight": "500", "textDecoration": "none", "transition": "all 0.2s", "background": "transparent", "color": "#64748b", "borderRadius": "8px", "--chart-color-palette": "default"}} href="/user-profile" {...{"data-navigate-to": "user-profile"}}>{"User Profile"}</a>
      </div>
    </nav>
    <main id="ij4xh" className="assistant-main" style={{"padding": "24px 16px", "margin": "0 auto", "maxWidth": "1200px", "--chart-color-palette": "default"}}>
      <section id="i7izo" className="assistant-content" style={{"padding": "32px", "margin": "12px 24px", "background": "#ffffff", "borderRadius": "14px", "border": "1px solid #f1f5f9", "boxShadow": "0 1px 4px rgba(0,0,0,0.06)", "--chart-color-palette": "default"}}>
        <h2 id="iwgsv" style={{"margin": "0 0 12px 0", "fontSize": "1.35rem", "fontWeight": "700", "color": "#0f172a", "--chart-color-palette": "default"}}>{"Work Projects"}</h2>
        <p id="ig5ph" style={{"margin": "0", "lineHeight": "1.6", "color": "#475569", "--chart-color-palette": "default"}}>{"Tasks related to ongoing work projects. Manage your tasks below."}</p>
      </section>
      <section id="iv2sze" className="assistant-two-column" style={{"margin": "12px 24px", "display": "grid", "--chart-color-palette": "default", "gap": "20px", "gridTemplateColumns": "1fr 1fr"}}>
        <h2 id="i1ft3v" style={{"margin": "0 0 8px 0", "fontSize": "1.35rem", "fontWeight": "700", "color": "#0f172a", "--chart-color-palette": "default"}}>{"Tasks and Status"}</h2>
        <section id="iix4xi" className="assistant-card" style={{"padding": "28px", "margin": "0", "background": "#ffffff", "borderRadius": "14px", "border": "1px solid #f1f5f9", "boxShadow": "0 1px 4px rgba(0,0,0,0.06)", "--chart-color-palette": "default"}}>
          <h2 id="iai5of" style={{"margin": "0 0 16px 0", "fontSize": "1.25rem", "fontWeight": "700", "color": "#0f172a", "--chart-color-palette": "default"}}>{"Tasks in List"}</h2>
          <TableBlock id="i8kwjh" styles={{"width": "100%", "margin": "12px 0", "minHeight": "300px", "borderRadius": "12px", "--chart-color-palette": "default"}} title="Tasks in List" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Taskid", "column_type": "field", "field": "taskId", "type": "str", "required": true}, {"label": "Title", "column_type": "field", "field": "title", "type": "str", "required": true}, {"label": "Description", "column_type": "field", "field": "description", "type": "str", "required": true}, {"label": "Duedate", "column_type": "field", "field": "dueDate", "type": "date", "required": true}, {"label": "Priority", "column_type": "field", "field": "priority", "type": "enum", "options": ["High", "Low", "Medium"], "required": true}, {"label": "Status", "column_type": "field", "field": "status", "type": "enum", "options": ["Cancelled", "Completed", "InProgress", "Pending"], "required": true}, {"label": "Createdat", "column_type": "field", "field": "createdAt", "type": "date", "required": true}, {"label": "Updatedat", "column_type": "field", "field": "updatedAt", "type": "date", "required": true}], "formColumns": [{"column_type": "field", "field": "taskId", "label": "taskId", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "title", "label": "title", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "description", "label": "description", "type": "str", "required": false, "defaultValue": null}, {"column_type": "field", "field": "dueDate", "label": "dueDate", "type": "date", "required": false, "defaultValue": null}, {"column_type": "field", "field": "priority", "label": "priority", "type": "enum", "required": true, "defaultValue": "Medium", "options": ["High", "Low", "Medium"]}, {"column_type": "field", "field": "status", "label": "status", "type": "enum", "required": true, "defaultValue": "Pending", "options": ["Cancelled", "Completed", "InProgress", "Pending"]}, {"column_type": "field", "field": "createdAt", "label": "createdAt", "type": "date", "required": true, "defaultValue": null}, {"column_type": "field", "field": "updatedAt", "label": "updatedAt", "type": "date", "required": false, "defaultValue": null}, {"column_type": "lookup", "path": "contains", "field": "contains", "lookup_field": "listId", "entity": "ToDoList", "type": "str", "required": true}]}} dataBinding={{"entity": "Task", "endpoint": "/task/"}} />
        </section>
        <section id="i3jd8l" className="assistant-card" style={{"padding": "28px", "margin": "0", "background": "#ffffff", "borderRadius": "14px", "border": "1px solid #f1f5f9", "boxShadow": "0 1px 4px rgba(0,0,0,0.06)", "--chart-color-palette": "default"}}>
          <h2 id="iwc1jk" style={{"margin": "0 0 16px 0", "fontSize": "1.25rem", "fontWeight": "700", "color": "#0f172a", "--chart-color-palette": "default"}}>{"Task Priority Distribution"}</h2>
          <ChartBlock id="i5453j" styles={{"width": "100%", "margin": "12px 0", "minHeight": "400px", "borderRadius": "12px", "--chart-color-palette": "default"}} chartType="pie-chart" title="Task Priority Distribution" color="default" chart={{"showLegend": true, "legendPosition": "bottom", "showLabels": true, "labelPosition": "inside", "paddingAngle": 0, "innerRadius": 0, "outerRadius": 80, "startAngle": 0, "endAngle": 360}} series={[{"name": "Task", "label": "Task", "color": "#4CAF50", "dataSource": "task", "endpoint": "/task/"}]} />
        </section>
      </section>
      <section id="iqugvf" className="assistant-form" style={{"padding": "32px", "margin": "12px 24px", "background": "#ffffff", "borderRadius": "14px", "border": "1px solid #f1f5f9", "boxShadow": "0 1px 4px rgba(0,0,0,0.06)", "--chart-color-palette": "default"}}>
        <h2 id="i86yvj" style={{"margin": "0 0 20px 0", "fontSize": "1.35rem", "fontWeight": "700", "color": "#0f172a", "--chart-color-palette": "default"}}>{"Add New Task"}</h2>
        <form id="form" onSubmit={(e) => { e.preventDefault(); }}>
          <div style={{"marginBottom": "10px"}}>
            <label htmlFor="i0z3e1" style={{"display": "block", "marginBottom": "5px"}}>{"i0z3e1"}</label>
            <input id="i0z3e1" type="text" />
          </div>
          <div style={{"marginBottom": "10px"}}>
            <label htmlFor="i2w6jw" style={{"display": "block", "marginBottom": "5px"}}>{"i2w6jw"}</label>
            <input id="i2w6jw" type="text" />
          </div>
          <div style={{"marginBottom": "10px"}}>
            <label htmlFor="i471qn" style={{"display": "block", "marginBottom": "5px"}}>{"i471qn"}</label>
            <input id="i471qn" type="text" />
          </div>
          <div style={{"marginBottom": "10px"}}>
            <label htmlFor="i54sfh" style={{"display": "block", "marginBottom": "5px"}}>{"i54sfh"}</label>
            <input id="i54sfh" type="text" />
          </div>
          <div style={{"marginBottom": "10px"}}>
            <label htmlFor="idpiwg" style={{"display": "block", "marginBottom": "5px"}}>{"idpiwg"}</label>
            <input id="idpiwg" type="text" />
          </div>
          <button type="submit">Submit</button>
        </form>
      </section>
    </main>
    <footer id="iatiwl" className="assistant-footer" style={{"padding": "32px 48px", "fontFamily": "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif", "marginTop": "24px", "display": "flex", "background": "#0f172a", "color": "#94a3b8", "--chart-color-palette": "default", "justifyContent": "space-between", "alignItems": "center"}}>
      <div id="Component_3">
        <div id="imu91j" style={{"fontSize": "1.1rem", "fontWeight": "700", "marginBottom": "4px", "color": "#ffffff", "--chart-color-palette": "default"}} />
        <div id="i7rrlj" style={{"fontSize": "0.8rem", "--chart-color-palette": "default"}} />
      </div>
      <div id="ixia4g" style={{"display": "flex", "--chart-color-palette": "default", "gap": "20px"}}>
        <a id="ihdcrl" style={{"fontSize": "0.85rem", "textDecoration": "none", "transition": "color 0.2s", "color": "#94a3b8", "--chart-color-palette": "default"}} href="/">{"Privacy"}</a>
        <a id="iqpp08" style={{"fontSize": "0.85rem", "textDecoration": "none", "transition": "color 0.2s", "color": "#94a3b8", "--chart-color-palette": "default"}} href="/">{"Terms"}</a>
        <a id="i8yflw" style={{"fontSize": "0.85rem", "textDecoration": "none", "transition": "color 0.2s", "color": "#94a3b8", "--chart-color-palette": "default"}} href="/">{"Contact"}</a>
      </div>
    </footer>    </div>
  );
};

export default TodolistDetail;
