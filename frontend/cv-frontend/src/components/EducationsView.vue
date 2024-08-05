<template>
    <div>
      <h1>Educations</h1>
      <ul v-if="filteredEducations.length">
        <li v-for="education in filteredEducations" :key="education.id">
          <h2>{{ education.title }} - {{ education.institution }}</h2>
          <p><strong>Location:</strong> {{ education.location }}</p>
          <p><strong>Dates:</strong> {{ education.start_date }} - {{ education.end_date || 'Present' }}</p>
          <p><strong>Descriptions:</strong></p>
          <ul>
            <li v-for="(description, index) in education.descriptions" :key="index">
              {{ description.description }}
            </li>
          </ul>
        </li>
      </ul>
      <p v-else>No education available.</p>
      <button v-if="!showAll && educations.length > 3" @click="showAll = true">Show All</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        educations: [],
        showAll: false,
      };
    },
    created() {
      this.fetchEducations();
    },
    computed: {
      filteredEducations() {
        return this.showAll ? this.educations : this.educations.slice(0, 3);
      }
    },
    methods: {
      async fetchEducations() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/education/');
          this.educations = response.data;
        } catch (error) {
          console.error(error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  h1 {
    font-size: 2em;
    margin-bottom: 1em;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin-bottom: 1em;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  h2 {
    font-size: 1.5em;
    margin-bottom: 0.5em;
  }
  
  p {
    margin: 0.5em 0;
  }
  
  button {
    margin-top: 1em;
    padding: 0.5em 1em;
    background-color: #ced9e6;
    color: rgb(0, 0, 0);
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #fbfbfb;
  }
  </style>
  