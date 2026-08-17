import axios from 'axios'

const API = axios.create({
  baseURL: 'http://localhost:5000/api'
})

export const getLatestData = () => API.get('/latest')

export const getHistory = () => API.get('/history')

export const getStats = () => API.get('/stats')