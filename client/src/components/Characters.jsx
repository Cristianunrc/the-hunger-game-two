import {useEffect} from 'react';
import { useGame } from "./GameContext";

// const Tribute0Walk = "/board-images/characters/fallenAngelWalk0.png";
// const Tribute1Walk = "/board-images/characters/orcoWalk1.png";
// const Tribute2Walk = "/board-images/characters/minotauroWalk2.png";
// const Tribute3Walk = "/board-images/characters/reaperManWalk3.png";
// const Tribute4Walk = "/board-images/characters/golemWalk4.png";
// const Tribute5Walk = "/board-images/characters/goblinWalk5.png";
// const TributeNWalk = "/board-images/characters/fallenAngelWalkNeutral.png";

const Tribute0Fight = "/board-images/characters/fallenAngelFight0.png";
const Tribute1Fight = "/board-images/characters/orcoFight1.png";
const Tribute2Fight = "/board-images/characters/minotauroFight2.png";
const Tribute3Fight = "/board-images/characters/reaperManFight3.png";
const Tribute4Fight = "/board-images/characters/golemFight4.png";
const Tribute5Fight = "/board-images/characters/goblinFight5.png";
const TributeNFight = "/board-images/characters/fallenAngelFightNeutral.png";

// const Tribute0Dead = "/board-images/characters/fallenAngelDead0.png";
// const Tribute1Dead = "/board-images/characters/orcoDead1.png";
// const Tribute2Dead = "/board-images/characters/minotauroDead2.png";
// const Tribute3Dead = "/board-images/characters/reaperManDead3.png";
// const Tribute4Dead = "/board-images/characters/golemDead4.png";
// const Tribute5Dead = "/board-images/characters/goblinDead5.png";
// const TributeNDead = "/board-images/characters/fallenAngelDeadNeutral.png";

// const CharacterImages = [
//   Tribute0Walk,
//   Tribute1Walk,
//   Tribute2Walk,
//   Tribute3Walk,
//   Tribute4Walk,
//   Tribute5Walk
// ]

const CharacterImagesWeapons = [
  Tribute0Fight,
  Tribute1Fight,
  Tribute2Fight,
  Tribute3Fight,
  Tribute4Fight,
  Tribute5Fight
]

// const CharacterImagesDeads = [
//   Tribute0Dead,
//   Tribute1Dead,
//   Tribute2Dead,
//   Tribute3Dead,
//   Tribute4Dead,
//   Tribute5Dead
// ]

const renderTributeImage = (selectedTribute, characters) => {  
  const result = [];
  for (let i = 0; i < characters.length; i++) {
    const characterIndex = (parseInt(selectedTribute) + i) % characters.length;
    const tributeImage = characters[characterIndex];
    result.push(tributeImage);
  }
  return result;
};

const Characters = () => {
  const { selectedCharacter, setCharacters, setNeutralCharacter, setCharactersOrdered } = useGame();

  useEffect(() => {
    const tributeImages = renderTributeImage(selectedCharacter, CharacterImagesWeapons);
    
    setCharacters(tributeImages);
    setNeutralCharacter(TributeNFight);
    setCharactersOrdered(CharacterImagesWeapons);
  }, [selectedCharacter, setCharacters, setNeutralCharacter, setCharactersOrdered]);

  return null;
};

export default Characters;
