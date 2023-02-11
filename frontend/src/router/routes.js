import Vue from 'vue';
import VueRouter from 'vue-router';
import HomePage from "../components/HomePage.vue";
import MyBlogs from "../components/MyBlogs.vue";
import FrontPage from "../components/FrontPage.vue"
import AuthViews from "../components/auth_comps/AuthViews.vue"
// import App from "../App.vue";
// import base from "../components/navbar.vue";
Vue.use(VueRouter);

export default new VueRouter({
    mode:'history',
    routes: [
        {
            path: "/login",
            name: 'loginView',
            component: AuthViews,
        },
        {
            path: "/signup",
            name: "signupView",
            component: AuthViews,
        },
        {
            path: "/:username/homepage",
            name: "Homepage",
            component: HomePage
        },
        {
            path: "/:username/my-blogs",
            name: "MyBlogs",
            component: MyBlogs,
        },
        {
            path: "/",
            name: "LandingPage",
            component: FrontPage
        }
    ],
})