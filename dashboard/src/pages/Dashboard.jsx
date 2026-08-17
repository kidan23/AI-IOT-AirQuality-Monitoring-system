import { useEffect, useState } from 'react'
import { getLatestData, getHistory } from '../services/api'

import SensorCard from '../components/SensorCard'
import AlertCard from '../components/AlertCard'
import PollutionGauge from '../components/PollutionGauge'
import LineChartComponent from '../components/LineChartComponent'

const Dashboard = () => {

  const [latest, setLatest] = useState(null)
  const [history, setHistory] = useState([])

  const fetchData = async () => {
    try {
      const latestRes = await getLatestData()
      const historyRes = await getHistory()

      setLatest(latestRes.data)
      setHistory(historyRes.data)

    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {

    fetchData()

    const interval = setInterval(fetchData, 5000)

    return () => clearInterval(interval)

  }, [])

  return (
    <div className="dashboard-container">

      <h1>AI Air Quality Dashboard</h1>

      {latest && (
        <>
          <div className="top-grid">
            <SensorCard data={latest} />
            <AlertCard data={latest} />
            <PollutionGauge value={latest.pollution_index} />
          </div>

          <LineChartComponent data={history} />
        </>
      )}

    </div>
  )
}

export default Dashboard
