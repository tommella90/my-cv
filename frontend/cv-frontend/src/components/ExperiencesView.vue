<template>
  <div>
    <h1>Experiences</h1>
    <ul v-if="filteredExperiences.length">
      <li v-for="experience in filteredExperiences" :key="experience.id">
        <h2>{{ experience.title }} - {{ experience.company }}</h2>
        <p><strong>Location:</strong> {{ experience.location }}</p>
        <p><strong>Dates:</strong> {{ experience.start_date }} - {{ experience.end_date || 'Present' }}</p>
        <p><strong>Descriptions:</strong></p>
        <ul>
          <li v-for="(description, index) in experience.descriptions" :key="index">
            {{ description.description }}
          </li>
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
  color: #000;
}
</style>
