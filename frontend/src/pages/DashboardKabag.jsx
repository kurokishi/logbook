import { useEffect, useState } from 'react'


export default function DashboardKabag() {
const [period, setPeriod] = useState('monthly')
const [data, setData] = useState(null)


useEffect(() => {
api.get(`/dashboard/kabag?period=${period}`)
.then(res => setData(res.data))
.catch(() => alert('Gagal memuat data dashboard'))
}, [period])


if (!data) return <p className="loading">Loading dashboard...</p>


return (
<div className="container">
<h1>Dashboard Kepala Bagian</h1>


<div className="filter">
<label>Periode Laporan:</label>
<select value={period} onChange={e => setPeriod(e.target.value)}>
<option value="monthly">Bulanan</option>
<option value="quarterly">Triwulan</option>
<option value="semester">Semester</option>
</select>
</div>


<div className="cards">
<div className="card">Total Tiket<br /><strong>{data.total_tickets}</strong></div>
<div className="card success">Selesai Tepat Waktu<br /><strong>{data.on_time}</strong></div>
<div className="card danger">Terlambat<br /><strong>{data.late}</strong></div>
<div className="card">SLA<br /><strong>{data.sla_compliance}%</strong></div>
</div>


<h3>Rekap Per Kategori</h3>
<table>
<thead>
<tr>
<th>Kategori</th>
<th>Total</th>
<th>On Time</th>
<th>Late</th>
</tr>
</thead>
<tbody>
{data.by_category.map(row => (
<tr key={row.category}>
<td>{row.category}</td>
<td>{row.total}</td>
<td>{row.on_time}</td>
<td>{row.late}</td>
</tr>
))}
</tbody>
</table>


<div className="lock">
{data.locked
? '🔒 Periode laporan sudah dikunci'
: '🟢 Periode masih terbuka'}
</div>
</div>
)
}
