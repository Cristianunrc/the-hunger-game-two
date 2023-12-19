import {useEffect} from 'react';
import { useGame } from "./GameContext";

const Tribute0Walk1 = "/board-images/characters/fallenAngelWalk0.png";
const Tribute1Walk1 = "/board-images/characters/orcoWalk1.png";
const Tribute2Walk1 = "/board-images/characters/minotauroWalk2.png";
const Tribute3Walk1 = "/board-images/characters/reaperManWalk3.png";
const Tribute4Walk1 = "/board-images/characters/golemWalk4.png";
const Tribute5Walk1 = "/board-images/characters/goblinWalk5.png";
const TributeNWalk1 = "/board-images/characters/fallenAngelWalkNeutral.png";

const CharacterImages = [
  Tribute0Walk1,
  Tribute1Walk1,
  Tribute2Walk1,
  Tribute3Walk1,
  Tribute4Walk1,
  Tribute5Walk1
]

const renderTributeImage = (selectedTribute, characters) => {  
  const result = [];
  for (let i = 0; i < characters.length; i++) {
    result.push(characters[(parseInt(selectedTribute) + i) % characters.length]);
  }
  return result;
};

const Characters = () => {
  const { selectedCharacter, setCharacters, setNeutralCharacter, setCharactersOrdered} = useGame();

  useEffect(() => {
    const tributeImages = renderTributeImage(selectedCharacter, CharacterImages)
    setCharacters(tributeImages);
    setNeutralCharacter(TributeNWalk1);
    setCharactersOrdered(CharacterImages);
  }, [selectedCharacter, setCharacters, setNeutralCharacter, setCharactersOrdered]);

  return null;
};

export default Characters;
