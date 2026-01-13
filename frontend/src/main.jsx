import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './App.css'
from routers.report_archive import router as report_router
app.include_router(report_router)

ReactDOM.createRoot(document.getElementById('root')).render(
<React.StrictMode>
<App />
</React.StrictMode>
)
