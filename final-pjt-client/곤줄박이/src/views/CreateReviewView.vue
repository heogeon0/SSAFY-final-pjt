<template>
  <div id="communitybody">
    <community-nav></community-nav>
    <div id="community-form" style="height: 700px">
      <review-form :review="setCredential" action="create"></review-form>
    </div>
  </div>
</template>

<script>
import ReviewForm from '@/components/Community/ReviewForm.vue'
import CommunityNav from '@/components/Community/CommunityNav.vue'
import {mapGetters} from 'vuex'
export default {
  name : "createReview",
  data() {
    return {
      credentials : {
        title : "",
        content : "",
      },
    }
  },
  computed : {
    ...mapGetters(['nowCategory']),
    setCredential(){
      return {
        ...this.credentials,
        kind : this.nowCategory
      }
    }
  },
  components : {
    ReviewForm,
    CommunityNav,
  }
}
</script>

<style>

</style>