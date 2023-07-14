import React, { useState } from 'react';
import './App.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBasketballBall } from '@fortawesome/free-solid-svg-icons';
import matches from './matches.json';

/* REFER TO DESIGN. */

export default function App() {
  return (
    <>
      <Headed />
      <Predhead />
      <div className="section-divider"></div>
      <div className="bigDiv">
        <PlayerTable players={PLAYERS}/>
        <MatchTable matches={matches} />
      </div>
      <div className="section-divider"></div>
      <Articles />
      <div className="section-divider"></div>
      <AboutSection />
    </>
  );
}

function Headed() {
  return (
    <>
      <header className="PageHeader">
        <h1 className="PageTitle">PHouse<span>Preds</span><FontAwesomeIcon icon={faBasketballBall} className="ballicon"/></h1>
        <nav>
          <ul>
            <li>
              <a href="/" className="links">Predictor</a>
            </li>
            <li>
              <a href="#articles-section" className="links">Articles</a>
            </li>
            <li>
              <a href="#about-section" className="links">About</a>
            </li>
          </ul>
        </nav>
      </header>
    </>
  );
}

function Predhead() {
  const [inputText, setInputText] = useState('');
  const [displayText, setDisplayText] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [id, setID] = useState('');
  const [suggestedName, setSuggestedName] = useState('');
  
  const handleInputChange = (e) => {
    setInputText(e.target.value);
  }

  const handleSubmit = (input = inputText) => {
    setIsSubmitted(true);

    fetch('http://127.0.0.1:5000/convert', { 
      method: 'POST', // or 'GET'
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ inputArray: input })
    })
    .then(response => response.json()) // Convert response to JSON.
    .then(data => {
      setDisplayText(data.message);
      setID(data.id);
      if (data.id === -1) {
        setSuggestedName(data.message.split('"')[1]);
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }

  const handleSuggestion = () => {
    setInputText(suggestedName)
    handleSubmit(suggestedName)
  }

  return (
    <div className="container">
      <div className={`predDiv ${isSubmitted ? 'predDiv-slide-left' : ''}`}>
        <h3 className="predict-head">Predictor</h3>
        <p id="predict-about">Input any current NBA player's name to get projections for their next game!</p>
        <div className="input-area">
          <input className="user-input" placeholder="input a player!" type="text" value={inputText} onChange={handleInputChange}></input>
          {/* Don't want to pass in an event object to handleSubmit, so use arrow function to invoke handleSubmit (no args). */}
          <button className="submit-button" onClick={() => handleSubmit()}>Submit</button>
        </div>
      </div>
      <div className="helloMessage" style={{ opacity: isSubmitted ? '1' : '0', visibility: isSubmitted ? 'visible' : 'hidden' }}>
        <div className="playerInfo">
          <div className="playerImage">
            {(id === -1 || id === 0) ? null : <img src={`https://cdn.nba.com/headshots/nba/latest/260x190/${id}.png`} alt="Player" />}
          </div>
          <div className="playerPrediction">
            <h2>PREDICTED POINTS</h2>
            {displayText}
            {id === -1 ? <button className="yesButton" onClick={handleSuggestion}>Yes</button> : null}
          </div>
        </div>
      </div>
    </div>
  );
}

function PlayerTablePlayers({ player }) {
  return (
    <tr className="player-row" key={player.playerID}>
      <td>{player.name}</td>
      <td>{player.points}</td>
      <td>{player.assists}</td>
      <td>{player.rebounds}</td>
    </tr>
  );
}

function PlayerTable({ players }) {
  return (
    <div className="tablewrapper">
      <h3 className="playerdesc">Best performances from the previous matchday</h3>
      <table className="player-table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Points</th>
            <th>Assists</th>
            <th>Rebounds</th>
          </tr>
        </thead>
        <tbody>
          {players.map(player => (
            <PlayerTablePlayers player={player} key={player.playerID}/>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function MatchRow({match}) {
  return (
    <tr className="match-row">
      <td><img src={match.homeLogo} alt={match.homeTeam} />{match.homeTeam}</td>
      <td><img src={match.awayLogo} alt={match.awayTeam} />{match.awayTeam}</td>
    </tr>
  );
}

function MatchTable({matches}) {
  return (
    <div className="tablewrapper">
      <h3 className="matchdesc">Upcoming matches</h3>
      <table className="match-table">
        <thead>
            <tr>
              <th>Home Team</th>
              <th>Away Team</th>
            </tr>
          </thead>
          <tbody>
            {matches.map((match, index) => (
              <MatchRow match={match} key={index} />
            ))}
          </tbody>
      </table>
    </div>
  );
}

function OneArticle({ articleName }) { /* Can add some more params. */
  return (
    <div className="image-container">
      <a className="image-links" href="#articles-section">
        <img className="article-image" src='steph.png' alt="dame dolla" width="300" height="300" />
        <div className="article-overlay">
          <div className="article-content">
            <h2 className="article-title">{articleName}</h2>
            <p className="article-description">Damian Lillard requests a trade</p>
          </div>
        </div>
      </a>
    </div>
  );
}

function Articles() {
  return (
    <div className="article-wrapper">
      <h1 className="articulo">Articles</h1>
      <div className="article-container">
        <div className="image-container">
          <a className="image-links" href="#articles-section">
            <img className="article-image" src='dame.png' alt="dame dolla" width="300" height="300" />
            <div className="article-overlay">
              <div className="article-content">
                <h2 className="article-title">Dame Time's Up</h2>
                <p className="article-description">Damian Lillard requests a trade</p>
              </div>
            </div>
          </a>
        </div>
        <OneArticle articleName="CURRRYYY"/>
      </div>
    </div>
  );
}

function AboutSection() {
  return (
    <>
      <div>
        <h1 id="about-header">About... Coming Soon</h1>
      </div>
    </>
  );
}


const PLAYERS = [
  {name: "Fruits", playerID: 1, points: 12, rebounds: 5, assists: 5},
  {name: "ok", playerID: 2, points: 12, rebounds: 225, assists: 125},
  {name: "HIM", playerID: 3, points: 12, rebounds: 25, assists: 5},
  {name: "timmy", playerID: 4, points: 22, rebounds: 35, assists: 5},
  {name: "zags", playerID: 5, points: 14, rebounds: 5, assists: 545},
];

const items = [{ name: 'Option 1' }, { name: 'Option 2' }, { name: 'Option 3' }];