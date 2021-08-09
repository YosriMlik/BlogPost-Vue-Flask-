/* eslint-disable */
<template>
<div class="navbar sticky-top" id="nv">    
    <router-link to="/" class="nav-link logo"><a>Blog Post</a></router-link>
    <div v-on:click="permute" id="change">
        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi text-light" viewBox="0 0 16 16">
            <path d="M12 8a4 4 0 1 1-8 0 4 4 0 0 1 8 0zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z"/>
        </svg>
    </div>    
    <router-link class="nav-link" to="/addpost"><a id="addpost">+Post</a></router-link>
</div>
</template>

<script>
let root = document.documentElement;
let c = document.getElementsByClassName('content');
export default {    
    name: "Nav",
    data: function() {
        return {
            dark: true
        }
    },
    methods: {
        permute: function() {
            if(this.dark){
                /* Light */
                this.dark = false;
            } else{
                /* Dark */
                this.dark = true;
            };
        }
    },
    watch: {
        dark: function(d) {
            if(!d){
                /* Light */
                root.style.setProperty('--color', "#000");
                document.getElementById('change').innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-moon-fill" viewBox="0 0 16 16"> <path d="M6 .278a.768.768 0 0 1 .08.858 7.208 7.208 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277.527 0 1.04-.055 1.533-.16a.787.787 0 0 1 .81.316.733.733 0 0 1-.031.893A8.349 8.349 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.752.752 0 0 1 6 .278z"/>  </svg>'
                document.getElementById('bg').style.backgroundColor = '#fff';
                document.getElementById('nv').style.backgroundColor = '#aaddcc7a';                
                for (var i=0; i<c.length; i++){ 
                    c[i].style.backgroundColor = '#f9f3f3';
                    c[i].style.borderLeftColor = "#0042a5";
                };
            } else{
                /* Dark */
                root.style.setProperty('--color', "#fff");
                document.getElementById('change').innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi text-light" viewBox="0 0 16 16"> <path d="M12 8a4 4 0 1 1-8 0 4 4 0 0 1 8 0zM8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0zm0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13zm8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5zM3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8zm10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0zm-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0zm9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707zM4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708z"/> </svg>';     
                document.getElementById('bg').style.backgroundColor = '#212529';
                document.getElementById('nv').style.backgroundColor = '#363b40';
                for (i=0; i<c.length; i++){ 
                    c[i].style.backgroundColor = '#6c757d';
                    c[i].style.borderLeftColor = "#0dcaf0";
                };
            };
        }
    }
};
</script>

<style>
:root{
    --color: #fff;
}
#bg{
  background-color: #212529;
}
.content{  
    color: var(--color);
    margin-top: 10px;
    padding: 13px;
    padding-bottom: .1px;
    background-color: #6c757d;
    font-size: 18px;
    border-left: #0dcaf0 solid;
    border-radius: 3px;
}
#author, #linee, .newpost {
    color: var(--color);
}
</style>


<style lang="css" scoped>
#nv{
    background-color: #363b40;
    padding: 10px 100px;
}
#addpost{
    background-color: #28a745;
    color: #fff;
    text-decoration: none;
    border-radius: 5px;
    padding: 8px 35px;
}
.logo{
    padding: 10px;
    font-size: 20px;
    display: inline;
    color: #0dcaf0;
    font-weight: 500;
}
@media screen and (max-width: 750px) {
    #nv{
        padding: 10px 20px !important;
    }
}
</style>
