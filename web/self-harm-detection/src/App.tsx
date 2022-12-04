import React from 'react';
import logo from './logo.svg';
import './App.css';

import { w3cwebsocket as W3CWebSocket } from "websocket";

const client = new W3CWebSocket('ws://127.0.0.1:8080')

class App extends React.Component<{}, {message: string, suicidal: boolean | undefined}> {

  constructor(props: any) {
    super(props);
    this.state = {message: '', suicidal: undefined}
  }

  componentWillMount(): void {
      client.onopen = () => {
        console.log("Client Connected");
      }
      client.onmessage = (message) => {
        console.log(message.data)
        this.setState({suicidal: parseInt(message.data.toString()) === 1})
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
          <p>Enter text and see if you are at risk for self-harm</p>
          <textarea 
            id="message"
            className="textarea"
            name="message"
            onChange={this.handleChange}
            />
          <button onClick={this.onClick}>Send</button>
          <h3>{this.state.suicidal ? "The model predicts that you are at risk of suicide." : "The model predicts you are not at risk of suicide."}</h3>
          
        </header>
      </div>
    );
  }
}

export default App;
