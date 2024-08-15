import { useState } from 'react'
import CheckboxList from './checkBoxList'
import './styles.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>Checkboxes here.</h1>
      <CheckboxList/>
    </>
  )
}

export default App
