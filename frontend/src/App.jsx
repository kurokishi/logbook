import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import DashboardKabag from './pages/DashboardKabag'
import DashboardDirektur from './pages/DashboardDirektur'


export default function App() {
return (
<BrowserRouter>
<Routes>
<Route path="/kabag" element={<DashboardKabag />} />
<Route path="/direktur" element={<DashboardDirektur />} />
<Route path="*" element={<Navigate to="/kabag" />} />
</Routes>
</BrowserRouter>
)
}
