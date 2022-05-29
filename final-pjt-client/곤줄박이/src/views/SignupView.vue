<template>
  <div class="signup-div">
    <img
      class="background-image"
      src="@/assets/background.png"
      alt="background image"
    />
    <div id="fixed-box">
      <div id="signup-box" class="rounded-4">
        <h1 class="text-center mb-5">회원가입</h1>
        <account-error-list v-if="authError"></account-error-list>

        <form @submit.prevent="signup(credentials)">
          <div class="container">
            <div class="input-group mb-2">
              <span class="input-group-text" id="basic-addon1"
                ><label id="label" for="username">아이디: </label></span
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
              <div class="input-group mb-2">
                <span class="input-group-text" id="basic-addon1"
                  ><label id="label" for="password1">비밀번호: </label></span
                >
                <input
                  v-model="credentials.password1"
                  type="password"
                  id="password1"
                  required
                  class="form-control"
                  placeholder="Password1"
                  aria-label="Username"
                  aria-describedby="basic-addon1"
                />
              </div>
            </div>
            <div>
              <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1"
                  ><label id="label" for="password2"
                    >비밀번호 확인:
                  </label></span
                >
                <input
                  v-model="credentials.password2"
                  type="password"
                  id="password2"
                  required
                  class="form-control"
                  placeholder="Password2"
                  aria-label="Username"
                  aria-describedby="basic-addon1"
                />
              </div>
            </div>
            <button class="btn btn-outline-warning" id="signup-button">
              회원가입
            </button>
          </div>
        </form>
        <div class="mt-5">
          <p class="text-center" id="login-p">이미 NextLevel의 회원이시라면?</p>
          <p class="text-center">
            <router-link
              id="login-text"
              aria-current="page"
              :to="{ name: 'login' }"
              >로그인 페이지로 이동
            </router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AccountErrorList from "@/components/Account/AccountErrorList.vue";

export default {
  name: "SignupView",
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: "",
        password1: "",
        password2: "",
      },
    };
  },
  computed: {
    ...mapGetters(["authError"]),
  },
  methods: {
    ...mapActions(["signup"]),
  },
};
</script>

<style>
.signup-div {
  position: relative;
}
label {
  color: aliceblue;
}

.background-image {
  width: 100%;
  opacity: 20;
}
#signup-box {
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
#signup-button {
  width: 100%;
}
#signup-text {
  color: white;
}
#signup-p {
  color: rgb(172, 172, 172);
}
</style>
