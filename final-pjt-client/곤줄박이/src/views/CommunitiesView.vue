<template>
  <div id="communitybody">
    <community-nav></community-nav>
    <div id="community-form">
      <review-list :reviews="selectedCategory"></review-list>
    </div>
  </div>
</template>

<script>
import ReviewList from '@/components/Community/ReviewList.vue'
import CommunityNav from '@/components/Community/CommunityNav.vue'
import { mapGetters, mapActions } from 'vuex'


export default {
  name : 'CommunitiesView',
  components : {
    ReviewList,
    CommunityNav,
  },
  computed : {
    ...mapGetters(['reviews', 'selectedCategory'])
  },
  methods : {
    ...mapActions(['fetchReviews'])
  },
  created() {
    this.fetchReviews()
  }
}
</script>

<style>


</style>