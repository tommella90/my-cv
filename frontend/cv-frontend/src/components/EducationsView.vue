<template>
  <div class="education">
    <h1>Educations</h1>
    <ul v-if="filteredEducations.length">
      <li v-for="education in filteredEducations" :key="education.id" class="education-item">
        <div class="education-body">
          <!-- Add the image for the education here -->
          <div class="education-images" v-if="education.images && education.images.length">
            <img v-for="(image, index) in education.images" :key="index" :src="image.image" alt="Education Image" class="education-image" />
          </div>

          <!-- Wrap the education content -->
          <div class="education-content">
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
          </div>
        </div>
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
          const response = await axios.get('http://127.0.0.1:8000/education/');
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
  
  .education-body {
    display: flex; /* Align image and content side by side */
    align-items: flex-start; /* Align items at the top */
    margin-bottom: 1em; /* Space between entries */
  }
  
  .education-images {
    margin-right: 1em; /* Space between image and content */
  }
  
  .education-image {
    width: 100px; /* Set a fixed width for images */
    height: auto; /* Maintain aspect ratio */
    border-radius: 4px; /* Optional: rounded corners */
    border: 1px solid #ddd; /* Optional: border around images */
  }
  
  .education-content {
    flex: 1; /* Allow the content to take up the remaining space */
  }
  
  .education-header {
    margin-bottom: 0.5em;
  }
  
  .location {
    font-weight: bold;
  }
  
  /* Main title styling */
  h1 {
    font-size: 1.8em;
    margin-bottom: 0.5em;
  }
  
  /* Main list styling */
  ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
  }
  
  /* List item styling for education entries */
  li {
    margin-bottom: 0.5em;
    padding: 0.5em;
    border: 1px solid #ddd;
    border-radius: 4px;
    text-align: left;
  }
  
  /* Sub-list styling for descriptions */
  li ul {
    list-style-type: disc;
    margin-left: 1em;
    padding: 0;
  }
  
  li ul li {
    margin-bottom: 0.25em;
    border: none;
    padding: 0;
  }
  
  /* Sub-title styling */
  h2 {
    font-size: 1.4em;
    margin-bottom: 0.25em;
    text-align: left;
  }
  
  /* Paragraph styling */
  p {
    margin: 0.25em 0;
    text-align: left;
  }
  
  /* Button styling */
  button {
    margin-top: 0.5em;
    padding: 0.5em 1em;
    background-color: #ced9e6;
    color: rgb(0, 0, 0);
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.9em;
  }
  
  button:hover {
    background-color: #fbfbfb;
  }
  </style>
  
  