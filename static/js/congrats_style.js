/* by rikanutyy */
document.addEventListener('DOMContentLoaded', function () {
    const card = document.getElementById('interactive-card');

    // Add event listener for tap/click
    card.addEventListener('click', function () {
        // Toggle the 'hover' class on click/tap
        card.classList.toggle('hover');
    });
});