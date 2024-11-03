import React from 'react';
import rulesInfo from './rulesInfo.json';
import '../styles/Rules.css';

const Rules = ({ onViewChange }) => {
  const { title, content } = rulesInfo;
  const handleGoToInitGame = () => onViewChange('init');

  return (
    <div className="rules-container-wrapper">
      <div className="background"></div>
      <div className="rules-container">
        <h2>{title}</h2>
        {content.map((paragraph, index) => (
          <p key={index}>{paragraph}</p>
        ))}
        <button onClick={handleGoToInitGame}>Back to menu</button>
      </div>
    </div>
  );
};

export default Rules;
