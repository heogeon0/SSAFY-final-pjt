import router from '@/router'
import drf from '@/api/drf'
import axios from 'axios'


export default {
  // namespaced: true,
  state: {
    movies: [],
    moviedetail: null,
    movievideo: '',
    recommendMovie: null,
    reMovies: [],
    weather: null,
    time: null,
    searchMovies: []
  },
  getters: {
    scoreMovie(state) {
      const length = state.moviedetail.scores.length
      const scores = state.moviedetail.scores
      let sum = 0;
      let result = ''
      if (length > 0) {
        for (let i = 0; i < length; i++) {
          sum += scores[i]['number'];   // 배열의 요소들을 하나씩 더한다.
        }
        result = (sum / length).toFixed(1)
      }
      const movie_score = {
        length: length,
        result: result,
        score_count: state.moviedetail.score_count,
        score_sum: state.moviedetail.score_sum
      }
      return movie_score
    },
    reMovie(state) {
      return state.reMovies.filter((movie, idx) => {
        if (idx < 30) {
          return movie
        }
      })
    },
    recommendMovie(state) {
      return state.recommendMovie
    },
    searchMovie(state) {
      return state.searchMovies
    },
    mainCarouselMovie(state) {
      return state.movies.filter((movie, idx) => {
        if (idx < 10) {
          return movie
        }
      })
    },
    SubCarouselMovie(state) {
      return state.movies.filter((movie, idx) => {
        if (10 <= idx && idx < 20) {
          return movie
        }
      })
    },
    SubCarouselMovie2(state) {
      return state.movies.filter((movie, idx) => {
        if (20 <= idx && idx < 30) {
          return movie
        }
      })
    },
    SubCarouselMovie3(state) {
      return state.movies.filter((movie, idx) => {
        if (30 <= idx && idx < 40) {
          return movie
        }
      })
    },
    SubCarouselMovie4(state) {
      return state.movies.filter((movie, idx) => {
        if (40 <= idx && idx < 50) {
          return movie
        }
      })
    },
    SubCarouselMovie5(state) {
      return state.movies.filter((movie, idx) => {
        if (50 <= idx && idx < 60) {
          return movie
        }
      })
    },
    moviedetail(state) {
      return state.moviedetail
    },
    isModalView(state) {
      return !!state.moviedetail
    },
    getMovieVideo(state) {
      if (state.movievideo) return `https://www.youtube.com/embed/${state.movievideo}`
    },
    getMovieReview(state) {
      if (state.moviedetail) return state.moviedetail.scores
    },
    toDayWeather(state) {
      // 날씨 맨트
      const weather = ['Thunderstorm', 'Drizzle', 'Rain', 'Snow', 'Atmosphere', 'Clear', 'Clouds']
      const weatherMap = [
        '천둥번개치는 날씨엔',
        '잔잔한 이슬비와',
        '비오는 날',
        '크리스마스에는 집에서',
        '안개가득한 날',
        '화창한 날에는',
        '오늘처럼 꿀꿀한 날',
      ]
      const num = weather.indexOf(state.weather)
      return weatherMap.splice(num, 1)[0]
    },
    nowTime(state) {
      let time_idx = 0
      if (5 <= state.time && state.time <= 10) time_idx = 0
      else if (11 <= state.time && state.time <= 16) time_idx = 1
      else if (17 <= state.time && state.time <= 22) time_idx = 2
      else time_idx = 3
      const timeMap = [
        ['피곤한 아침을 깨워줄', '킬링타임 영화들'],
        ['무료한 오후', '역사 공부 어떠세요?'],
        ['오늘 저녁엔', '판타지 세계로'],
        ['잠안오는 새벽', '다큐멘터리 한편']
      ]
      return timeMap.splice(time_idx, 1)
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_MOVIE_DETAIL(state, movie) {
      state.moviedetail = movie
    },
    DELETE_DETAIL(state) {
      state.moviedetail = null
    },
    SET_MOVIE_VIDEO(state, video) {
      state.movievideo = video
    },
    PUSH_MOVIE_REVIEW(state, review) {
      state.moviedetail.scores.push(review)
    },
    RECOMMEND_GET_MOVIES(state, reMovies) {
      state.reMovies = reMovies
    },
    RECOMMEND_MOVIES(state, movie) {
      state.recommendMovie = movie
    },
    GETWEATHER(state, data) {
      state.weather = data.main
    },
    GETHOUR(state, hour) {
      state.time = hour
    },
    DELETE_SCORE(state, scores) {
      state.moviedetail.scores = scores
    },
    UPDATE_SCORE(state, scores) {
      state.moviedetail.scores = scores
    },
    SEARCH_MOVIE(state, searchMovies) {
      state.searchMovies = searchMovies
    },
  },

  actions: {
    getMovies({ commit, getters }) {
      axios({
        url: drf.movies.home(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('GET_MOVIES', res.data)
        })
        .catch(err => {
          console.error(err.response.data)
        })
    },
    getDetail({ commit }, movie) {
      const params = {
        key: API_KEY_YOU,
        part: 'snippet',
        Type: 'video',
        q: movie.title + '메인예고편',
      }
      axios({
        method: 'get',
        url: API_URL_YOU,
        params
      })
        .then(res => {
          commit('GET_MOVIE_DETAIL', movie)
          commit('SET_MOVIE_VIDEO', res.data.items[0].id.videoId)
        })
    },
    deleteMovie({ commit }, event) {
      event.stopPropagation()
      commit('DELETE_DETAIL')
    },
    setMovieScore({ commit, getters }, { moviePk, number, content }) {
      axios({
        url: drf.movies.createReview(moviePk),
        method: 'post',
        data: {
          number,
          content
        },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('PUSH_MOVIE_REVIEW', res.data[res.data.length - 1])
        })
        .catch(err => {
          console.log(err)
        })
    },
    getRecommendMovies({ commit, getters }) {
      axios({
        url: drf.movies.recommendation(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('RECOMMEND_GET_MOVIES', res.data)
        })
        .catch(err => {
          console.error(err.response.data)
        })
    },
    recommendMovie({ commit, getters }, movie) {
      axios({
        url: drf.movies.recommendation(),
        method: 'post',
        data: {
          movie
        },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('RECOMMEND_MOVIES', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getWeather({ commit }) {
      const now = new Date
      axios({
        url: WEATHER_URL,
        method: 'get'
      })
        .then(res => {

          commit('GETWEATHER', res.data.weather[0])
          commit('GETHOUR', now.getHours())
        })
    },
    DeleteReview({ commit, getters }, { moviePk, scorePk }) {
      axios({
        url: drf.movies.updateDeleteReview(moviePk, scorePk),
        method: 'delete',
        headers: getters.authHeader,
      })
        .then((res) => {
          commit('DELETE_SCORE', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateMoiveScore({ commit, getters }, { moviePk, scorePk, number, content }) {
      axios({
        url: drf.movies.updateDeleteReview(moviePk, scorePk),
        method: 'put',
        data: {
          number,
          content
        },
        headers: getters.authHeader,
      })
        .then((res) => {
          commit('UPDATE_SCORE', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    searchMovie({ commit, getters }, keyword) {
      axios({
        url: drf.movies.search(),
        method: 'post',
        data: { keyword },
        headers: getters.authHeader,
      })
        .then(res => {
          console.log(res.data)
          commit('SEARCH_MOVIE', res.data)
          router.push({ name: 'search' })
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
}
