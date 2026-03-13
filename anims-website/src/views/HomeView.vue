<script setup lang="ts">
import 'vidstack/bundle'
import type { MediaPlayerElement } from 'vidstack/elements';
import { onBeforeUnmount, ref } from 'vue';

const player = ref<MediaPlayerElement>(null);

onBeforeUnmount(() => {
  // This call will destroy the player and all child instances.
  player.value.destroy();
});
</script>

<template>
  <main>
    <media-player title="animations" src="@/anims/vid.mp4" keep-alive ref="player">
      <media-provider></media-provider>
    </media-player>
  </main>
</template>
