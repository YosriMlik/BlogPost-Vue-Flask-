<template>
    <div class="container">
        <form @submit.prevent="verif" method="POST">
            <br>
            <h1 class="text-center">Edit Your Post</h1>
            <br>
            <router-link to="/"><a class="btn btn-danger">&laquo; Previous</a></router-link>
            <br> <br>
            <h2 v-text="title"></h2>
            <h5>By: <b v-text="author"></b></h5>
            <div v-if="errors.length" class="alert alert-danger pb-0" role="alert">
                <b>Please correct the following error(s):</b>
                <ul>
                    <li v-for="error in errors" :key="error">{{error}}</li>
                </ul>
            </div>
            <input v-model="new_title" class="form-control" maxlength="100" name="title" id="title" type="text" placeholder="New title">
            <br>
            <textarea v-model="new_content" name="content" class="form-control" id="content" rows="6" cols="80" placeholder="What's in your mind ?"></textarea>
            <br>
            <input type="submit" value="Save" class="btn btn-primary">
        </form>
    </div>
</template>

<script>
export default {
    name: "edit",
    data: function() {
        return {
            errors: [],
            id: 0,
            title: '',
            new_title: '',
            author: '',
            new_content: ''
        }
    },
    created() {
        this.id = this.$route.params.id;
        this.title = this.$route.params.title;
        this.author = this.$route.params.author;
    },
    methods: {
    edit: function(){
      fetch(`http://localhost:5000/edit/${this.id}/`,{
        method: 'POST',
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: this.new_title,
            content: this.new_content,
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
        console.log('verif')
        this.errors = [];
        let formats = ['/','*','#','+','^','$','!',':',';',',','?','&','<','>','[',']','{', '}'];
        let b = true;
        
        for (let i=0; i<formats.length; i++) {
            console.log(this.new_title)
            if(this.new_title.includes(formats[i])){
                b = false;
            }
        }
        if(!b) { this.errors.push("No special characters [ /  *  #  +  ^  $  !  :  ;  ?  &  <  >  [  ]  {   }  ]"); }

        if(this.new_title && isNaN(this.new_title) && this.new_content && b){ 
            this.edit();
            return true; 
        } else{
            if(!this.new_title){
                this.errors.push("Title is required");
            }
//      -----------------  
            let t = parseFloat(this.new_title);
            if(!isNaN(t)){
                this.errors.push("Title is not a number");
            }
//      -----------------           
            if(!this.new_content){
                this.errors.push("Content is required");
            }
            f.preventDefault();
        }
    }
    }
};
</script>

<style>

h1, h2, h5 {
    color: var(--color);
}
</style>