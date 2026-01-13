import { useEffect, useState } from 'react'
import api from '../services/api'

export default function DashboardKabag() {
  const [period, setPeriod] = useState('monthly')
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)

  // ==============================
  // LOAD DATA DASHBOARD
  // ==============================
  useEffect(() => {
    setLoading(true)
    api
      .get(`/dashboard/kabag?period=${period}`)
      .then(res => setData(res.data))
      .catch(() => alert('Gagal memuat data dashboard'))
      .finally(() => setLoading(false))
  }, [period])

  // ==============================
  // EXPORT EXCEL e-KINERJA
  // ==============================
  const handleExportEkinerja = () => {
    const apiUrl = import.meta.env.VITE_API_URL
    const url = `${apiUrl}/export/ekinerja?period=${period}`
    window.open(url, '_blank')
  }

  // ==============================
  // RENDER
  // ==============================
  if (loading) {
    return <p style={{ padding: 40 }}>Loading dashboard...</p>
  }

  return (
    <div className="container">
      <h1>Dashboard Kepala Bagian</h1>

      {/* ===================== FILTER PERIODE ===================== */}
      <div className="filter">
        <label>Periode Laporan:&nbsp;</label>
        <select
          value={period}
          onChange={e => setPeriod(e.target.value)}
        >
          <option value="monthly">Bulanan</option>
          <option value="quarterly">Triwulan</option>
          <option value="semester">Semester</option>
        </select>
      </div>

      {/* ===================== EXPORT BUTTON ===================== */}
      <div style={{ marginBottom: 20 }}>
        <button
          onClick={handleExportEkinerja}
          style={{
            padding: '10px 16px',
            backgroundColor: '#2563eb',
            color: 'white',
            border: 'none',
            borderRadius: 6,
            cursor: 'pointer',
            fontWeight: 'bold'
          }}
        >
          📥 Export Excel e-Kinerja
        </button>
      </div>

      {/* ===================== SUMMARY CARDS ===================== */}
      <div className="cards">
        <div className="card">
          Total Tiket
          <br />
          <strong>{data.total_tickets}</strong>
        </div>

        <div className="card success">
          Selesai Tepat Waktu
          <br />
          <strong>{data.on_time}</strong>
        </div>

        <div className="card danger">
          Terlambat
          <br />
          <strong>{data.late}</strong>
        </div>

        <div className="card">
          SLA Compliance
          <br />
          <strong>{data.sla_compliance}%</strong>
        </div>
      </div>

      {/* ===================== TABLE PER KATEGORI ===================== */}
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

      {/* ===================== LOCK STATUS ===================== */}
      <div className="lock" style={{ marginTop: 16 }}>
        {data.locked
          ? '🔒 Periode laporan sudah dikunci (final)'
          : '🟢 Periode masih terbuka'}
      </div>
    </div>
  )
}
