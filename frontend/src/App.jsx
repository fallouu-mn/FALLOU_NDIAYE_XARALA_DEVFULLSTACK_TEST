import { Routes, Route } from 'react-router-dom'
import BootcampList from './components/BootcampList'
import BootcampDetail from './components/BootcampDetail'
import AdminDashboard from './components/AdminDashboard'

function App() {
  return (
    <Routes>
      <Route path="/" element={<BootcampList />} />
      <Route path="/bootcamps/:id" element={<BootcampDetail />} />
      <Route path="/admin" element={<AdminDashboard />} />
    </Routes>
  )
}

export default App