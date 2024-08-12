<template>
  <div class="experience">
    
    <div class="image-container">
      <img src="http://127.0.0.1:8000/static/cv_icons/noos.png" alt="Experience Icon" class="experience-image"/>
    </div>

    <h1>Experiences</h1>
    <ul v-if="filteredExperiences.length">
      <li v-for="experience in filteredExperiences" :key="experience.id">
        <div class="experience-header">
          <h2>{{ experience.title }} - {{ experience.company }}</h2>
          <p>
            <span class="location">{{ experience.location }}</span> - 
            {{ experience.start_date }} - {{ experience.end_date || 'Present' }}
          </p>
        </div>
        <ul>
          <li v-for="(description, index) in experience.descriptions" :key="index" v-html="description.description"></li>
        </ul>
      </li>
    </ul>
    <p v-else>No experiences available.</p>
    <button v-if="!showAll && experiences.length > 3" @click="showAll = true">Show All</button>
  </div>
</template>



<script>
import axios from 'axios';

export default {
  data() {
    return {
      experiences: [],
      showAll: false,
    };
  },
  created() {
    this.fetchExperiences();
  },
  computed: {
    filteredExperiences() {
      return this.showAll ? this.experiences : this.experiences.slice(0, 3);
    }
  },
  methods: {
    async fetchExperiences() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/experience/');
        this.experiences = response.data;
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>


<style scoped>
.experience {
  margin: 0 10%;
  padding: 1em;
}

.experience-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.location {
  font-weight: bold;
}

/* Main title styling */
h1 {
  font-size: 1.8em; /* Match font size with Educations view */
  margin-bottom: 0.5em; /* Reduced margin for compactness */
}

/* Main list styling */
ul {
  list-style-type: none;
  padding: 0;
  margin: 0; /* Remove default margin */
}

/* List item styling for experience entries */
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
