import { useEffect, useState } from 'react'
import { processMove } from '../api/apiCalls'

export default function Game({ game }) {
    const [player, setPlayer] = useState(null);
    const [round, setRound] = useState(null);
    const [board, setBoard] = useState([]);
    const [winner, setWinner] = useState("pending");

    const handleClick = async (index) => {
        try {
            const body = { player, round, index };
            const data = await processMove(game.id, body);
            setPlayer(data.player);
            setRound(data.round);
            setBoard(data.board);
            if (data.winner) {
                setWinner(data.winner);
            }
        } catch (error) {
            console.error("Error processing move:", error);
        }
    };

    useEffect(() => {
        setPlayer(game.player);
        setRound(game.round);
        setBoard(game.board);
        setWinner(game.winner);
    }, [game]);

    return (
        <>
            <div className="font-bold">Round: {round}</div>
            <div className="grid grid-cols-3 grid-rows-3 gap-5 mt-10 max-w-xs mx-auto">
                {board.map((item, index) => (
                    <button
                        key={index}
                        className="flex items-center justify-center h-24 w-24 bg-[#ffe1cd] border-1 border-[#ffc7a1] rounded-md text-2xl font-bold text-gray-800 transition-colors duration-300 ease-in-out hover:bg-[#ffc299] disabled:bg-gray-500"
                        disabled={winner !== "pending"}
                        onClick={() => handleClick(index)}
                    >
                        {item}
                    </button>
                ))}
            </div>
            <div className="text-center mt-5 text-lg font-bold">
                {winner === 'X' && <div>X Wins!</div>}
                {winner === 'O' && <div>O Wins!</div>}
                {winner === 'Tie' && <div>It's a tie!</div>}
            </div>
        </>
    );
}
