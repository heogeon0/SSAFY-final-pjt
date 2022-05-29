<template>
  <div id="communitybody">
    <community-nav></community-nav>
    <div id="community-form">
      <router-link :to="{ name: 'communities' }"
        ><button id="go-menu" class="btn btn-warning">목록</button></router-link
      >
      <div id="community-contents" style="padding: 40px 20px; height: 600px">
        <div id="title">
          <div style="margin: 0px 0xpx 25px">
            <div class>
              <div style="height:10px padding-bottom:100px !important">
                <span
                  class="h4"
                  style="
                    background-color: rgb(255, 187, 0);
                    height: 8px !important;
                  "
                  >{{ setKind }}</span
                >
              </div>
              <h1 style="color: black" class="col">
                {{ selectedReview.title }}
              </h1>
            </div>
          </div>
        </div>
        <div id="information" style="margin: 0px 20px">
          <div class="d-flex justify-content-between">
            <div>
              <span style="margin-right: 20px"
                >작성자 : {{ selectedReview.user.username }}</span
              >
              <span style="margin-right: 20px">작성 : {{ created_time }}</span>
              <span @click="likeReview(selectedReview.pk)"
                ><i class="fas fa-heart fa-bounce"></i>
                {{ selectedReview.like_count }}
              </span>
            </div>

            <div>
              <div v-if="isAuthor">
                <div id="controlbox">
                  <router-link
                    :to="{
                      name: 'updateReview',
                      params: { reviewPk: selectedReview.pk },
                    }"
                    class="me-3"
                    >수정</router-link
                  >
                  <a href="#" @click.prevent="deleteReview(selectedReview.pk)">
                    삭제</a
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
        <hr />
        <div>
          {{ selectedReview.content }}
        </div>
      </div>
      <hr />
      <div
        style="
          margin-top: 0px;
          color: white;
          padding-left: 5px;
          margin-bottom: 10px;
        "
      >
        댓글 수 : {{ selectedReview.comments.length }}
        <hr />
      </div>
      <div style="padding-left: 5px">
        <comment-list :comments="selectedReview.comments"></comment-list>
      </div>
    </div>
  </div>
</template>

<script>
import CommentList from "@/components/Community/CommentList.vue";
import CommunityNav from "@/components/Community/CommunityNav.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "reviewDetail",
  components: {
    CommentList,
    CommunityNav,
  },
  data() {
    return {
      myKind: ["영화리뷰", "영화정보", "자유게시판"],
    };
  },
  methods: {
    ...mapActions(["fetchReview", "deleteReview", "likeReview"]),
  },

  computed: {
    ...mapGetters(["selectedReview", "isAuthor", "isAuthor"]),
    setKind() {
      const num = this.selectedReview.kind;
      return this.myKind.slice(num - 1, num)[0];
    },
    created_time() {
      return this.selectedReview.created_at.slice(0, 10);
    },
  },
  created() {
    this.fetchReview(this.$route.params.reviewPk);
  },
};
</script>

<style>
#go-menu {
  position: relative;
  left: 93%;
  bottom: 10px;
  right: 10%;
}
</style>