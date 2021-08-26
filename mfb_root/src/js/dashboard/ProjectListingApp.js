// import vue app in .html page
import { createApp } from 'vue';
import App from '../../vue/ProjectListingApp.vue';

const app = createApp(App);
app.mount('#project_listing_app');

// Hot Module Replacement (HMR) - Remove this snippet to remove HMR.
// Learn more: https://www.snowpack.dev/concepts/hot-module-replacement
if (import.meta.hot) {
  import.meta.hot.accept();
  import.meta.hot.dispose(() => {
    app.unmount();
  });
}

var eGridDiv = document.querySelector('#project_listing_app');
eGridDiv.style.setProperty('width', '100%');
eGridDiv.style.setProperty('height', '100%');
