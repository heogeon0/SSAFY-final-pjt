<template>
  <div class="account-error-list mb-4">
    <div v-for="(errors, field) in authError" :key="field">
      <div>
        <div v-for="(error, idx) in errors" :key="idx">
          <div>{{ error }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "AccountErrorList",
  computed: {
    ...mapGetters(["authError"]),
  },
};
</script>

<style>
.account-error-list {
  color: rgb(236, 76, 76);
}
</style>
