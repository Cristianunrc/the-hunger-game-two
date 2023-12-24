import React, { createContext, useContext, useState } from "react";

const GameContext = createContext();

export const GameProvider = ({ children }) => {
  const [gameID, setGameID] = useState(null);
  const [selectedCharacter, setSelectedCharacter] = useState(null);
  const [winnerCharacter, setWinnerCharacter] = useState(null);
  const [characters, setCharacters] = useState(null);
  const [neutralCharacter, setNeutralCharacter] = useState(null);
  const [charactersOrdered, setCharactersOrdered] = useState(null);
  // const [charactersLife, setCharactersLife] = useState([]);
  // const [weaponsState, setWeaponsState] = useState([]);

  const contextValue = {
    gameID,
    setGameID,
    selectedCharacter,
    setSelectedCharacter,
    winnerCharacter,
    setWinnerCharacter,
    characters,
    setCharacters,
    neutralCharacter,
    setNeutralCharacter,
    charactersOrdered,
    setCharactersOrdered,
    // charactersLife,
    // setCharactersLife,
    // weaponsState,
    // setWeaponsState,
  };

  return (
    <GameContext.Provider value={contextValue}>
      {children}
    </GameContext.Provider>
  );
};

export const useGame = () => {
  return useContext(GameContext);
};
