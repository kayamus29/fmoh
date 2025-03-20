function initializeHeaderScripts() {
    // Reinitialize header-specific plugins
    if (typeof $.fn.slicknav !== 'undefined') {
        $('.mobile-nav').slicknav({
            prependTo: '.mobile-nav'
        });
    }
}

function initializeFooterScripts() {
    // Reinitialize footer-specific scripts if needed
}