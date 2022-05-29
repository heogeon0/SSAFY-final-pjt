<template>
  <div>
    <div id="community-nav-div"></div>
    <div id="community-nav">
      <div
        id="good"
        class="no-active"
        @click="changeActive(0)"
        @mouseover="setActive"
        @mouseout="setNoActive($event, 0)"
      >
        <h4>핫게시판</h4>
      </div>
      <div
        id="good"
        class="no-active"
        @click="changeActive(1)"
        @mouseover="setActive"
        @mouseout="setNoActive($event, 1)"
      >
        <h4>영화리뷰</h4>
      </div>
      <div
        id="good"
        class="no-active"
        @click="changeActive(2)"
        @mouseover="setActive"
        @mouseout="setNoActive($event, 2)"
      >
        <h4>영화정보</h4>
      </div>
      <div
        id="good"
        class="no-active"
        @click="changeActive(3)"
        @mouseover="setActive"
        @mouseout="setNoActive($event, 3)"
      >
        <h4>자유게시판</h4>
      </div>
    </div>
  </div>
</template>

<script>
import router from "@/router";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "CommunityNav",
  methods: {
    ...mapActions(["setCategory"]),

    changeActive(num) {
      const nav_list = document.querySelectorAll('#good')
      nav_list.forEach((nav,idx) => {
        if (idx===num) {
          nav.className = "yes-active"
          console.log(nav)
        } else if (idx !== num) {
          nav.className = "no-active"
          console.log(nav)
        }
      })
      router.push({ name: "communities" });
      this.setCategory(num);
    },

    setActive(event) {
      event.target.className = "yes-active";
    },
    setNoActive(event,num) {
      if (num != this.nowCategory)
      event.target.className = "no-active";
    },
  },
  computed: {
    ...mapGetters(["nowCategory"]),
  },
};
</script>

<style>
#community-nav {
  display: flex;
  justify-content: space-around;
  align-items: center;
  width: 1000px;
  margin: 10px auto;
  height: 50px;
  background-color: rgb(80, 80, 80);
  border-radius: 15px;
}
#btn {
  color: white;
  padding-bottom: 0px;
}

.no-active {
  color: rgba(210, 208, 208);
  border-bottom: 3px solid rgb(152, 111, 0);
  height: 35px;
}
.yes-active {
  cursor: pointer;
  color: white;
  border-bottom: 3px solid rgb(255, 187, 0);
  height: 35px;
}

#community-nav-div {
  width: 100vw;
  height: 200px;
  background-image: url("@/assets/backgroundnav.png");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  overflow: hidden;
}
</style>