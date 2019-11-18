import home from "./pages/Home.vue";
import about from "./pages/About.vue";
import stores from "./pages/Stores.vue";
import offers from "./pages/Offers.vue";
import blog from "./pages/Blog.vue";
import corporate from "./pages/Corporate.vue";

import categoryPage from "./pages/CategoryPage.vue";
import notFound from "./pages/404.vue";



const routes = [
    { path: '/404', alias: '*', component: notFound},

    { path: "/home", component: home },
    { path: "/about", component: about },
    { path: "/stores", component: stores },
    { path: "/offers", component: offers },
    { path: "/blog", component: blog },
    { path: "/corporate", component: corporate },

    { path: "/category/:id", component: categoryPage }
];

export default routes;