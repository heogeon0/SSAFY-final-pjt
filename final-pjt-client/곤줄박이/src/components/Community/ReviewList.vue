<template>
  <div>
    <router-link :to="{ name: 'createReview' }"><div id="create-btn" class="btn btn-sm btn-warning" style="margin-top:5px">글만들기</div></router-link>
    <div id="community-contents">
      <table>
        <tr>
          <th id="num">번호</th>
          <th>제목</th>
          <th>작성자</th>
        <!-- <td class="table-date">날짜</td> -->
        </tr>
        <tr v-for="review in paginatedData" :key="review.pk">
          <td id="num" class="col col-2"> {{ review.pk }} </td>
          <td class="col col-8"> 
            <router-link 
            :to="{ name: 'reviewDetail' , params : {'reviewPk' : review.pk}}">  
            {{ review.title }} <span id="small-text" style="color:rgb(255, 187, 0);
            font-size :small;
            ">[{{ review.comment_count }}]</span>
            </router-link> 
            </td>
          <td class="col col-2"> {{ review.user.username }} </td>
            <!-- <td class="table-date">{{ review.created_at }}</td> -->
        </tr>
      </table>
    
    </div>
    <div class="padding">
      <ul class="pagination">
        <li class="page-item"><a class="btn btn-outline-secondary btn-sm" @click.prevent="prevPage" 
        :class="{ 'disabled' : pageNum === 0}">이전</a></li>
        <li class="page-item" v-for="k in pageCount" :key="k"><a 
        class="btn btn-outline-secondary btn-sm" 
        @click.prevent="seletectPage(k)"
        :class="{ 'active' : k === pageNum + 1 }"
        >{{k}}</a></li>
        <li class="page-item"><a class="btn btn-outline-secondary btn-sm" @click.prevent="nextPage"
        :class="{ 'disabled' : pageNum + 1 === pageCount}">다음</a></li>
      </ul>
    </div>
  </div>

</template>

<script>
import { mapActions } from 'vuex'

export default {
  name : 'reviewList',
  data() {
    return {
      pageNum : 0
    }
  },
  props : {
    reviews : {
      type : Array,
    },
    pageSize : {
      type : Number,
      required : false,
      default : 15,
    }
  },
  methods : {
    ...mapActions(['fetchReview']),
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },
    seletectPage (k) {
      this.pageNum = k-1;
    }
  },
  computed : {
    pageCount() {
      let lstLength = this.reviews.length
      let lstSize = this.pageSize
      let page = Math.floor((lstLength - 1) / lstSize) + 1
      return page
    },
    paginatedData(){
      const start = this.pageNum * this.pageSize
      const end = start + this.pageSize

      return this.reviews.slice(start,end)
    }
  }

}
</script>

<style>
#num {
  padding: 0px 0px 0px 10px;
}
table {
  width: 100%;

}
table tr:first-child {
  border-bottom: 3px solid rgb(80, 80, 80);
  border-top:0px;
}
tr{
  border-top: 1px solid rgb(81, 81, 81);
  height: 40px !important;
}
th, td {
  vertical-align : middle ;
}

#create-btn {
  position: relative;
  left : 93%;
  bottom: 10px;
}
.padding {
  margin-top :30px ;
  display: flex;
  justify-content: center;
}
.background-image {
  width: 100%;
  opacity: 40%;
}

</style>