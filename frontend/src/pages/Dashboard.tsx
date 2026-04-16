import React from "react";
import { ChartBlock } from "../components/runtime/ChartBlock";
import { TableBlock } from "../components/runtime/TableBlock";
import { MetricCardBlock } from "../components/runtime/MetricCardBlock";

const Dashboard: React.FC = () => {
  return (
    <div id="qWyJqLGyYzWfFcOlz" style={{"fontFamily": "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif", "minHeight": "100vh", "background": "#f8fafc", "color": "#1e293b", "--chart-color-palette": "default"}}>
    <nav id="idcnd" className="assistant-nav-header" style={{"height": "64px", "padding": "0 32px", "fontFamily": "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif", "position": "sticky", "top": "0", "zIndex": 50, "display": "flex", "background": "#ffffff", "borderBottom": "1px solid #e2e8f0", "boxShadow": "0 1px 3px rgba(0,0,0,0.06)", "--chart-color-palette": "default", "justifyContent": "space-between", "alignItems": "center"}}>
      <p id="ii626" style={{"fontSize": "1.25rem", "fontWeight": "700", "letterSpacing": "-0.01em", "color": "#0f172a", "--chart-color-palette": "default"}}>{"ToDoList App"}</p>
      <div id="ifqwm" style={{"display": "flex", "--chart-color-palette": "default", "alignItems": "center", "gap": "4px"}}>
        <a id="ih3kq" style={{"padding": "8px 16px", "fontSize": "0.9rem", "fontWeight": "500", "textDecoration": "none", "transition": "all 0.2s", "background": "transparent", "color": "#64748b", "borderRadius": "8px", "--chart-color-palette": "default"}} href="/home" {...{"data-navigate-to": "home"}}>{"Home"}</a>
        <a id="i9t6i" style={{"padding": "8px 16px", "fontSize": "0.9rem", "fontWeight": "600", "textDecoration": "none", "transition": "all 0.2s", "background": "#eff6ff", "color": "#2563eb", "borderRadius": "8px", "--chart-color-palette": "default"}} href="/dashboard" {...{"data-navigate-to": "dashboard"}}>{"Dashboard"}</a>
        <a id="itd5g" style={{"padding": "8px 16px", "fontSize": "0.9rem", "fontWeight": "500", "textDecoration": "none", "transition": "all 0.2s", "background": "transparent", "color": "#64748b", "borderRadius": "8px", "--chart-color-palette": "default"}} href="/todolist-detail" {...{"data-navigate-to": "todolist-detail"}}>{"ToDoList Detail"}</a>
        <a id="i8pjc" style={{"padding": "8px 16px", "fontSize": "0.9rem", "fontWeight": "500", "textDecoration": "none", "transition": "all 0.2s", "background": "transparent", "color": "#64748b", "borderRadius": "8px", "--chart-color-palette": "default"}} href="/user-profile" {...{"data-navigate-to": "user-profile"}}>{"User Profile"}</a>
      </div>
    </nav>
    <section id="i39kd" className="assistant-hero" style={{"padding": "64px 48px", "margin": "24px", "textAlign": "center", "background": "linear-gradient(135deg, #1e3a5f 0%, #2563eb 100%)", "color": "#ffffff", "borderRadius": "16px", "--chart-color-palette": "default"}}>
      <h1 id="i37zm" style={{"margin": "0 0 16px 0", "fontSize": "2.25rem", "lineHeight": "1.2", "fontWeight": "800", "letterSpacing": "-0.02em", "--chart-color-palette": "default"}}>{"Your Task Overview"}</h1>
      <p id="il0hg" style={{"margin": "0 auto 28px auto", "fontSize": "1.1rem", "lineHeight": "1.6", "maxWidth": "600px", "opacity": "0.9", "--chart-color-palette": "default"}}>{"Quickly see your lists and tasks status at a glance."}</p>
      <button id="ipbj4" className="assistant-cta" style={{"padding": "12px 28px", "fontSize": "1rem", "fontWeight": "600", "cursor": "pointer", "background": "#ffffff", "color": "#2563eb", "borderRadius": "10px", "border": "none", "boxShadow": "0 2px 8px rgba(0,0,0,0.15)", "--chart-color-palette": "default"}}>{"Continue"}</button>
    </section>
    <main id="ina4j" className="assistant-main" style={{"padding": "24px 16px", "margin": "0 auto", "maxWidth": "1200px", "--chart-color-palette": "default"}}>
      <section id="ihilc" className="assistant-stats-grid" style={{"margin": "12px 24px", "display": "grid", "--chart-color-palette": "default", "gap": "16px", "gridTemplateColumns": "repeat(3, 1fr)"}}>
        <h2 id="izlom" style={{"margin": "0 0 4px 0", "fontSize": "1.25rem", "fontWeight": "700", "color": "#0f172a", "--chart-color-palette": "default"}}>{"Key Metrics"}</h2>
        <MetricCardBlock id="iuodc" styles={{"width": "100%", "minHeight": "140px", "--chart-color-palette": "default"}} metric={{"metricTitle": "Total Lists", "format": "number", "valueColor": "#2c3e50", "valueSize": 32, "showTrend": true, "positiveColor": "#27ae60", "negativeColor": "#e74c3c", "value": 0, "trend": 12}} dataBinding={{"entity": "User", "endpoint": "/user/", "data_field": "userId"}} />
        <MetricCardBlock id="i4h26" styles={{"width": "100%", "minHeight": "140px", "--chart-color-palette": "default"}} metric={{"metricTitle": "Tasks Due Today", "format": "number", "valueColor": "#2c3e50", "valueSize": 32, "showTrend": true, "positiveColor": "#27ae60", "negativeColor": "#e74c3c", "value": 0, "trend": 12}} dataBinding={{"entity": "User", "endpoint": "/user/", "data_field": "userId"}} />
        <MetricCardBlock id="iutbk" styles={{"width": "100%", "minHeight": "140px", "--chart-color-palette": "default"}} metric={{"metricTitle": "Completed Tasks This Week", "format": "number", "valueColor": "#2c3e50", "valueSize": 32, "showTrend": true, "positiveColor": "#27ae60", "negativeColor": "#e74c3c", "value": 0, "trend": 12}} dataBinding={{"entity": "User", "endpoint": "/user/", "data_field": "userId"}} />
      </section>
      <section id="icj0c" className="assistant-two-column" style={{"margin": "12px 24px", "display": "grid", "--chart-color-palette": "default", "gap": "20px", "gridTemplateColumns": "1fr 1fr"}}>
        <h2 id="iuwsl" style={{"margin": "0 0 8px 0", "fontSize": "1.35rem", "fontWeight": "700", "color": "#0f172a", "--chart-color-palette": "default"}}>{"ToDoLists Overview"}</h2>
        <section id="iv1gz" className="assistant-card" style={{"padding": "28px", "margin": "0", "background": "#ffffff", "borderRadius": "14px", "border": "1px solid #f1f5f9", "boxShadow": "0 1px 4px rgba(0,0,0,0.06)", "--chart-color-palette": "default"}}>
          <h2 id="ip8t2" style={{"margin": "0 0 16px 0", "fontSize": "1.25rem", "fontWeight": "700", "color": "#0f172a", "--chart-color-palette": "default"}}>{"Your ToDoLists"}</h2>
          <TableBlock id="idhxc" styles={{"width": "100%", "margin": "12px 0", "minHeight": "300px", "borderRadius": "12px", "--chart-color-palette": "default"}} title="Your ToDoLists" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Listid", "column_type": "field", "field": "listId", "type": "str", "required": true}, {"label": "Title", "column_type": "field", "field": "title", "type": "str", "required": true}, {"label": "Description", "column_type": "field", "field": "description", "type": "str", "required": true}, {"label": "Createdat", "column_type": "field", "field": "createdAt", "type": "date", "required": true}, {"label": "Updatedat", "column_type": "field", "field": "updatedAt", "type": "date", "required": true}], "formColumns": [{"column_type": "field", "field": "listId", "label": "listId", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "title", "label": "title", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "description", "label": "description", "type": "str", "required": false, "defaultValue": null}, {"column_type": "field", "field": "createdAt", "label": "createdAt", "type": "date", "required": true, "defaultValue": null}, {"column_type": "field", "field": "updatedAt", "label": "updatedAt", "type": "date", "required": false, "defaultValue": null}, {"column_type": "lookup", "path": "user", "field": "user", "lookup_field": "userId", "entity": "User", "type": "str", "required": true}, {"column_type": "lookup", "path": "task", "field": "task", "lookup_field": "taskId", "entity": "Task", "type": "list", "required": false}]}} dataBinding={{"entity": "ToDoList", "endpoint": "/todolist/"}} />
        </section>
        <section id="ieh2y" className="assistant-card" style={{"padding": "28px", "margin": "0", "background": "#ffffff", "borderRadius": "14px", "border": "1px solid #f1f5f9", "boxShadow": "0 1px 4px rgba(0,0,0,0.06)", "--chart-color-palette": "default"}}>
          <h2 id="ib8ek" style={{"margin": "0 0 16px 0", "fontSize": "1.25rem", "fontWeight": "700", "color": "#0f172a", "--chart-color-palette": "default"}}>{"Tasks Status Distribution"}</h2>
          <ChartBlock id="ij85g" styles={{"width": "100%", "margin": "12px 0", "minHeight": "400px", "borderRadius": "12px", "--chart-color-palette": "default"}} chartType="bar-chart" title="Tasks Status Distribution" color="#3498db" chart={{"barWidth": 30, "orientation": "vertical", "showGrid": true, "showLegend": true, "showTooltip": true, "stacked": false, "animate": true, "legendPosition": "top", "gridColor": "#e0e0e0", "barGap": 4}} series={[{"name": "Taskid", "label": "Taskid", "color": "#3498db", "dataSource": "task", "endpoint": "/task/", "labelField": "taskId", "dataField": "taskId"}]} />
        </section>
      </section>
    </main>
    <footer id="ixyxj" className="assistant-footer" style={{"padding": "32px 48px", "fontFamily": "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif", "marginTop": "24px", "display": "flex", "background": "#0f172a", "color": "#94a3b8", "--chart-color-palette": "default", "justifyContent": "space-between", "alignItems": "center"}}>
      <div id="Component_2">
        <div id="i4985" style={{"fontSize": "1.1rem", "fontWeight": "700", "marginBottom": "4px", "color": "#ffffff", "--chart-color-palette": "default"}} />
        <div id="i4bbu" style={{"fontSize": "0.8rem", "--chart-color-palette": "default"}} />
      </div>
      <div id="itr8v" style={{"display": "flex", "--chart-color-palette": "default", "gap": "20px"}}>
        <a id="i1arl" style={{"fontSize": "0.85rem", "textDecoration": "none", "transition": "color 0.2s", "color": "#94a3b8", "--chart-color-palette": "default"}} href="/">{"Privacy"}</a>
        <a id="ieq0l" style={{"fontSize": "0.85rem", "textDecoration": "none", "transition": "color 0.2s", "color": "#94a3b8", "--chart-color-palette": "default"}} href="/">{"Terms"}</a>
        <a id="ioopv" style={{"fontSize": "0.85rem", "textDecoration": "none", "transition": "color 0.2s", "color": "#94a3b8", "--chart-color-palette": "default"}} href="/">{"Contact"}</a>
      </div>
    </footer>    </div>
  );
};

export default Dashboard;
