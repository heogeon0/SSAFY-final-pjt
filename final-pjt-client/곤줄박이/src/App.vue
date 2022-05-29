<template>
  <div class="app">
    <nav-bar></nav-bar>
    <router-view></router-view>
    <footer-bar></footer-bar>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import FooterBar from "@/components/FooterBar.vue";

import { mapActions } from "vuex";

export default {
  name: "app",

  components: {
    NavBar,
    FooterBar,
  },
  methods: {
    ...mapActions(["fetchCurrentUser",'fetchReviews']),
  },
  created() {
    this.fetchCurrentUser();
    this.fetchReviews()
  },
};
</script>


<style>

</style>
