<template>
  <div id="app3">
    <hooper
      :progress="true"
      :autoPlay="true"
      :playSpeed="5000"
      :settings="hooperSettings"
      :centerMode="true"
      pagination="no"
      :infiniteScroll="true"
      :wheelControl="false"
      style="height: 400px"
    >
      <slide v-for="movie in movies" :key="movie.id">
        <div class="slide-div" @click="getDetail(movie)">
          <img
            id="app3img"
            style="cursor: pointer"
            width="100%"
            height="400px"
            :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
          />
        </div>
      </slide>
      <hooper-navigation slot="hooper-addons"></hooper-navigation>
    </hooper>
  </div>
</template>

<script>
import "hooper/dist/hooper.css";
import { Hooper, Slide, Navigation as HooperNavigation } from "hooper";
import { mapActions } from "vuex";

export default {
  name: "App",
  props: {
    movies: {
      type: Array,
    },
  },
  components: {
    Hooper,
    Slide,
    HooperNavigation,
  },
  methods: {
    ...mapActions(["getDetail"]),
  },

  data() {
    return {
      hooperSettings: {
        itemsToShow: 3,
        centerMode: true,
        breakpoints: {
          1100: {
            itemsToShow: 4,
            pagination: "fraction",
          },
          1400: {
            itemsToShow: 6,
            pagination: "fraction",
          },
          2000: {
            itemsToShow: 8,
            pagination: "fraction",
          },
        },
      },
    };
  },
};
</script>

<style>
#app3 {
  background-color: rgb(0, 0, 0);
  height: auto;
  padding: 21px 0;
}

.slide-div {
  height: 400px;
  padding: 10px;
  width: 100%;
}
#app3img:hover {
  transform: scale(1.05);
  transition: all 200ms ease-in;
  filter: brightness(60%);
}
</style>
