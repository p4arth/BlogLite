import Vue from 'vue';
import VueRouter from 'vue-router';
import FrontView from '../components/FrontView.vue';
Vue.use(VueRouter);

export default new VueRouter({
    mode:'history',
    routes:[
        {
            path:'/api/login',
            name:'FrontView',
            component: FrontView,
        }
    ],
})