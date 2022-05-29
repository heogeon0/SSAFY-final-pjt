<template>
  <div>
    <comment-list-item 
      v-for="comment in comments" 
      :comment="comment" 
      :key="comment.pk">
    </comment-list-item>  
    <hr>
    <comment-list-form></comment-list-form>
    <hr>
  </div>
</template>

<script>
import CommentListItem from '@/components/Community/CommentListItem.vue'
import CommentListForm from '@/components/Community/CommentListForm.vue'

export default {
  name : 'CommentList',
  components : {
    CommentListForm,
    CommentListItem,
  },
  props : {
    comments : Array,
  }
}
</script>

<style>

</style>