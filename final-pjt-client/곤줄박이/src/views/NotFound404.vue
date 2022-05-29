<template>
  <div id="errorpage">
    <div>
      <div>
        <h1 class="mb-3">404 Not Found</h1>
        <h1 class="mb-5">유효하지 않은 페이지 입니다.</h1>
      </div>
      <img
        style="width: 15%"
        class="not-found mt-5"
        src="@/assets/404.png"
        alt="not-found"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "NotFound404",
};
</script>

<style>
img.not-found {
  width: 100%;
}
h1 {
  color: white;
}
#errorpage {
  text-align: center;
  padding: 200px;
}
</style>
