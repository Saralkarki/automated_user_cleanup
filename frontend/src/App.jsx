import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [reports, setReports] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [triggering, setTriggering] = useState(false)

  const fetchReports = async () => {
    try {
      setLoading(true)
      const response = await fetch('/api/reports/latest/')
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      const data = await response.json()
      setReports([data]) // Wrap single report in array
      setError(null)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const triggerCleanup = async () => {
    try {
      setTriggering(true)
      const response = await fetch('/api/cleanup/trigger/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]')?.value || ''
        }
      })
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      await fetchReports() // Refresh data
    } catch (err) {
      setError(err.message)
    } finally {
      setTriggering(false)
    }
  }

  useEffect(() => {
    fetchReports()
  }, [])

  if (loading) {
    return (
      <div className="container">
        <h1>Cleanup Reports Dashboard</h1>
        <p className="loading">Loading cleanup reports...</p>
      </div>
    )
  }

  if (error) {
    return (
      <div className="container">
        <h1>Cleanup Reports Dashboard</h1>
        <p className="error">Error: {error}</p>
      </div>
    )
  }

  return (
    <div className="container">
      <h1>Cleanup Reports Dashboard</h1>
      {reports.length > 0 ? (
        <table className="table">
          <thead>
            <tr>
              <th>Report ID</th>
              <th>Timestamp</th>
              <th>Users Deleted</th>
              <th>Active Users Remaining</th>
            </tr>
          </thead>
          <tbody>
            {reports.map(report => (
              <tr key={report.id}>
                <td>{report.id}</td>
                <td>{new Date(report.timestamp).toLocaleString()}</td>
                <td>{report.users_deleted}</td>
                <td>{report.active_users_remaining}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No reports available</p>
      )}
      <button 
        className="btn btn-primary" 
        onClick={triggerCleanup}
        disabled={triggering}
        style={{ marginTop: '20px' }}
      >
        {triggering ? 'Triggering...' : 'Trigger Manual Cleanup'}
      </button>
    </div>
  )
}

export default App
