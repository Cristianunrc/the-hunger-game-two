import {useEffect} from 'react';
import { useGame } from "./GameContext";

const Tribute0Walk1 = "/board-images/characters/fallenAngelFight0.png";
const Tribute1Walk1 = "/board-images/characters/orcoFight1.png";
const Tribute2Walk1 = "/board-images/characters/minotauroFight2.png";
const Tribute3Walk1 = "/board-images/characters/reaperManFight3.png";
const Tribute4Walk1 = "/board-images/characters/golemFight4.png";
const Tribute5Walk1 = "/board-images/characters/goblinFight5.png";
const TributeNWalk1 = "/board-images/characters/fallenAngelFightNeutral.png";

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
