// src/axios.js
import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',  // Replace with your Django backend URL
  timeout: 1000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export default instance;
