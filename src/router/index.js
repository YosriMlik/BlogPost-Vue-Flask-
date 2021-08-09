import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import newPost from "../views/new-post.vue";
import edit from '../views/edit.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/addpost",
    name: "newPost",
    component: newPost,
  },
  {
    path: "/edit/:id/",
    name: "edit",
    component: edit,
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
