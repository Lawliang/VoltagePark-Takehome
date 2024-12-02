import { useState, useEffect } from 'react'
import './App.css'
import logoUrl from './assets/logo.png'
// pages
import Game from './pages/game'
// api
import { createGame, fetchGame } from './api/apiCalls'

function App() {
  const [id, setId] = useState(null)
  const [game, setGame] = useState(null)

  const handleStartGame = async () => {
    const data = await createGame()
    setGame(data)
  }
  
  const handleFetchGame = async (id) => {
    const data = await fetchGame(id)
    setGame(data)
  }

  return (
    <>
      <div className="flex flex-col items-center">
        <img className="w-96" src={logoUrl}/>
      <div className="flex flex-col gap-6 p-10 bg-[#e7e1dc] rounded-xl">
        <button 
          onClick={handleStartGame}
          className="bg-green-500 text-white py-2 px-4 rounded-lg shadow-md hover:bg-green-600 transition duration-300">
            { game ? "Reset" : "Start new game"}
        </button>
        <div className="flex gap-3 items-center">
          <input 
            placeholder="Enter game ID" 
            onChange={(e) => setId(e.target.value)}
            className="border border-slate-300 p-2 rounded-xl focus:outline-none focus:ring-1 focus:ring-purple-400 transition duration-300"/>
          <button 
            onClick={() => handleFetchGame(id)}
            className="bg-green-400 text-white py-2 px-4 rounded-lg shadow-md hover:bg-green-500 transition duration-300">
              Fetch game
          </button>
        </div>
        { game
          ? <Game game={game}/>
          : null }
      </div>
      </div>
    </>
  )
}

export default App
