import { useState } from 'react'
import BasicTabs from './components/TabComponents'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
     <BasicTabs/>
    </div>
  )
}

export default App
