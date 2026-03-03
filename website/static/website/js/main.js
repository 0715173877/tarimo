// Main JavaScript for interactive features

// Auto-play carousels
document.addEventListener('DOMContentLoaded', function() {
    // Initialize any carousels
    var serviceCarousel = document.getElementById('serviceCarousel');
    if (serviceCarousel) {
        new bootstrap.Carousel(serviceCarousel, {
            interval: 5000,
            wrap: true,
            pause: 'hover'
        });
    }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Form validation for complaint button
const complaintBtn = document.querySelector('.complaint-btn');
if (complaintBtn) {
    complaintBtn.addEventListener('click', function(e) {
        // Optional: Add tracking or analytics
        console.log('Complaint button clicked');
    });
}