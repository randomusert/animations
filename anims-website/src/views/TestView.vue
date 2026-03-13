<script setup>

import videoFile from '@/anims/vid.mp4'
</script>

<template>
  <main>

    <video controls width="600">
    <source :src="videoFile" type="video/mp4">
  </video>

  </main>
</template> 