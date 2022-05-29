<template>
  <div class="home">
    <!-- 모달 -->
    <div id="black-bg" class="black-bg" v-if="isModalView" @click="deleteMovie">
      <div class="white-bg" onclick="event.stopImmediatePropagation()">
        <movie-detail></movie-detail>
      </div>
    </div>

    <!-- 모달 끝 -->

    <!-- 시작박스 -->
    <div class="row main-div">
      <!-- 메인캐러셀시작 -->
      <!-- <span class="h1">메인캐러샐</span> -->
      <main-carousel :movies="mainCarouselMovie"></main-carousel>
    </div>
    <!-- 메인캐러셀끝 -->
    <div class="row sub-div">
      <!-- 서브 캐러셀 -->
      <div class="h2 my-text">
        <span class="yellow">{{ toDayWeather }}</span> 이 영화 어때요? ☁
      </div>
      <sub-carousel :movies="SubCarouselMovie"></sub-carousel>
    </div>
    <div class="row sub-div">
      <div class="h2 my-text">
        <span class="yellow">{{ nowTime[0][0] }} </span>{{ nowTime[0][1] }} 🕑
      </div>
      <sub-carousel :movies="SubCarouselMovie2"></sub-carousel>
    </div>
    <div class="row sub-div">
      <div class="h2 my-text">
        영원히 회자되는
        <span class="yellow">명작 10선 🏆</span>
      </div>

      <sub-carousel :movies="SubCarouselMovie3"></sub-carousel>
    </div>
    <div class="row sub-div">
      <div class="h2 my-text">
        <span class="yellow"> 한국 영화 BEST 10 </span>아직 안보셨다면! 🎬
      </div>

      <sub-carousel :movies="SubCarouselMovie4"></sub-carousel>
    </div>
    <div class="row sub-div">
      <div class="h2 my-text">
        감동이 있는
        <span class="yellow">애니메이션 </span>모음 🎈
      </div>
      <sub-carousel :movies="SubCarouselMovie5"></sub-carousel>
    </div>
    <!-- 부분캐러셀끝 -->
  </div>
  <!-- 시작박스끝 -->
</template>

<script>
import MainCarousel from "@/components/Movie/MainCarousel.vue";
import SubCarousel from "@/components/Movie/SubCarousel.vue";
import MovieDetail from "@/components/Movie/MovieDetail.vue";

import { mapActions, mapGetters } from "vuex";

export default {
  name: "HomeView",
  components: {
    MainCarousel,
    SubCarousel,
    MovieDetail,
  },

  methods: {
    ...mapActions([
      "getMovies",
      "deleteMovie",
      "fetchCurrentUser",
      "getWeather",
    ]),
  },

  created() {
    this.getMovies();
    this.getWeather();
  },

  computed: {
    ...mapGetters([
      "mainCarouselMovie",
      "SubCarouselMovie",
      "SubCarouselMovie2",
      "SubCarouselMovie3",
      "SubCarouselMovie4",
      "SubCarouselMovie5",
      "isModalView",
      "currentUser",
      "toDayWeather",
      "nowTime",
    ]),
  },
};
</script>

<style>
.h2 {
  font-weight: 700;
}
.main-div {
  margin: 10px;
  color: white !important;
}

.sub-div {
  margin: 170px 30px;
  height: 450px !important;
  color: white !important;
}
/* 모달창 */
.my-modal {
  box-sizing: border-box;
  background-color: red;
}
.black-bg {
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  position: fixed;
  padding: 5% 0%;
  z-index: 1;
}

.white-bg {
  width: 100%;
  height: 90%;
}
</style>