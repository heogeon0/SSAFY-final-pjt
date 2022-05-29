<template>
  <div class="mb-5">
    <form @submit.prevent="onSubmit" class="comment-list-form">
      <div class="d-flex">
        <input
          type="text"
          class="form-control"
          style="width: 50%; height: 50px"
          id="comment"
          v-model="content"
          required
        />
        <button class="btn btn-outline-warning" style="height: 50px">
          Comment
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "CommentListForm",
  data() {
    return {
      content: "",
    };
  },
  computed: {
    ...mapGetters(["selectedReview"]),
  },
  methods: {
    ...mapActions(["createComment"]),
    onSubmit() {
      this.createComment({
        reviewPk: this.selectedReview.pk,
        content: this.content,
      });
      this.content = "";
    },
  },
};
</script>

<style>
</style>