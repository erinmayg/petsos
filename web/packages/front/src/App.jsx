import React, { useState, useEffect } from "react";
import LoginPage from "./components/LoginPage";
import SignUpPage from "./components/SignUpPage";
import SearchSitters from "./components/SearchSitters";
import Nav from "./components/Nav"
import Landing from "./components/landing/Landing"
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

function App() {
  const [foo, setFoo] = useState('N/A');
  useEffect(() => {
    fetch('/api/foo')
      .then((res) => res.json())
      .then((data) => setFoo(data.foo))
      .catch((err) => setFoo(err.message));
  }, []);
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path="/signup">
            <SignUpPage />
          </Route>

          <Route exact path="/login">
            <LoginPage />
          </Route>

          <Route exact path="/searchsitters">
            <SearchSitters />
          </Route>

          <Route exact path="/">
            <Nav />
            <Landing />
          </Route>
          
        </Switch>
      </Router>
    </div>
  );
}

export default App;