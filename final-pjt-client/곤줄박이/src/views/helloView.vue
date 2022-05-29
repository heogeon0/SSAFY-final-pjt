<template>
  <div id="temp">
    <div id="temp-2">
      <img
        class="background-image"
        src="@/assets/background.png"
        alt="background image"
      />
    </div>
    <div id="temp-box" class="text-center">
      <h4>지금 뭐보지?!</h4>
      <h5>더 이상 고민할 필요 없어요.</h5>
      <br />
      <h5>국내 영화부터 명작 애니메이션까지</h5>
      <h5>NEXTLEVEL만의 추천 알고리즘으로</h5>
      <h4>취향저격 영화보기!</h4>
      <br />
      <br />
      <button class="btn btn-warning">
        <router-link aria-current="page" :to="{ name: 'login' }"
          >1초만에 가입해보세요
        </router-link>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "tempVue",
};
</script>

<style>
#temp {
  position: relative;
}
#temp-2 {
  opacity: 0.6;
}
#temp-box {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
}
</style>