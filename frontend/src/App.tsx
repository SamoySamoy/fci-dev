import { useState } from "react";
import Modal from "react-modal"; // Import the modal component
import "./App.css";

interface SquareProps {
  value: string | null;
  onSquareClick: () => void;
}
function calculateWinner(squares: (string | null)[]): string | null {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}

function Square({ value, onSquareClick }: SquareProps) {
  return (
    <button
      className="w-16 h-16 text-2xl font-bold border border-gray-400 flex items-center justify-center"
      onClick={onSquareClick}
    >
      {value}
    </button>
  );
}

interface BoardProps {
  xIsNext: boolean;
  squares: (string | null)[];
  onPlay: (squares: (string | null)[]) => void;
}

function Board({ xIsNext, squares, onPlay }: BoardProps) {
  function handleClick(i: number) {
    if (calculateWinner(squares) || squares[i]) {
      return;
    }
    const nextSquares = squares.slice();
    if (xIsNext) {
      nextSquares[i] = "X";
    } else {
      nextSquares[i] = "O";
    }
    onPlay(nextSquares);
  }

  const winner = calculateWinner(squares);
  let status;
  if (winner) {
    status = "Winner: " + winner;
  } else {
    status = "Next player: " + (xIsNext ? "X" : "O");
  }

  return (
    <>
      <div className="mb-4 text-xl font-semibold">{status}</div>
      <div className="grid grid-cols-3 gap-2">
        {squares.map((value, i) => (
          <Square key={i} value={value} onSquareClick={() => handleClick(i)} />
        ))}
      </div>
    </>
  );
}

interface GameState {
  history: (string | null)[][];
  currentMove: number;
}

export default function App() {
  const [history, setHistory] = useState<GameState["history"]>([
    Array(9).fill(null),
  ]);
  const [currentMove, setCurrentMove] = useState<GameState["currentMove"]>(0);
  const [winner, setWinner] = useState<string | null>(null);
  const xIsNext = currentMove % 2 === 0;
  const currentSquares = history[currentMove];

  function handlePlay(nextSquares: (string | null)[]) {
    const nextHistory = [...history.slice(0, currentMove + 1), nextSquares];
    setHistory(nextHistory);
    setCurrentMove(nextHistory.length - 1);
    const calculatedWinner = calculateWinner(nextSquares);
    if (calculatedWinner) {
      setWinner(calculatedWinner);
    }
  }

  function jumpTo(nextMove: number) {
    setCurrentMove(nextMove);
    setWinner(null);
  }

  const moves = history.map((squares, move) => {
    let description;
    if (move > 0) {
      description = "Go to move #" + move;
    } else {
      description = "Go to game start";
    }
    return (
      <li key={move} className="mb-2">
        <button
          className="text-blue-500 hover:underline"
          onClick={() => jumpTo(move)}
        >
          {description}
        </button>
      </li>
    );
  });

  return (
    <div className="flex flex-col items-center p-4">
      <div className="mb-8">
        <Board xIsNext={xIsNext} squares={currentSquares} onPlay={handlePlay} />
      </div>
      <div>
        <ol>{moves}</ol>
      </div>
      <Modal
        isOpen={!!winner}
        onRequestClose={() => setWinner(null)}
        className="modal"
        overlayClassName="overlay"
        style={{
          content: {
            top: "50%",
            left: "50%",
            right: "auto",
            bottom: "auto",
            marginRight: "-50%",
            transform: "translate(-50%, -50%)",
            width: "fit-content",
            padding: "2rem",
            borderRadius: "8px",
            background: "#fff",
            boxShadow: "0px 4px 16px rgba(0, 0, 0, 0.2)",
          },
        }}
      >
        <div className="modal-content">
          <h2>Winner!</h2>
          <p>{winner} has won the game!</p>
          <button onClick={() => setWinner(null)}>Close</button>
        </div>
      </Modal>
    </div>
  );
}
