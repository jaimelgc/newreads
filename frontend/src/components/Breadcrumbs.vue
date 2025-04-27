<script setup lang="ts">
    import { computed } from 'vue'
    import { useRoute } from 'vue-router'

    const route = useRoute()

    const breadcrumbs = computed(() => {
    const crumbs: { label: string; to: string }[] = []

    // Example logic: Build breadcrumbs from matched routes
    route.matched.forEach((r) => {
        if (r.meta?.breadcrumb) {
        crumbs.push({
            label: r.meta.breadcrumb as string,
            to: r.path,
        })
        }
    })

    return crumbs
    })
</script>

<template>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb">
        <li
          v-for="(crumb, index) in breadcrumbs"
          :key="index"
          class="breadcrumb-item"
          :class="{ active: index === breadcrumbs.length - 1 }"
        >
          <router-link v-if="index !== breadcrumbs.length - 1" :to="crumb.to">{{ crumb.label }}</router-link>
          <span v-else>{{ crumb.label }}</span>
        </li>
      </ol>
    </nav>
</template>