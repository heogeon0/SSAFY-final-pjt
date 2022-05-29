<template>
  <div
    id="modalbox"
    :style="{
      'background-image': `linear-gradient(to left, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 1), rgba(0, 0, 0, 1)), url('https://image.tmdb.org/t/p/original${moviedetail.backdrop_path}')`,
    }"
  >
    <div id="first" v-if="isVideo">
      <div id="youtube-back">
        <video-modal
          :video="getMovieVideo"
          @close="videoSwitch"
          id="video-fixed"
        ></video-modal>
      </div>
    </div>

    <img
      src="@/assets/x-button.png"
      id="myButton"
      @click="deleteMovie"
      style="width: 2.5%; border-radius: 70%"
      alt=""
    />

    <div id="second" class="row">
      <div class="col col-12 col-lg-6" style="margin: 0.5% 0px 0px 3%">
        <div class="movie-detail">
          <h1>{{ moviedetail.title }}</h1>
          <br />
          <div class="d-flex justify-content-between">
            <div>
              <span class="h4">평점 {{ moviedetail.vote_average }} </span>
              <span> ㆍ</span>
              <span v-for="genre in moviedetail.genres" :key="genre.id">
                {{ genre }} /
              </span>
              <span> {{ moviedetail.released_date }}</span>
            </div>
            <button
              class="btn btn-outline-warning mybutton"
              @click.prevent="videoSwitch"
            >
              예고편보기
            </button>
          </div>
          <div id="border-2" class="mt-2">
            <p class="mt-3">{{ moviedetail.overview }}</p>
          </div>
        </div>
        <div>
          <div class="review">
            <div id="border-1" class="mb-2">
              <div class="mb-3">
                <span class="h3 text"> 한 줄 리뷰</span>
                <span class="h5">
                  ㆍ 총 {{ scoreMovie.length }}건 | 평점{{
                    scoreMovie.result }}</span
                >
              </div>
            </div>

            <span class="review-form">
              <movie-review-form
                :moviePk="moviedetail.pk"
                :scores="moviedetail.scores"
              ></movie-review-form>
            </span>
            <span class="review-list">
              <movie-review-list
                :reviews="moviedetail.scores"
                :moviePk="moviedetail.pk"
                class="mt-5"
              ></movie-review-list>
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!--가장큰행 (1: contentbox, 2:moviebox)-->
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import VideoModal from "@/components/Movie/VideoModal.vue";
import MovieReviewForm from "@/components/Movie/MovieReviewForm.vue";
import MovieReviewList from "@/components/Movie/MovieReviewList.vue";

export default {
  name: "movie-detail",
  components: {
    VideoModal,
    MovieReviewForm,
    MovieReviewList,
  },
  computed: {
    ...mapGetters(["moviedetail", "getMovieVideo", "scoreMovie"]),
  },
  data() {
    return {
      isVideo: false,
    };
  },

  methods: {
    ...mapActions(["deleteMovie"]),
    videoSwitch() {
      this.isVideo = !this.isVideo;
    },
    alterClose() {
      this.$emit("close");
    },
  },
};
</script>

<style>
#border-1 {
  border-bottom: 0.5px solid rgb(171, 171, 171);
}
#border-2 {
  border-top: 0.5px solid rgb(171, 171, 171);
}
.movie-detail {
  padding: 0px 0px 30px 0px;
}
#modalbox {
  height: 100%;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  color: white;
}
/* #first {
  position: fixed;
  top: 50%;
  left: 50%;
  height: 70%;
  width: 80%;
  transform: translate(-50%, -50%);
  background: rgba(0, 0, 0, 0.532);
} */

#video-fixed {
  position: fixed;
  top: 50%;
  left: 50%;
  /* height: 60%; */
  width: 80%;
  transform: translate(-50%, -50%);
  z-index: 2;
}
#second {
  width: 90%;
  padding: 30px;
}
#myButton {
  position: fixed;
  left: 99.5%;
  transform: translate(-100%);
  width: 50px;
  cursor: pointer;
}
</style>