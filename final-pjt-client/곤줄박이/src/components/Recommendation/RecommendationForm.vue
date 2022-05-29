<template>
  <div>
    <div class="container" id="box2">
      <div class="row">
        <div
          v-for="movie in movies"
          :key="movie.id"
          class="col-lg-2 col-md-3 col-sm-4 col-6"
        >
          <div style="width: 10rem" class="mb-3 mx-1">
            <div @click="setBind($event, movie.pk)">
              <img
                id="first-recom-img"
                :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
                class="card-img-top"
                alt="..."
                height="250px"
              />
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="d-flex justify-content-center py-5 grad" id="button-div">
      <router-link
        aria-current="page"
        :to="{ name: 'recommendationMovie' }"
        id="movie-router"
      >
        <button
          class="row btn btn-warning"
          id="select"
          @click="recommendMovie(selectedData)"
        >
          선택 완료
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "RecommendationForm",
  props: {
    movies: {
      type: Array,
    },
  },

  data() {
    return {
      selectedData: [],
    };
  },

  methods: {
    ...mapActions(["recommendMovie"]),
    setBind(event, movie) {
      if (event.path[1].classList.toggle("selected")) {
        this.selectedData.push(movie);
      } else {
        const moviePop = this.selectedData.indexOf(movie);
        this.selectedData.splice(moviePop, 1);
      }
    },
  },
};
</script>

<style>
#movie-router {
  font-size: 20px;
}
#box2 {
  height: 100%;
  padding: 50px 5%;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}
.card {
  margin: 20px;
}
.selected {
  opacity: 0.5;
  border: 1px solid rgb(255, 255, 255);
}
a {
  text-decoration: none;
  color: black;
  font: bold;
}
#select {
  height: 60px;
  width: 500px;
}
.grad {
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0),
    rgba(0, 0, 0, 0.5),
    rgb(0, 0, 0)
  );
  position: fixed;
  top: 85%;
}
#button-div {
  width: 100%;
  height: 200px;
  margin-bottom: 10px;
}
#first-recom-img:hover {
  transform: scale(1.05);
  transition: all 200ms ease-in;
  filter: brightness(60%);
}
</style>