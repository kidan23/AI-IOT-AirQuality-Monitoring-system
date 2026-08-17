import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from 'recharts'

const LineChartComponent = ({ data }) => {

  return (
    <div className="chart-container">

      <h2>Pollution Trend</h2>

      <ResponsiveContainer width="100%" height={400}>

        <LineChart data={data}>

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="timestamp" />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="pollution_index"
            stroke="#ff0000"
          />

        </LineChart>

      </ResponsiveContainer>

    </div>
  )
}

export default LineChartComponent
