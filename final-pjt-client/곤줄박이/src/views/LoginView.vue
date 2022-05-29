<template>
  <div class="login-div">
    <img
      class="background-image"
      src="@/assets/background.png"
      alt="not-found"
    />
    <div id="login-box" class="rounded-4">
      <h1 class="text-center mb-5">Login</h1>
      <account-error-list v-if="authError"></account-error-list>

      <form @submit.prevent="login(credentials)">
        <div class="container">
          <div class="input-group mb-2">
            <span class="input-group-text" id="basic-addon1"
              ><label id="label" for="username">username: </label></span
            >

            <input
              v-model="credentials.username"
              type="text"
              id="username"
              required
              class="form-control"
              placeholder="Username"
              aria-label="Username"
              aria-describedby="basic-addon1"
            />
          </div>

          <div>
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1"
                ><label id="label" for="password">password: </label></span
              >
              <input
                v-model="credentials.password"
                type="password"
                id="password"
                required
                class="form-control"
                placeholder="Password"
                aria-label="Username"
                aria-describedby="basic-addon1"
              />
            </div>
          </div>
          <button class="btn btn-outline-warning" id="login-button">
            로그인 하기
          </button>
        </div>
      </form>
      <div class="mt-5">
        <p class="text-center" id="login-p">
          아직 NextLevel의 회원이 아니신가요?
        </p>
        <p class="text-center" id="login-p">
          지금 회원가입하고 영화 추천 받아보세요!
        </p>
        <p class="text-center">
          <router-link
            id="login-text"
            aria-current="page"
            :to="{ name: 'signup' }"
            >회원가입 하러가기
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AccountErrorList from "@/components/Account/AccountErrorList.vue";

export default {
  name: "LoginView",
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: "",
        password: "",
      },
    };
  },
  computed: {
    ...mapGetters(["authError"]),
  },
  methods: {
    ...mapActions(["login"]),
  },
};
</script>

<style>
.login-div {
  position: relative;
}
.background-image {
  width: 100%;
  opacity: 20;
}
#login-box {
  border-radius: 30px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 50px 100px 100px 100px;
  background: rgba(0, 0, 0, 0.651);
}
#label {
  color: black;
}
#login-button {
  width: 100%;
}
#login-text {
  color: white;
}
#login-p {
  color: rgb(172, 172, 172);
}
</style>
