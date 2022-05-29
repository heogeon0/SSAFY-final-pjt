<template>
  <nav
    id="myNav"
    class="
      navbar navbar-fixed-top navbar-expand-md navbar-dark
      bg-dark
      sticky-top
    "
  >
    <div class="container-fluid">
      <div>
        <a class="navbar-brand" href="http://localhost:8080/">
          <span>NEXTLEVEL</span>
        </a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>

      <div class="offcanvas offcanvas-end" id="navbarSupportedContent">
        <div class="d-flex justify-content-between">
          <div></div>
          <div v-if="isLoggedIn">
            <form
              @submit.prevent="mySearch(keyword)"
              class="d-flex"
              role="search"
            >
              <input
                v-model="keyword"
                class="form-control me-2"
                type="search"
                placeholder="Search"
                aria-label="Search"
              />
              <button class="btn btn-outline-warning" type="submit">
                Search
              </button>
            </form>
          </div>
          <ul class="navbar-nav mb-lg-0">
            <li v-if="isLoggedIn" class="nav-item mx-3">
              <!-- active 클래스! -->
              <router-link
                class="nav-link active"
                aria-current="page"
                :to="{ name: 'home' }"
                >Home</router-link
              >
            </li>
            <li v-if="isLoggedIn" class="nav-item">
              <router-link
                class="nav-link active"
                aria-current="page"
                :to="{ name: 'recommendation' }"
                >영화추천</router-link
              >
            </li>
            <li v-if="isLoggedIn" class="nav-item mx-3">
              <router-link
                class="nav-link active"
                aria-current="page"
                :to="{ name: 'communities' }"
                >게시판</router-link
              >
            </li>
            <li v-if="isLoggedIn" class="nav-item mx-3">
              <router-link
                class="nav-link active"
                aria-current="page"
                :to="{ name: 'logout' }"
                >로그아웃</router-link
              >
            </li>
            <!-- <li v-if="isLoggedIn" class="nav-item mx-3">
              <router-link
                class="nav-link active"
                aria-current="page"
                :to="{ name: 'login' }"
                >로그인</router-link
              >
            </li>
            <li v-if="isLoggedIn" class="nav-item mx-3">
              <router-link
                class="nav-link active"
                aria-current="page"
                :to="{ name: 'signup' }"
                >회원가입</router-link
              >
            </li> -->
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "NavBar",
  data() {
    return {
      keyword: "",
    };
  },

  methods: {
    ...mapActions(["searchMovie"]),
    mySearch(movie) {
      this.searchMovie(movie);
      this.keyword = "";
    },
  },

  computed: {
    ...mapGetters(["isLoggedIn", "currentUser"]),
    username() {
      return this.currentUser.username ? this.currentUser.username : "guest";
    },
  },
};
</script>

<style>
#myNav {
  font-size: 18px;
  background-color: rgb(0, 0, 0) !important;
}
</style>