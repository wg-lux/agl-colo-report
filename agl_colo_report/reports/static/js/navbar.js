// navbar.js

function toggleSidebar() {
    const sidebar = document.getElementById("mySidebar");
    const mainContent = document.getElementById("mainContent");

    if (sidebar.style.width === "0px") {
        sidebar.style.width = "250px";
        mainContent.style.marginLeft = "250px";
    } else {
        sidebar.style.width = "0px";
        mainContent.style.marginLeft = "40px";
    }
}

// Expand the sidebar by default when the page loads
window.onload = function() {
    const sidebar = document.getElementById("mySidebar");
    const mainContent = document.getElementById("mainContent");
    sidebar.style.width = "250px";
    mainContent.style.marginLeft = "250px";
};