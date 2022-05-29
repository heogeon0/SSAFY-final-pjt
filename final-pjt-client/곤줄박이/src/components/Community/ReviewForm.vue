<template>
  <div>
    <div id="community-contents" style="height:600px; padding: 30px 20px !important;">
      <form  @submit.prevent="onSubmit" style="width : 90%; margin:auto">
        <h1>
          글쓰기
        </h1>
        <hr>
        <div id="controller">
          <router-link :to="{name : 'communities'}"><button class="btn btn-secondary">Cancle</button></router-link>  <span></span> 
          <button class="btn btn-warning">{{action}}</button>
        </div>
        <div style = "display:flex;">
          <select name="kind" v-model="newReview.kind" style="width:20%; height:50px; margin : auto">
            <option value="0"> 분류선택</option>
            <option value="1"> 영화리뷰</option>
            <option value="2"> 영화정보</option>
            <option value="3"> 자유게시판</option>
          </select>

          <input
            v-model="newReview.title"
            placeholder="제목"
            type="text"
            id="title"
            required
            style="width:70%; margin: auto; height : 50px"
            />
        </div>

        <div style="margin:auto; width:100%; padding: 30px 20px">
          <textarea
            v-model="newReview.content"
            type="textarea"
            id="content"
            required
            style="width:100%; height:300px; resize:none"
          ></textarea>
        </div>
        
          <button id="my-create-button" class="btn btn-warning">{{action}}</button>
      </form>
    </div>
  </div>
</template>

<script>
import {mapActions}  from 'vuex'
export default {
  name : 'ReviewForm',
  props : {
    review : Object,
    action : String,
  },
  data(){
    return{ 
      newReview : {
        title : this.review.title,
        kind : this.review.kind,
        content : this.review.content,
      }
    }
  },
methods : {
  ...mapActions(['createReview','updateReview']),
  onSubmit () {
    if(this.action==='create'){
      this.createReview(this.newReview)
    } else if (this.action ==='update') {
      const payload = {
        pk : this.review.pk,
        ...this.newReview,
      }
      this.updateReview(payload)
    }
  }
}

}
</script>

<style>
#controller {
  position : relative ;
  left: 80%;
  bottom: 60px;
}


#my-create-button {
  position: relative;
  bottom: 20px;
  left : 89%
}
</style>