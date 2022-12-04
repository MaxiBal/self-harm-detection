import React from 'react';
import logo from './logo.svg';
import './App.css';

import { w3cwebsocket as W3CWebSocket } from "websocket";

const client = new W3CWebSocket('ws://127.0.0.1:8080')

class App extends React.Component<{}, {message: string}> {

  constructor(props: any) {
    super(props);
    this.state = {message: ''}
  }

  componentWillMount(): void {
      client.onopen = () => {
        console.log("Client Connected");
      }
      client.onmessage = (message) => {
        console.log(message.data);
      }
  }

  handleChange = (event: any) => {
    this.setState({message: event.target.value})
  }

  onClick = (event: any) => {

    let message = this.state.message

    client.send(JSON.stringify({'message': message}))
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1>Self-Harm Detector</h1>
          <p>Enter what somebody wrote and see if they are at risk for self-harm</p>
          <textarea 
            id="message"
            className="textarea"
            name="message"
            onChange={this.handleChange}
            />
          <button onClick={this.onClick}>Send</button>
        </header>
      </div>
    );
  }
}

export default App;
