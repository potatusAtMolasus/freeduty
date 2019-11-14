import about from "./components/about.vue";
import home from "./components/home.vue";
import categoryPage from "./components/categoryPage.vue";
import notFound from "./components/404.vue";
import catalog from "./components/catalog.vue";

const routes = [
    { path: "*", component: notFound },
    { path: "/home", component: home },
    { path: "/catalog", component: catalog },
    { path: "/about", component: about },
    { path: "/category/:id", component: categoryPage }
];

export default routes;