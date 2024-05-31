<template>
  <div class="page-success">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Спасибо вам!</h1>

        <p>Ваш заказ будет обработан в течение 48 часов.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Success",
  mounted() {
    document.title = "Success | Djackets";
  },
};
</script>
