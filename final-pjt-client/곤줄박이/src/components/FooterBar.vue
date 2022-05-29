<template>
  <!-- Footer -->
  <footer id="footer">
    <section>
      <div class="text-center text-md-start mt-5">
        <div class="d-flex flex-row mb-3">
          <div md="3" lg="4" xl="3" class="mx-auto mb-4">
            <h6 class="text-uppercase fw-bold mb-4">NextLevel</h6>
            <p>맞춤형 영화를 제공하는 영화 추천 서비스입니다.</p>
            <p>현재 상영 중인 유명작부터, 명작, 개인추천까지!</p>
            <p>지금 홈페이지를 통해 만나보세요.</p>
          </div>
          <div md="2" lg="2" xl="2" class="mx-auto mb-4">
            <h6 class="text-uppercase fw-bold mb-4">SITE MAP</h6>
            <p>
              <a href="http://localhost:8080/" class="text-reset">HOME</a>
            </p>
            <p>
              <a href="http://localhost:8080/recommendation" class="text-reset"
                >Recommendations</a
              >
            </p>
            <p>
              <a href="http://localhost:8080/communities" class="text-reset"
                >Review</a
              >
            </p>
            <p>
              <a href="#!" class="text-reset">Log-in/Sign-up</a>
            </p>
          </div>
          <div md="3" lg="2" xl="2" class="mx-auto mb-4">
            <h6 class="text-uppercase fw-bold mb-4">Used Skills</h6>
            <p>Python</p>
            <p>Django</p>
            <p>HTML/CSS/JavaScript</p>
            <p>Vue</p>
          </div>

          <div md="4" lg="3" xl="3" class="mx-auto mb-md-0 mb-4">
            <h6 class="text-uppercase fw-bold mb-4">SSAFY Gumi 3</h6>
            <p>ChaeRi Kim</p>
            <p>DongWook Lee</p>
            <p>GeonNyeong Heo</p>
          </div>
        </div>
      </div>
    </section>
    <div class="text-center p-4" style="background-color: rgba(0, 0, 0, 0.05)">
      © 2022 Copyright:
      <a class="text-reset fw-bold">NextLevel</a>
    </div>
  </footer>
</template>

<script>
export default {
  name: "FooterBar",
};
</script>

<style>
#footer {
  color: rgb(123, 123, 123);
}
</style>