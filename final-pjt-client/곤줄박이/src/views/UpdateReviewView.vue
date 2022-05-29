<template>
  <div id="communitybody">
    <community-nav></community-nav>
    <div id="community-form" style="height: 700px">
      <review-form v-if="isReview" :review="selectedReview" action="update"></review-form>
    </div>
  </div>
</template>

<script>

import ReviewForm from '@/components/Community/ReviewForm.vue'
import CommunityNav from '@/components/Community/CommunityNav.vue'

import {mapGetters, mapActions} from 'vuex'

export default {
  name : "createReview",
  components : {
    ReviewForm,
    CommunityNav,
  },
  computed : {
    ...mapGetters(['selectedReview', 'isReview',])
  },
  methods : {
    ...mapActions(['fetchReview'])
  },
  created() {
    this.fetchReview(this.$route.params.reviewPk)
  }
}
</script>

<style>

</style>