<script setup lang="ts">
    import { defineProps, ref, computed } from 'vue';

    const props = defineProps({
        book: Object
    })

    const showFullDescription = ref(false)

    const toggleFullDescription = () => {
        showFullDescription.value = !showFullDescription.value
    }

    const truncateDescription = computed(() => {
        let description = props.book.description; // check description? ERROR ts
        if (!showFullDescription.value) {
            description = description.substring(0,90) + '...';
        }
        return description;
    });

</script>