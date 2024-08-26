<template>
  <div class="experience">
    <h1>Experiences</h1>
    <ul v-if="filteredExperiences.length">
      <li v-for="experience in filteredExperiences" :key="experience.id" class="experience-item">
        <div class="experience-body">
          <!-- Add the image for the experience here -->
          <div class="experience-images" v-if="experience.images && experience.images.length">
            <img v-for="(image, index) in experience.images" :key="index" :src="image.image" alt="Experience Image" class="experience-image" />
          </div>

          <!-- Wrap the experience content -->
          <div class="experience-content">
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
          </div>
        </div>
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
        const response = await axios.get('http://127.0.0.1:8000/experience/');
        console.log(response.data);
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

/* Add this style for each experience item */
.experience-item {
  display: flex; /* Create a flex container */
  align-items: flex-start; /* Align items at the start (top-aligned) */
  margin-bottom: 1em;
}

/* Flex container for image and content */
.experience-body {
  display: flex;
  gap: 1em; /* Space between image and content */
  width: 100%;
}

/* Experience image styling */
.experience-images {
  flex-shrink: 0; /* Prevent the image from shrinking */
}

.experience-image {
  width: 100px; /* Fixed width for images */
  height: auto; /* Maintain aspect ratio */
  border-radius: 4px; /* Optional: rounded corners */
  border: 1px solid #ddd; /* Optional: border around images */
}

/* Experience content styling */
.experience-content {
  flex-grow: 1; /* Allow content to grow and fill space */
}

/* Rest of your styles */
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
  font-size: 1.8em;
  margin-bottom: 0.5em;
}

/* Main list styling */
ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

/* List item styling for experience entries */
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
