import "jquery";

import "../../src/scss/index.scss";

import "./dashboard/ProjectListingApp";

import "./global_topbar/MFB_dropdown";

if (import.meta.hot) {
    import.meta.hot.accept(({ module }) => {
        import.meta.hot.invalidate();
    });
}
