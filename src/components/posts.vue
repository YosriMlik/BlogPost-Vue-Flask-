<template>
    <div class="container">
        <br>
        <h2 style="color: blueviolet;">{{title}}</h2>
            <small id="author">
                By: <b class="pe-1">{{author}}</b>&nbsp;
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-clock" viewBox="0 0 16 16">
                    <path d="M8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71V3.5z"/>
                    <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm7-8A7 7 0 1 1 1 8a7 7 0 0 1 14 0z"/>
                </svg> : {{date}}
            </small>
        <br>
        <ul style="list-style-type:none">
            <div class="content">
                <li>
                    <p>{{content}}</p>
                </li>
            </div>
        </ul>
        <router-link :to="{name: 'edit', params: {id: id, title: title, author: author }}"><a class="btn btn-primary me-3" >Edit</a></router-link>
        <a class="btn btn-danger" @click="this.delete">Delete</a>
        <br>
        <hr id="linee">
    </div>
</template>

<script>
export default {
    name: "posts",
    props: ["id", "title", "author", "content", "date"],
    methods: {
    delete: function(){
      console.log('Deleting');
      fetch(`http://localhost:5000/delete/${this.id}`,{
        method: 'DELETE',
        headers: {
          "Content-Type": "application/json"
        }
      })
      .then(() => {
        this.$emit('clicked')
      })
      .catch(error => {
        console.log(error)
      })
      
    },
    /*getPosts(){
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

    },*/

    },
    
};
</script>
