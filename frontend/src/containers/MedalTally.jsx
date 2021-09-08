import axios from 'axios';
import React, {useState, useEffect} from 'react';

const MedalTally = () => {
  const [medals, setMedals] = useState([]);

  useEffect(() => {
      axios.get('http://localhost:8000/api/v1/medals')
      .then(res => setMedals(res.data))
      .catch(err => console.log(err));
  } , []);  

  return ( <div>
    <h1>Medal Tally</h1>
    {medals.map(medal => <div key={medal.id}>{medal.medal_type}</div>)}
  </div> );
}
 
export default MedalTally;
