(() => {
 var anchorLink = document.querySelector("a[href='#topButton']"),
target = document.getElementById("mainHeader");
anchorLink.addEventListener("click", function(e) {
    if (window.scrollTo) {
        e.preventDefault();
        window.scrollTo({"behavior": "smooth", "top": target.offsetTop});
    }
})
})();