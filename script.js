// ===== SMOOTH SCROLL — tous les liens internes =====
$(function () {
    $(document).on('click', 'a[href^="#"]', function (e) {
        var hash = this.hash;
        if (!hash || hash === '#') return;
        var $target = $(hash);
        if ($target.length) {
            e.preventDefault();
            $('html, body').animate({ scrollTop: $target.offset().top - 80 }, 700);
        }
    });

    // ===== FORMULAIRE CONTACT — mailto (pas de PHP en local) =====
    $('#contact-form').on('submit', function (e) {
        e.preventDefault();

        var name    = $.trim($('#name').val());
        var email   = $.trim($('#email').val());
        var subject = $.trim($('#subject').val());
        var message = $.trim($('#message').val());

        // Validation
        var valid = true;
        ['#name', '#email', '#subject', '#message'].forEach(function (sel) {
            var el = $(sel);
            if (!el.val().trim()) { el.css('border', '2px solid #dc3545'); valid = false; }
            else { el.css('border', ''); }
        });
        if (!valid) { showContactMsg('Veuillez remplir tous les champs.', 'danger'); return; }

        // Ouvrir le client mail
        var bodyTxt = 'Nom: ' + name + '\nEmail: ' + email + '\n\n' + message;
        var mailto  = 'mailto:claverkouakou1@gmail.com'
                    + '?subject=' + encodeURIComponent(subject)
                    + '&body='    + encodeURIComponent(bodyTxt);

        window.location.href = mailto;
        showContactMsg("Votre client mail va s'ouvrir. Merci !", 'success');
        this.reset();
    });

    function showContactMsg(text, type) {
        $('.contact-feedback').remove();
        var $p = $('<p class="contact-feedback fw-bold mt-3 text-center"></p>')
            .text(text).css('color', type === 'success' ? '#28a745' : '#dc3545');
        $('#contact-form').append($p);
        setTimeout(function () { $p.remove(); }, 5000);
    }
});

// ===== BOUTON SCROLL-TO-TOP (grand, bleu, visible) =====
(function () {
    // Crée le bouton dynamiquement
    var btn = document.createElement('button');
    btn.id = 'scrollToTopBtn';
    btn.setAttribute('aria-label', 'Retour en haut');
    btn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    document.body.appendChild(btn);

    window.addEventListener('scroll', function () {
        btn.classList.toggle('visible', window.scrollY > 300);
    });

    btn.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
})();

// ===== Three.js — particules section Projets =====
function initProjectParticles() {
    var canvas = document.getElementById('particles-3d');
    if (!canvas || typeof THREE === 'undefined') return;

    var renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
    var scene    = new THREE.Scene();
    var camera   = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

    var count     = window.innerWidth < 768 ? 150 : 400;
    var positions = new Float32Array(count * 3);
    for (var i = 0; i < count * 3; i++) { positions[i] = (Math.random() - 0.5) * 10; }

    var geo    = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    var mat    = new THREE.PointsMaterial({ size: 0.02, color: 0xffffff, transparent: true, opacity: 0.6 });
    var points = new THREE.Points(geo, mat);
    scene.add(points);
    camera.position.z = 3;

    (function animate() {
        requestAnimationFrame(animate);
        points.rotation.y += 0.001;
        renderer.render(scene, camera);
    })();

    window.addEventListener('resize', function () {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });
}

$(document).ready(initProjectParticles);
