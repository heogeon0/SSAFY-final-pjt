<template>
  <div>
    <div id="black-bg" class="black-bg" v-if="isModalView" @click="deleteMovie">
      <div class="white-bg" onclick="event.stopImmediatePropagation()">
        <movie-detail></movie-detail>
      </div>
    </div>
    <h1 class="py-5 text-center">
      <span class="yellow">{{ currentUser.username }}님</span>만을 위한 추천
      영화입니다!
    </h1>
    <div id="app5">
      <sequential-entrance>
        <div
          v-for="movie in recommendMovie"
          :key="movie.id"
          class="col-lg-3 col-md-6 col-sm-12 col-12 recom-div mb-5"
        >
          <div
            class="box3 recom-div mx-auto"
            style="width: 18.5rem"
            v-for="index in 1"
            :key="index"
          >
            <div class="card" style="width: 18rem" @click="getDetail(movie)">
              <img
                id="#app4img"
                style="cursor: pointer"
                :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
                class="card-img-top"
                alt="..."
                height="400px"
              />
              <div class="card-body">
                <h5 class="card-title">{{ movie.title }}</h5>
                <p class="card-text"></p>
              </div>
            </div>
          </div>
        </div>
      </sequential-entrance>
    </div>
    <br />
    <br />
    <br />
  </div>
</template>

<script>
import MovieDetail from "@/components/Movie/MovieDetail.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "RecommendationMovie",
  components: {
    MovieDetail,
  },

  methods: {
    ...mapActions([
      "fetchCurrentUser",
      "getDetail",
      "getMovies",
      "deleteMovie",
    ]),
  },

  computed: {
    ...mapGetters([
      "currentUser",
      "recommendMovie",
      "moviedetail",
      "isModalView",
    ]),
  },
};
</script>

<style>
#app5 {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 60px;
}
.recom-div {
  margin: 30px;
}
#app5 > span {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.my-modal {
  box-sizing: border-box;
  background-color: red;
}
.black-bg {
  width: 100%;
  height: 100%;
  /* background: rgba(0, 0, 0, 0.8); */
  position: fixed;
  padding: 5% 0%;
  z-index: 1;
}

.white-bg {
  width: 100%;
  height: 90%;
}
#app4img:hover {
  transform: scale(1.05);
  transition: all 200ms ease-in;
  filter: brightness(60%);
}
</style>