<script setup lang="ts">
    import { defineProps, ref, computed } from 'vue';


    interface Book {
        title: string
        author?: string
        description: string
        // add more fields as needed
    }

    const props = defineProps<{ book: Book }>()

    // og JS
    
    // const props = defineProps({
    //     book: Object
    // })

    const showFullDescription = ref(false)

    const toggleFullDescription = () => {
        showFullDescription.value = !showFullDescription.value
    }

    const truncateDescription = computed(() => {
        let description = props.book.description;
        if (!showFullDescription.value) {
            description = description.substring(0,90) + '...';
        }
        return description;
    });

</script>

<template>
    <div class="bg-white rounded-xl shadow-md relative">
        <div class="p-4">
            <div class="mb-6">
                <div class="text-gray-600 my-2">{{ book.title }}</div>
            </div>
            <div class="mb-5">
                {{ truncateDescription }}
                <button @click="toggleFullDescription" class="text-green-500 hover:text-green-600">
                    {{ showFullDescription ? 'See Less' : 'See More' }}
                </button>
            </div>
            <!-- <RouterLink :to="'/jobs/' + job.id" class="h-[36px] bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-lg text-center text-sm">
                Read More
            </RouterLink> -->
        </div>
    </div>
</template>