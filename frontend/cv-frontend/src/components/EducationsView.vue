<template>
  <div class="education">
    <h1>Educations</h1>
    <ul v-if="filteredEducations.length">
      <li v-for="education in filteredEducations" :key="education.id">
        <div class="education-header">
          <h2>{{ education.title }} - {{ education.institution }}</h2>
          <p>
            <span class="location">{{ education.location }}</span> - 
            {{ education.start_date }} - {{ education.end_date || 'Present' }}
          </p>
        </div>
        <ul>
          <li v-for="(description, index) in education.descriptions" :key="index" v-html="description.description">
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
.education {
  margin: 0 10%;
  padding: 1em;
}

.education-header {
  display: flex;
  justify-content: space-between;
  align-items: left;
  margin-bottom: 0.5em;
}

.location {
  font-weight: bold;
}
/* Main title styling */
h1 {
  font-size: 1.8em; /* Slightly smaller font size */
  margin-bottom: 0.em; /* Reduced margin */
}

/* Main list styling */
ul {
  list-style-type: none;
  padding: 0;
  margin: 0; /* Remove default margin */
}

/* List item styling for education entries */
li {
  margin-bottom: 0.5em; /* Reduced margin between list items */
  padding: 0.5em; /* Maintain reduced padding for compactness */
  border: 1px solid #ddd;
  border-radius: 4px;
  text-align: left; /* Left-align text */
}

/* Sub-list styling for descriptions */
li ul {
  list-style-type: disc; /* Show bullet points */
  margin-left: 1em; /* Adjusted indent for compactness */
  padding: 0; /* Remove default padding */
}

li ul li {
  margin-bottom: 0.25em; /* Reduced space between bullets */
  border: none; /* Remove borders */
  padding: 0; /* Remove padding */
}

/* Sub-title styling */
h2 {
  font-size: 1.4em; /* Slightly smaller font size */
  margin-bottom: 0.25em; /* Reduced margin below title */
  text-align: left; /* Left-align title text */
}

/* Paragraph styling */
p {
  margin: 0.25em 0; /* Reduced margin for paragraphs */
  text-align: left; /* Left-align paragraph text */
}

/* Button styling */
button {
  margin-top: 0.5em; /* Reduced top margin */
  padding: 0.5em 1em;
  background-color: #ced9e6;
  color: rgb(0, 0, 0);
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9em; /* Slightly smaller font size */
}

button:hover {
  background-color: #fbfbfb;
}
</style>
