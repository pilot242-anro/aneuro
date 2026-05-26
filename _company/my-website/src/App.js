import React, { useState } from 'react';
import './App.css';

function App() {
  const [tarotCard, setTarotCard] = useState('');
  const tarotCards = [
    'The Fool',
    'The Magician',
    'The High Priestess',
    'The Empress',
    'The Emperor',
    'The Hierophant',
    'The Lovers',
    'The Chariot',
    'Strength',
    'The Hermit',
    'Wheel of Fortune',
    'Justice',
    'The Hanged Man',
    'Death',
    'Temperance',
    'The Devil',
    'The Tower',
    'The Star',
    'The Moon',
    'The Sun',
    'Judgment',
    'The World'
  ];

  const drawTarotCard = () => {
    const randomIndex = Math.floor(Math.random() * tarotCards.length);
    setTarotCard(tarotCards[randomIndex]);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>4주 보는 4주 프리, 타로카드, 타로카드 보는 사이트</h1>
        <button onClick={drawTarotCard}>타로 카드 뽑기</button>
        {tarotCard && <h2>당신의 타로 카드는: {tarotCard}</h2>}
      </header>
    </div>
  );
}

export default App;