// Smooth scroll pour les liens de navigation et footer
$(function () {
    $(".navbar a, footer a").on("click", function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;
            $('body').animate({ scrollTop: $(hash).offset().top }, 900, function () {
                window.location.hash = hash;
            });
        }
    });

    // Formulaire de contact — envoi AJAX avec feedback visuel
    $('#contact-form').submit(function (e) {
        e.preventDefault();
        $('.comments').empty();

        // Feedback visuel sur le bouton
        const submitBtn = this.querySelector('input[type="submit"]');
        const originalValue = submitBtn.value;
        submitBtn.value = 'Envoi en cours...';
        submitBtn.disabled = true;

        var postdata = $('#contact-form').serialize();

        $.ajax({
            type: 'POST',
            url: 'php/contact.php',
            data: postdata,
            dataType: 'json',
            success: function (result) {
                if (result.isSuccess) {
                    // Correction : .append() au lieu de .appende()
                    $("#contact-form").append("<p class='thank-you'>Votre message a bien été envoyé. Merci de m'avoir contacté :)</p>");
                    $("#contact-form")[0].reset();
                } else {
                    $("firstname + .comments").html(result.firstnameError);
                    $("name + .comments").html(result.nameError);
                    $("email + .comments").html(result.emailError);
                    $("phone + .comments").html(result.phoneError);
                    $("message + .comments").html(result.messageError);
                }
            },
            error: function () {
                $("#contact-form").append("<p class='thank-you' style='color:red;'>Une erreur est survenue. Veuillez réessayer.</p>");
            },
            complete: function () {
                submitBtn.value = originalValue;
                submitBtn.disabled = false;
            }
        });
    });
});

// Bouton scroll-to-top (déclaré une seule fois)
const scrollToTopBtn = document.createElement('div');
scrollToTopBtn.innerHTML = '<span class="fa-solid fa-arrow-up"></span>';
scrollToTopBtn.className = 'scroll-to-top';
document.body.appendChild(scrollToTopBtn);

window.addEventListener('scroll', () => {
    scrollToTopBtn.style.opacity = (window.scrollY > 300) ? 1 : 0;
});

scrollToTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});
