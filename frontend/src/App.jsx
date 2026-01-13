import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import DashboardKabag from './pages/DashboardKabag'


export default function App() {
return (
<BrowserRouter>
<Routes>
<Route path="/kabag" element={<DashboardKabag />} />
<Route path="*" element={<Navigate to="/kabag" />} />
</Routes>
</BrowserRouter>
)
}
