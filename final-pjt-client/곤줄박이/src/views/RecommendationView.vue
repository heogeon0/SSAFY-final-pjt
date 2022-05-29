<template>
  <div>
    <h2 class="text-center mt-5 text-white">
      나만을 위한 콘텐츠를 추천 받아보세요!
    </h2>
    <br />
    <h1 class="text-center">
      보고 싶은 <span class="h1 yellow"> 3개 이상의 영화</span>를 선택하세요
    </h1>
    <div>
      <recommendation-form :movies="reMovie"></recommendation-form>
    </div>
  </div>
</template>

<script>
import RecommendationForm from "@/components/Recommendation/RecommendationForm.vue";

import { mapActions, mapGetters } from "vuex";
export default {
  name: "RecommendationView",
  components: {
    RecommendationForm,
  },

  methods: {
    ...mapActions(["getRecommendMovies", "fetchCurrentUser"]),
  },
  created() {
    this.getRecommendMovies();
  },

  computed: {
    ...mapGetters(["reMovie", "currentUser"]),
  },
};
</script>

<style>
.yellow {
  color: rgb(255, 208, 0);
}
</style>