<template>
  <div class="column is-3">
    <div class="box product-box">
      <figure class="image mb-4 product-image">
        <img v-bind:src="product.get_thumbnail" />
      </figure>

      <div class="product-info">
        <h3 class="is-size-4 product-name">{{ product.name }}</h3>
        <div class="price-button-container">
          <p class="is-size-6 has-text-grey">
            ₽ {{ formatPrice(product.price) }}
          </p>
          <router-link
            v-bind:to="product.get_absolute_url"
            class="button is-dark"
            >Перейти</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductBox",
  props: {
    product: Object,
  },
  methods: {
    formatPrice(price) {
      // Округление цены до целого числа
      const roundedPrice = Math.floor(price); // или Math.round(price) для округления
      // Регулярное выражение для разделения пробелами между тысячами
      return roundedPrice.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    },
  },
};
</script>

<style scoped>
.product-box {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
}

.product-image {
  width: 100%;
  padding-top: 75%; /* Формат 4:3 */
  position: relative;
  overflow: hidden;
}

.product-image img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product-info {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
}

.product-name {
  margin-bottom: 10px;
  line-height: 1.3;
  min-height: 3.2em;
}

.price-button-container {
  margin-top: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
