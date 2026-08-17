const SensorCard = ({ data }) => {

  return (
    <div className="card">
      <h2>Sensor Reading</h2>

      <p>MQ Value: {data.mq}</p>

      <p>Pollution Index: {data.pollution_index.toFixed(2)}</p>

      <p>Status: {data.label}</p>
    </div>
  )
}

export default SensorCard
