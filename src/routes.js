import home from "./pages/Home.vue";
import about from "./pages/About.vue";
import offers from "./pages/Offers.vue";
import blog from "./pages/Blog.vue";
import contacts from "./pages/Contacts.vue";

import searchPage from "./pages/SearchPage.vue";
import postPage from "./pages/SinglePost.vue";
import itemPage from "./pages/SingleItem.vue";
import notFound from "./pages/404.vue";

const routes = [
    { path: '/404', alias: '*', component: notFound},

    { path: "/home", component: home },
    { path: "/about", component: about },
    { path: "/offers", component: offers },
    { path: "/blog", component: blog },
    { path: "/contacts", component: contacts },

    { path: "/search/:id", component: searchPage },
    { path: "/post/:id", component: postPage },
    { path: "/item/:id", component: itemPage }
];

export default routes;