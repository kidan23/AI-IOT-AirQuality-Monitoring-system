const AlertCard = ({ data }) => {

  return (
    <div className="card">
      <h2>AI Alert</h2>

      <p>{data.alert.message}</p>

      <h3>{data.alert.level}</h3>
    </div>
  )
}

export default AlertCard
