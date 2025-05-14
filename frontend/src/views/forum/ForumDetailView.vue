<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  import axios from 'axios';

  interface Comment {
    id: number;
    content: string;
    poster: { username: string } | null;
    created_at: string;
    quoted_post?: Comment | null;
    }

  interface Post {
    id: number;
    title: string;
    content: string;
    poster: { username: string } | null;
    created_at: string;
    comments: Comment[];
  }

  const route = useRoute();
  const post = ref<Post | null>(null);
  const newComment = ref('');
  const quotedCommentId = ref<number | null>(null);

  const fetchPost = async () => {
  const res = await axios.get(`/api/posts/${route.params.id}/`);
    post.value = res.data;
  };

  const submitComment = async () => {
  try {
    await axios.post('/api/comments/', {
      content: newComment.value,
      original_post: post.value?.id,
      quoted_post: quotedCommentId.value,
    });
    newComment.value = '';
    quotedCommentId.value = null;
    await fetchPost(); // refresh comments
  } catch (error) {
    console.error(error);
  }
  };

onMounted(fetchPost);
</script>

<template>
  <div v-if="post">
    <h2>{{ post.title }}</h2>
    <p><strong>{{ post.poster?.username || 'Unknown' }}</strong> - {{ new Date(post.created_at).toLocaleString() }}</p>
    <p>{{ post.content }}</p>

    <h3>Comments</h3>
    <ul>
      <li v-for="comment in post.comments" :key="comment.id" style="margin-bottom: 1em;">
        <div style="border: 1px solid #ccc; padding: 10px;">
          <p><strong>{{ comment.poster?.username || 'Unknown' }}</strong> said:</p>
          <p>{{ comment.content }}</p>
          <p><small>{{ new Date(comment.created_at).toLocaleString() }}</small></p>
          <button @click="quotedCommentId = comment.id">Reply</button>

          <!-- Reply Info -->
          <div v-if="comment.quoted_post" style="margin-top: 5px; padding-left: 10px; border-left: 2px solid #999;">
            <small>Replying to {{ comment.quoted_post.poster?.username || 'Unknown' }}: "{{ comment.quoted_post.content }}"</small>
          </div>
        </div>
      </li>
    </ul>

    <!-- New Comment Form -->
    <div style="margin-top: 2em;">
      <h4>Leave a Comment</h4>
      <div v-if="quotedCommentId" style="margin-bottom: 0.5em;">
        <strong>Replying to comment #{{ quotedCommentId }}</strong>
        <button @click="quotedCommentId = null" style="margin-left: 10px;">Cancel</button>
      </div>
      <textarea v-model="newComment" placeholder="Write your comment..." rows="3" style="width: 100%;"></textarea>
      <button @click="submitComment">Post Comment</button>
    </div>
  </div>
</template>