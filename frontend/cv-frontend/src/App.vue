<template>
  <div id="app">
    <ExperiencesView/>
    <EducationsView/>
    <router-view/>
  </div>
</template>

<script>
import EducationsView from './components/EducationsView.vue';
import ExperiencesView from './components/ExperiencesView.vue';


export default {
  name: 'App',
  components: {
    ExperiencesView, EducationsView
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
