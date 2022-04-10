<template>
  <div id="app">
    <Header />
    <!-- <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav> -->
    <router-view/>
    <Footer />
  </div>
</template>

<style>
  @import "assets/css/bootstrap/bootstrap.css";
  @import "assets/css/styles.css";
</style>

<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

export default {
  components: {Header, Footer}
}
</script>
