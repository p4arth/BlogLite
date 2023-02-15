import Vue from 'vue';
import VueRouter from 'vue-router';
import HomePage from "../components/HomePage.vue";
import MyBlogs from "../components/user_blogs/MyBlogs.vue";
import FrontPage from "../components/FrontPage.vue"
import UserProfile from "../components/UserProfile.vue";
// import AuthViews from "../components/auth_comps/AuthViews.vue"
// import App from "../App.vue";
// import base from "../components/navbar.vue";
Vue.use(VueRouter);

export default new VueRouter({
    mode:'history',
    routes: [
        {
            path: "/login",
            name: 'loginView',
            component: FrontPage,
        },
        {
            path: "/signup",
            name: "signupView",
            component: FrontPage,
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
            path: "/:username/profile",
            name: "Profile",
            component: UserProfile,
        },
        {
            path: "/",
            name: "LandingPage",
            component: FrontPage
        }
    ],
})