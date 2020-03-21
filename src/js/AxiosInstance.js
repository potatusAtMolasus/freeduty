import axios from "axios";

const instance = axios.create({
  baseURL: 'http://764ef1b1.ngrok.io',       
  headers: {
    'Content-Type': 'application/json',
  }
})

export default instance;