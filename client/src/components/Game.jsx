import React, { useState, useEffect, memo } from 'react';
import {
  TransformWrapper,
  TransformComponent,
  useControls
} from "react-zoom-pan-pinch";
import Board from "./Board.jsx";
import { useGame } from "./GameContext";
import './Game.css';

const ControlsZoom = () => {
  const { zoomIn, zoomOut, resetTransform } = useControls();
  return (
    <>
      <button onClick={() => zoomIn()}>🔍+</button>
      <button onClick={() => zoomOut()}>🔍-</button>
      <button onClick={() => resetTransform()}>Reset</button>
    </>
  );
};

const ControlsAdvance = memo(({ onPause, onBack, isPaused }) => {
  return (
    <>
      <button onClick={onPause}>{ isPaused ? 'Play' : 'Pause' }</button> 
      <button onClick={onBack}>Back</button>
    </>
  );
});

const Game = ({onViewChange}) => {

  //Tamaño del tablero
  const [boardSize, setBoardSize] = useState(20);

  //Estado del tablero
  const [boardState, setBoardState] = useState([]);

  //Estado de la simulación
  const [isPaused, setPaused] = useState(false);
  
  //Estado ganador
  const [winner, setWinner] = useState(null);

  //Estado distritos
  const [liveTribute, setLiveTribute] = useState([]);
  
  // Salud de cada distrito
  const [healthDistrict, setHealthDistrict] = useState([]); 

  // Salud del distrito 0
  const [healthDistrict0, setHealthDistrict0] = useState(0);

  //Estado del juego
  const [gameInitialized, setGameInitialized] = useState(false);

  //Estado para regular el fetch
  const [fetchGameData, setFetchGameData] = useState(true);

  //Estado para obtener el id del juego actual, se obtiene de un contexto
  const { gameID, setGameID } = useGame();

  //Estado para obtener la apariencia del distrito ganador
  const { setWinnerCharacter } = useGame();

  const [speed, setSpeed] = useState(1);

  const handleSpeedChange = (event) => {
    const newSpeed = parseFloat(event.target.value);
    setSpeed(newSpeed);
  };

  const SpeedSlider = ({ speed, handleSpeedChange }) => {
    return (
      <div className="speed-slider">
      <div htmlFor="speed">Speed: {speed}</div>
      <input
        type="range"
        id="speed"
        name="speed"
        min="0.5"
        max="5"
        step="0.1"
        value={speed}
        onChange={handleSpeedChange}
        style={{
          width: '80%', // Modifica el ancho del control deslizante
          margin: '0 auto', // Centra el control deslizante horizontalmente
          padding: '5px', // Añade un espacio alrededor del control deslizante
          cursor: 'pointer', 
        }}
      />
    </div>
    );
  };

  // Pone pausa o reanuda la simulación
  const handlePause = () => {
    setPaused(!isPaused); 
  };

  const handleFinish = () => {
    setGameID(null);
    onViewChange("finish");
  }

  const handleBackToMenu = () => {
    setGameID(null);
    onViewChange("menu");
  }

  // Tablero vacío
  const emptyBoard = Array.from({ length: boardSize }, () => Array(boardSize).fill('  '));
  
  // Crea un juego
  const initialBoard = async () => {
    const response = await fetch(`http://localhost:5000/game/${gameID}`, {
      method: 'PUT',
    });

    if (response.ok) {
      const data = await response.json();
      const gameData = data[gameID];
      const health = data['health'];

      if (gameData && gameData.board) {
        setBoardState(gameData.board.board);
        setBoardSize(gameData.board.rows);
        setHealthDistrict(health); // seteo la salud de todos los distritos
        setHealthDistrict0(health[0]); // seteo la salud del distrito 0
      } else {
        console.error('La estructura de datos es incorrecta:', data);
      }
    } else {
      console.error('Error al finalizar el juego');
    }
    setGameInitialized(true);
    setPaused(true);
  }
  
  // Actualiza el juego creado 
  const fetchGameInfo = async () => {
    try {
      if (fetchGameData && winner === null && gameInitialized) {
        const response = await fetch(`http://localhost:5000/game/${gameID}`, {
          method: 'GET',
        });
        if (response.ok) {
          const data = await response.json();
          const gameData = data[gameID];
          const pause = data['pause'];
          const health = data['health'];
          setLiveTribute(pause);
          setHealthDistrict(health);
          setBoardState(gameData.board.board);
          
          if (gameData.winner !== null) {
            setGameID(null);
            setWinner(gameData.winner);
            setWinnerCharacter(gameData.winner);
            setFetchGameData(false);
          }
        }
      }
    } catch (error) {
      console.error("Error fetching game information:", error);
    }
  };
 
  // Crea un juego si es necesario y se encarga de actualizarlo cada cierto intervalo
  useEffect(() => {
    let timeInterval;

    const updateTimeInterval = () => {
      clearInterval(timeInterval);
      timeInterval = setInterval(() => {
        if (!isPaused) {
          fetchGameInfo();
        }
      }, 1000 / speed);
    };

    if (gameID !== null && !gameInitialized) {
      initialBoard();
    }

    if (!fetchGameData) {
      handleFinish();
    }

    updateTimeInterval(); // Establecer el intervalo inicial

    return () => {
      clearInterval(timeInterval);
    };
  }, [gameID, isPaused, gameInitialized, winner, speed]);

  return (
    <main className="game">
      <div className="game-container">
        <div className="health-section">
          <h2>Health Districts</h2>
            {healthDistrict.map((health, index) => (
              <div key={index} className="health-bar-container">
                <p>District {index}</p>
                <div className="health-bar">
                  <div className="health-progress" style={{ width: `${Math.max(index === 0 ? (health / healthDistrict0) * 100 : (health / 200) * 100,  0)}%` }}>
                    <span className="health-value">{health}</span>
                  </div>
                </div>
              </div>
            ))}
        </div>  
      {liveTribute.length !== 0 && isPaused && (
                <div className="ventana-emergente-container">
                    <div className="ventana-emergente" onClick={handlePause}>
                        <div className="overlay"></div>
                        <h2>¡PAUSE!</h2>
                        {liveTribute.map((elemento, index) => (
                          <p key={index}>District {index} : {elemento} lives</p>
                        ))}
                    </div>
                </div>
            )}
        <TransformWrapper minScale={0.5}>
          <div className="button-section left">
            <SpeedSlider speed={speed} handleSpeedChange={handleSpeedChange} />
            <ControlsZoom />
          </div>
          <TransformComponent>
            <section className="board">
              {!gameInitialized ? (
                <Board boardSize={boardSize} boardState={emptyBoard} />
              ) : (
                <Board size={boardSize} boardState={boardState} />
              )}
            </section>
          </TransformComponent>
        </TransformWrapper>
        <div className="button-section right">
          <ControlsAdvance onPause={handlePause} onBack={handleBackToMenu} isPaused={isPaused} />
        </div>
      </div>
    </main>
  );
};

export default Game;
