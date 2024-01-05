import React from 'react';
import Header from './Header.jsx';
import Footer from './Footer.jsx';
import Logout from './Logout.jsx';
import '../styles/InitGame.css';

const InitGame = ({ onViewChange, isLoggedIn, onLogout, authenticatedUser }) => {
  const handlePlayGame = () => {
    onViewChange("menu");
  };

  const handleViewRules = () => {
    onViewChange("rules");
  };

  const handleViewAbout = () => {
    onViewChange("about");
  };

  return (
    <div className="init-render">
      <Header onViewChange={onViewChange} isLoggedIn={isLoggedIn} authenticatedUser={authenticatedUser} /> 
      <div className="video">      
        <video className='video-init' autoPlay muted loop playsInline>
          <source src="/video.mp4" type="video/mp4"/>
        </video>
      </div> 
      <button className='button-play-game' onClick={handleViewRules}>GAME RULES</button>
      <button
        className={`button-play-game ${isLoggedIn ? '' : 'disabled'}`}
        onClick={handlePlayGame}
        disabled={!isLoggedIn}
      >
        PLAY GAME
      </button>
      <button className='button-play-game' onClick={handleViewAbout}>ABOUT GAME</button>
      {isLoggedIn && <Logout isLoggedIn={isLoggedIn} onLogout={onLogout} onViewChange={onViewChange} />}
      <Footer onViewChange={onViewChange} /> 
    </div>
  );
};

export default InitGame;
