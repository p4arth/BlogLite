import Vue from 'vue';
import VueRouter from 'vue-router';
import HomePage from "../components/HomePage.vue";
import MyBlogs from "../components/user_blogs/MyBlogs.vue";
import FrontPage from "../components/FrontPage.vue"
import UserProfile from "../components/UserProfile.vue";
import PublishArea from "../components/PublishArea.vue";
import EditBlog from "../components/EditBlog.vue";
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
        },
        {
            path: "/:username/publish",
            name: "Publish",
            component: PublishArea
        },
        {
            path: "/:username/edit/post/:post_id",
            name: "EditBlog",
            component: EditBlog
        }
    ],
})