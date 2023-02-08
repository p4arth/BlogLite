import Vue from 'vue';
import VueRouter from 'vue-router';
import loginView from '../components/loginView.vue';
import signupView from "../components/signupView.vue";
import HomePage from "../components/HomePage.vue";
// import App from "../App.vue";
// import base from "../components/navbar.vue";
Vue.use(VueRouter);

export default new VueRouter({
    mode:'history',
    routes: [
        {
            path: "/login",
            name: 'loginView',
            component: loginView,
        },
        {
            path: "/signup",
            name: "signupView",
            component: signupView,
        },
        {
            path: "/:username/homepage",
            name: "Homepage",
            component: HomePage
        },
        // {
        //     path: "/:username/publish_new_article",
        //     name: "NewArticle",
        //     componet: App,
        // }
    ],
})