import drf from '@/api/drf'
import axios from 'axios'
import router from '@/router'


// import _ from 'lodash'

export default {
  // namespaced: true,
  state: {
    reviews: [],
    selectedReview: {},
    category : 0,
  },

  getters: {
    reviews (state){
      return state.reviews
    },
    selectedReview (state){
      return state.selectedReview
    },
    isReview (state) {
      return !!state.selectedReview
    },
    isAuthor (state,getters){
      return state.selectedReview.user?.username === getters.currentUser.username
    },
    selectedCategory (state){
      if(state.category !== 0){
        return state.reviews.filter(review => {
          return review.kind === state.category
        })
      } else {
        return state.reviews.filter(review => {
          return review.like_count >= 1
        })
      }
    },
    nowCategory(state) {
      return state.category
    }
  },

  mutations: {
    FETCHREVIEWS(state, reviews) {
      state.reviews = reviews
    },
    FETCHREVIEW( state, review){
      state.selectedReview = review
      // state.reviews.push(review)
    },
    SETCOMMENTS (state, comments){
      state.selectedReview.comments = comments
    },
    SET_CATEGORY(state, num){
      state.category = num
    },

  },

  actions: {
    fetchReviews({ commit, getters }) {
      axios({
        url : drf.communities.reviews(),
        method : 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('FETCHREVIEWS', res.data)
        })
        .catch(err => { // 에러페이지로 이동 구현
          console.log(err)
        })
    },

    fetchReview({ commit, getters }, reviewPk) {
      axios({
        url : drf.communities.review(reviewPk),
        method : 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('FETCHREVIEW', res.data)
        })
        .catch(err => { // 에러페이지로 이동 구현
          console.log(err)
        })

    },

    createReview({ commit, getters }, credentials) {
      axios({
        url : drf.communities.reviews(),
        method : 'post',
        data : credentials,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('FETCHREVIEW', res.data)
          // dispatch(this.fetchReview, paresInt(res.data.reviewPk))
          router.push({name : 'reviewDetail', params : {'reviewPk' : res.data.pk} })
        })
        .catch(err => {
          console.log(err)
        })
    },

    updateReview({ commit, getters }, credentials ) {
      axios({
        url : drf.communities.review(credentials.pk),
        method : 'put',
        data : credentials,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('FETCHREVIEW', res.data)
          router.push({name : 'reviewDetail', params : {'reviewPk' : res.data.pk} })
        })
        .catch(err => {
          console.log(err)
        })
    },

    deleteReview({ commit, getters }, reviewPK) {
      if(confirm('정말 삭제하시겠습니까?')){
        axios({
          url : drf.communities.review(reviewPK),
          method : 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('FETCHREVIEW','')
            router.push({name: 'communities'})
          })
          .catch(err => {
            console.log(err)
          })
        }
    },

    likeReview({ commit, getters }, reviewPk) {
      axios({
        url : drf.communities.reviewLike(reviewPk),
        method : 'post',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('FETCHREVIEW', res.data)
        })

        .catch(err => console.error(err.response))
    },

    createComment({ commit,getters }, { reviewPk, content }) {
      const comment = { content }
      axios({
        url : drf.communities.commentCreate(reviewPk),
        method : 'post',
        data : comment,
        headers: getters.authHeader,
      })
        .then((res) => {
          commit('SETCOMMENTS', res.data) 
        })
        .catch(err => {
          console.log(err)
        })
    },

    updateComment({ commit, getters }, credentials) { //commentPk를 받아야함
      axios({
        url : drf.communities.commentChange(credentials.reviewPk, credentials.commentPk),
        method : 'put',
        data : credentials,
        headers: getters.authHeader,
      })
        .then((res) => {
          console.log(res.data)
          commit('SETCOMMENTS', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },

    deleteComment({ commit, getters },  {reviewPk,commentPk} ) {
      axios({
        url : drf.communities.commentChange(reviewPk, commentPk),
        method : 'delete',
        data : {},
        headers: getters.authHeader,
      })
        .then((res) => {
          commit('SETCOMMENTS', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    setCategory({commit}, num ) {
      commit('SET_CATEGORY',num)
    },
    commentLike({ commit, getters}, {reviewPk,commentPk}){
      axios({
        url : drf.communities.commentLike(reviewPk, commentPk),
        method : 'post',
        headers: getters.authHeader,
      })
      .then((res)=> {
        console.log(res.data)
        commit('SETCOMMENTS', res.data)
      })
    }
  },
}
