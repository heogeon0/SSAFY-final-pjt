<template>
  <div>
    <div v-if="bools">
      <form @submit.prevent="score_update">
        <div class="d-flex">
          <div class="d-flex">
            <div class="d-flex mt-1">
              <label for="score">평점 :</label>
              <div class="star-rating space-x-4 mx-2">
                <input
                  type="radio"
                  id="5-stars"
                  name="rating"
                  value="5"
                  v-model="number"
                />
                <label for="5-stars" class="star pr-4">★</label>
                <input
                  type="radio"
                  id="4-stars"
                  name="rating"
                  value="4"
                  v-model="number"
                />
                <label for="4-stars" class="star">★</label>
                <input
                  type="radio"
                  id="3-stars"
                  name="rating"
                  value="3"
                  v-model="number"
                />
                <label for="3-stars" class="star">★</label>
                <input
                  type="radio"
                  id="2-stars"
                  name="rating"
                  value="2"
                  v-model="number"
                />
                <label for="2-stars" class="star">★</label>
                <input
                  type="radio"
                  id="1-star"
                  name="rating"
                  value="1"
                  v-model="number"
                />
                <label for="1-star" class="star">★</label>
              </div>
            </div>
            <br />

            <div class="d-flex justify-content-end mt-1">
              <label for="review"> </label
              ><input
                class="review-input form-control vote-detail"
                type=""
                id="review"
                v-model="content"
              />
              <button class="btn btn-outline-warning vote-detail">
                <p id="text-smaller">수정하기</p>
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>
    <div v-else>
      <form @submit.prevent="reviewSubmit">
        <div class="d-flex">
          <div class="d-flex">
            <div class="d-flex mt-1">
              <label for="score">평점 :</label>
              <div class="star-rating space-x-4 mx-2">
                <input
                  type="radio"
                  id="5-stars"
                  name="rating"
                  value="5"
                  v-model="number"
                />
                <label for="5-stars" class="star pr-4"> ★</label>
                <input
                  type="radio"
                  id="4-stars"
                  name="rating"
                  value="4"
                  v-model="number"
                />
                <label for="4-stars" class="star">★</label>
                <input
                  type="radio"
                  id="3-stars"
                  name="rating"
                  value="3"
                  v-model="number"
                />
                <label for="3-stars" class="star">★</label>
                <input
                  type="radio"
                  id="2-stars"
                  name="rating"
                  value="2"
                  v-model="number"
                />
                <label for="2-stars" class="star">★</label>
                <input
                  type="radio"
                  id="1-star"
                  name="rating"
                  value="1"
                  v-model="number"
                />
                <label for="1-star" class="star">★</label>
              </div>
            </div>
            <br />

            <div class="d-flex justify-content-end mt-1">
              <label for="review"> </label
              ><input
                class="review-input form-control vote-detail"
                type=""
                id="review"
                v-model="content"
              />
              <button class="btn btn-outline-warning vote-detail">
                <p id="text-smaller">작성하기</p>
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "MovieReviewForm",
  data() {
    return {
      number: 0,
      content: "",
      scorePk: "",
    };
  },
  props: {
    moviePk: Number,
    scores: Array,
  },
  computed: {
    ...mapGetters(["currentUser"]),
    bools() {
      for (let i = 0; i < this.scores.length; i++) {
        if (this.scores[i].user.username === this.currentUser.username) {
          // this.scorePk = this.scores[i].pk
          return true;
        }
      }
      return false;
    },
  },
  methods: {
    ...mapActions(["setMovieScore", "updateMoiveScore"]),
    reviewSubmit() {
      this.setMovieScore({
        moviePk: this.moviePk,
        number: this.number,
        content: this.content,
      });
      (this.number = 0), (this.content = "");
    },
    score_update() {
      for (let i = 0; i < this.scores.length; i++) {
        if (this.scores[i].user.username === this.currentUser.username) {
          this.updateMoiveScore({
            moviePk: this.moviePk,
            scorePk: this.scores[i].pk,
            number: this.number,
            content: this.content,
          });
        }
      }
    },
  },
};
</script>

<style>
#text-smaller {
  font-size: 11.5px;
}
#score {
  width: 50px !important;
}
#review {
  width: 300px !important;
}
.star-rating {
  display: flex;
  flex-direction: row-reverse;
  font-size: 1.5rem;
  line-height: 1.5rem;
  justify-content: space-around;
  padding: 0 0.2em;
  text-align: center;
  width: 5em;
}

.star-rating input {
  display: none;
}
.vote-detail {
  height: 30px;
}
.star-rating label {
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 0.3px;
  -webkit-text-stroke-color: #ffffff;
  cursor: pointer;
}

.star-rating :checked ~ label {
  -webkit-text-fill-color: gold;
}

.star-rating label:hover,
.star-rating label:hover ~ label {
  -webkit-text-fill-color: #fff58c;
}
</style>