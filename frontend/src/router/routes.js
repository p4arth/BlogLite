import Vue from 'vue';
import VueRouter from 'vue-router';
import loginView from '../components/loginView.vue';
import signupView from "../components/signupView.vue";
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
        }
    ],
})