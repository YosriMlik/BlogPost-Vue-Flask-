/* eslint-disable */
<template>
    <div class="container newpost">
        <h2 class="text-center">Add a post</h2>
        <br>
        <router-link to="/"><a class="btn btn-danger">&laquo; Previous</a></router-link>
        <br> <br>
        <form @submit.prevent="verif" method="POST" class="mb-5">
            <h4>Title: </h4>
            <div v-if="errors.length" class="alert alert-danger pb-0" role="alert">
                <b>Please correct the following error(s):</b>
                <ul>
                    <li v-for="error in errors" :key="error">{{error}}</li>
                </ul>
            </div>
            <input v-model="title" class="form-control" maxlength="100" name="title" id="title" type="text" placeholder="New title">
            <br>
                
            <h4>Author: </h4>
            <input v-model="author" class="form-control" maxlength="20" name="author" id="author" type="text" placeholder="New author" style="color: #000;">
            <br>
               
            <h4>Content: </h4>
            <textarea v-model="content" name="content" class="form-control" id="content" rows="6" cols="80" placeholder="What's in your mind ?"></textarea>
            <br>

            <input type="submit" value="Post" class="btn btn-primary">
        </form>
    </div>
</template>

<script>
//import axios from 'axios';
export default {
    name: "new-post",
    data: function() {
        return {
            errors: [],
            title: '',
            author: '',
            content: '',
        }
    },
    methods: {
    add: function(){
      fetch("http://localhost:5000/add-post/",{
        method: 'POST',
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: this.title,
            author: this.author,
            content: this.content,
        })
      })
      .then(resp => resp.json())
      .then( () => {
        this.$router.push({ name: 'Home' })
      })
      .catch(error => {
        console.log(error)
      })
    },
    verif: function(f) {
        this.errors = [];
        let formats = ['/','*','#','+','^','$','!',':',';',',','?','&','<','>','[',']','{', '}'];
        let b = true;
        
        for (let i=0; i<formats.length;i++) {
            let s = String(this.title);
            let s2 = String(this.author);
            if(s.includes(formats[i]) || s2.includes(formats[i])){
                b = false;
            }
        }
        if(!b) { this.errors.push("No special characters [ /  *  #  +  ^  $  !  :  ;  ?  &  <  >  [  ]  {   }  ]"); }

        if(this.title && isNaN(this.title) && this.author && isNaN(this.author) && this.content && isNaN(this.content) && b){ 
            this.add();
            return true; 
        } else{
            if(!this.title){
                this.errors.push("Title is required");
            }
//      -----------------  
            let t = parseFloat(this.title);
            if(!isNaN(t)){
                this.errors.push("Title is not a number");
            }
//      -----------------           
            if(!this.author){
                this.errors.push("Author is required");
            }
            let a = parseFloat(this.author);
            if(!isNaN(a)){
                this.errors.push("Author is not a number"); 
            }
//      ---------------
            if(!this.content){
                this.errors.push("Content is required");
            }
            f.preventDefault();
        }
    }
    }
}
</script>