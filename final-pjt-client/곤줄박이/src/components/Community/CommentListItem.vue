<template>
  <div>
    <h5 style="color: white">{{ comment.user.username }}</h5>
    <div style="display: inline-block" class="comment-box">
      <p v-if="!isEditing">{{ payload.content }}</p>
      <span v-if="isEditing">
        <input style="" type="text" v-model="payload.content" />
        <button @click="onUpdate">Update</button> |
        <button @click="switchIsEditing">Cancle</button>
      </span>

      <span v-if="currentUser.username === comment.user.username && !isEditing">
        <a href="#" @click.prevent="switchIsEditing">Edit</a> |
        <a href="#" @click.prevent="deleteComment(payload)">Delete</a> |
      </span>
        <a href="#" @click.prevent="commentLike(payload)">
      <i class="far fa-heart"></i>
      {{ comment.like_count }}</a>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "CommentListItem",
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        reviewPk: this.$route.params.reviewPk,
        commentPk: this.comment.pk,
        content: this.comment.content,
      },
    };
  },
  computed: {
    ...mapGetters(["currentUser"]),
  },
  methods: {
    ...mapActions(["updateComment", "deleteComment", "commentLike"]),
    switchIsEditing() {
      this.isEditing = !this.isEditing;
    },
    onUpdate() {
      this.updateComment(this.payload);
      this.isEditing = false;
    },
  },
};
</script>

<style>
.comment-box {
  display: block;
  position: static;
  width: auto !important;
  margin: 0px 3px 10px;
  padding: 10px 20px;
  background-color: rgb(198, 198, 198);
  border-radius: 10px;
}
</style>