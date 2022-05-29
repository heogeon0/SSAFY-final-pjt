const HOST = 'http://localhost:8000/'

const MOVIES = 'movies/'
// const RECOMMENDATION = 'recommendation/'
const COMMUNITIES = 'communitys/'
const ACCOUNTS = 'accounts/'


export default {
  movies: {
    home: () => HOST + MOVIES + 'home/',
    createReview: (moviePk) => HOST + MOVIES + 'home/' + `${moviePk}/` + 'score/',
    updateDeleteReview: (moviePk, scorePk) => HOST + MOVIES + 'home/' + `${moviePk}/` + 'score/' + `${scorePk}/`,
    recommendation: () => HOST + MOVIES + 'recommendation/',
    search: () => HOST + MOVIES + 'searchmovie/',
  },
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
  },
  communities: {
    reviews: () => HOST + COMMUNITIES + 'review/',
    review: reviewPk => HOST + COMMUNITIES + 'review/' + `${reviewPk}/`,
    reviewLike: reviewPk => HOST + COMMUNITIES + 'review/' + `${reviewPk}/` + 'like/',
    commentCreate: (reviewPk) => HOST + COMMUNITIES + 'review/' + `${reviewPk}/` + 'comment/',
    commentChange: (reviewPk, commentPk) => HOST + COMMUNITIES + 'review/' + `${reviewPk}/` + 'comment/' + `${commentPk}/`,
    commentLike: (reviewPk, commentPk) => HOST + COMMUNITIES + 'review/' + `${reviewPk}/` + 'comment/' + `${commentPk}/` + 'like/'
    // likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    // comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    // comment: (articlePk, commentPk) =>
    //   HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  },

}
