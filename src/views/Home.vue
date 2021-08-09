eslint-disable
<template>
  <div class="home">
    <posts v-model="posts" v-for="post in posts" 
    :id="post.id"
    :key="post.id"
    :title="post.title"
    :author="post.author"
    :date="post.date_posted"
    :content="post.content" 
    @clicked="onClickChild" 
     />
  </div>
</template>

<script>
//import axios from 'axios';
import posts from "@/components/posts.vue";
export default {
  name: 'home',
  data() {
    return {
      posts: []
    };
  },
  components: {
    posts
  },
  methods: {
    onClickChild () {
      this.$router.go(this.$router.currentRoute)
    },
    getPosts(){
      fetch("http://localhost:5000/",{
        method: 'GET',
        Headers: {
          "Content-Type": "application/json"
        }
      })
      .then(resp => resp.json())
      .then(data => {
        this.posts.push(...data)
      })
      .catch(error => {
        console.log(error)
      })

    },
  },
  created() {
    this.getPosts();
  },
};
</script>
