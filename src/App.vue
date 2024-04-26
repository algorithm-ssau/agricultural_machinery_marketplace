<script setup>
import Header from './component/Header.vue'
import UnderHeader from './component/UnderHeader.vue'
import CatImage from './component/CatImage.vue'
import Card from './component/Card.vue'
</script>
<template>
  <div class="bg-gray-800 w-full h-1/4 m-auto">
    <Header />
    <UnderHeader />
    <CatImage />
    <div class="bg-slate-200">
      <Card />
    </div>
  </div>
</template>
