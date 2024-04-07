<template>
  <div class="bg-slate-950 w-full h-16 flex justify-between px-32">
    <div>
      <button class="h-16"><img src="/src/public/buttoncatalog.svg" alt="Button" /></button>
    </div>
    <ul class="flex items-center pl-96 gap-3">
      <li class="flex items-center gap-4">
        <a href="https://www.example.com/link1"><img src="/src/public/insta.svg" alt="Link" /></a>
      </li>
      <li class="flex items-center gap-4">
        <a href="https://www.example.com/link2"><img src="/src/public/vk.svg" alt="Link" /></a>
      </li>
      <li class="flex items-center gap-4">
        <a href="https://www.example.com/link3"
          ><img src="/src/public/facebook.svg" alt="Link"
        /></a>
      </li>
    </ul>
    <form class="pt-2">
      <div class="position-relative">
        <input
          type="text"
          name="catolog"
          id="catolog"
          placeholder="Поиск по каталогу"
          class="h-11 w-60 rounded pl-12 pr-3"
        />
        <img
          class="absolute top-24 bottom-0 left-256 m-1 h-5 w-5"
          src="/src/public/search.svg"
          alt="Image"
        />
      </div>
    </form>
  </div>
</template>
