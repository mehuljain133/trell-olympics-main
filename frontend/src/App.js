import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

import React from "react";
import Home from "./containers/Home";
import MedalTally from "./containers/MedalTally";

const App = () => {
  return (
    <React.Fragment>
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/medal-tally">Medal Tally</Link>
              </li>
            </ul>
          </nav>
          <Switch>
            <Route path="/medal-tally">
              <MedalTally />
            </Route>
            <Route path="/">
              <Home />
            </Route>
          </Switch>
        </div>
      </Router>
    </React.Fragment>
  );
};

export default App;
