<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6 hero-custom">
      <div class="hero-body has-text-centered">
        <p class="title mb-6 title-custom">
          Совершайте покупки на Cornhub!
        </p>
        <p class="subtitle subtitle-custom">
          Лучший онлайн-магазин сельхоз техники
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered new-arrivals-title">
          Новые поступления
        </h2>
      </div>

      <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>

<style scoped>
.hero-custom {
  background: linear-gradient(135deg, #ff4824 0%, #ffb217 100%);
  color: #ffffff;
}

.title-custom {
  font-family: "Arial Black", Gadget, sans-serif;
  font-size: 2.5rem;
  text-shadow: 2px 2px 4px #000000;
}

.subtitle-custom {
  font-family: "Comic Sans MS", cursive, sans-serif;
  font-size: 1.5rem;
}

.new-arrivals-title {
  font-family: "Georgia", serif;
  color: #ff802c;
  margin-bottom: 2rem;
  text-shadow: 1px 1px 2px #aaaaaa;
}

.columns.is-multiline {
  padding: 2rem;
  background-color: #f5f5f5;
}

.column {
  padding: 1rem;
}

.ProductBox {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.ProductBox:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}
</style>

<script>
import axios from "axios";

import ProductBox from "@/components/ProductBox";

export default {
  name: "Home",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {
    ProductBox,
  },
  mounted() {
    this.getLatestProducts();

    document.title = "Home | Djackets";
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("/api/v1/latest-products/")
        .then((response) => {
          this.latestProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
