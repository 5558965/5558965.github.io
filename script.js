$(function(){

    $(".navbar a,footer a") .on("click", function(event){

        event.preventDefault();
        var hash = this.hash;
        $('body').animate({scrollTop: $(hash).offset().top} , 900 , function(){window.location.hash = hash;})
    });
}) 
    $('#contact-form') .submit(function(e){

        e.preventDefault();
        $('.comments').empty();
        var postdata = $('#contact-form').serialize();
    
    $.ajax({
        type: 'POST',
        url: 'php/contact.php',
        data: postdata,
        dataType: 'json',
        success: function(result) {

            if(result.isSuccess)
            {
                $("#contact-form").appende("<p class='thank-you'>Votre message a bien été envoyé. Merci de m'avoir contacté:)</p>");
                $("#contact-form")[0].reset();
            }
            else
            {
                $("firstname + .comments").html(result.firstnameError);
                $("name + .comments").html(result.nameError);
                $("email + .comments").html(result.emailError);
                $("phone + .comments").html(result.phoneError);
                $("message + .comments").html(result.messageError);
            }
            }
            
            }
            
    );
});


// Dans script.js
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


document.getElementById('contact-form').addEventListener('submit', function(e) {
  e.preventDefault();
  const submitBtn = this.querySelector('input[type="submit"]');
  submitBtn.value = 'Envoi en cours...';
  submitBtn.disabled = true;
  
  // Simulation d'envoi
  setTimeout(() => {
    this.submit();
  }, 1500);
});



// Dans script.js
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