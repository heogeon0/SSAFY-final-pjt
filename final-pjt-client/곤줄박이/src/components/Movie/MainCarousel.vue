<template>
  <div>
    <hooper :autoPlay="true" :playSpeed="5000" style="height: 600px">
      <slide v-for="movie in movies" :key="movie.id" class="slide">
        <div class="slide-div" @click="getDetail(movie)">
          <div
            id="test"
            style="cursor: pointer"
            :style="{
              'background-image': `linear-gradient(to left, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 1), rgba(0, 0, 0, 1)), url('https://image.tmdb.org/t/p/original${movie.backdrop_path}')`,
            }"
          >
            <div id="main-sub">
              <div class="main-title">
                <h1>{{ movie.title }}</h1>
                <br />
                <span id="main-overview"> {{ movie.overview }} </span>
                <hr />
                <button
                  id="detail-button"
                  class="btn btn-outline-warning"
                  @click="getDetail(movie)"
                >
                  자세히 보기
                </button>
              </div>
            </div>
          </div>
        </div>
      </slide>
    </hooper>
  </div>
</template>

<script>
import { Hooper, Slide } from "hooper";
import "hooper/dist/hooper.css";
import { mapActions } from "vuex";

export default {
  name: "MainCarousel",
  props: {
    movies: {
      type: Array,
    },
  },
  components: { Hooper, Slide },
  methods: {
    ...mapActions(["getDetail"]),
  },
};
</script>

<style>
#test {
  height: 600px;
  width: 100%;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}
#main-sub {
  padding: 200px 50px;
  height: 100px;
  width: 500px;
}

#main-overview {
  display: -webkit-box;
  -webkit-line-clamp: 7;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
#detail-button {
  width: 150px;
}
</style>