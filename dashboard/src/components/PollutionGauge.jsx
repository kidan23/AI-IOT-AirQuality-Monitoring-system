const PollutionGauge = ({ value }) => {

  return (
    <div className="card">
      <h2>Pollution Index</h2>

      <h1>{value.toFixed(2)}</h1>
    </div>
  )
}

export default PollutionGauge
