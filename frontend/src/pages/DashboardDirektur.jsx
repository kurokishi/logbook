import { useEffect, useState } from 'react'
api.get(`/dashboard/direktur?period=${period}`)
.then(res => setData(res.data))
.catch(() => alert('Gagal memuat dashboard direktur'))
}, [period])


if (!data) return <p className="loading">Loading dashboard direktur...</p>


return (
<div className="container">
<h1>Dashboard Direktur</h1>
<p style={{ color: '#555' }}>
Ringkasan strategis kinerja layanan IT RSUD (tanpa detail unit)
</p>


<div className="filter">
<label>Periode:</label>
<select value={period} onChange={e => setPeriod(e.target.value)}>
<option value="monthly">Bulanan</option>
<option value="quarterly">Triwulan</option>
<option value="semester">Semester</option>
</select>
</div>


<div className="cards">
<div className="card">
Total Tiket<br /><strong>{data.total_tickets}</strong>
</div>
<div className="card success">
SLA Compliance<br /><strong>{data.sla_compliance}%</strong>
</div>
<div className="card">
Rata-rata Waktu Penyelesaian<br />
<strong>{data.avg_resolution_hours} jam</strong>
</div>
</div>


<h3>Tren Penyelesaian</h3>
<table>
<thead>
<tr>
<th>Status</th>
<th>Jumlah</th>
</tr>
</thead>
<tbody>
<tr>
<td>Selesai Tepat Waktu</td>
<td>{data.on_time}</td>
</tr>
<tr>
<td>Terlambat</td>
<td>{data.late}</td>
</tr>
</tbody>
</table>


<div className="lock">
{data.locked
? '🔒 Data periode ini telah dikunci (final)'
: '🟢 Data masih berjalan'}
</div>
</div>
)
}
