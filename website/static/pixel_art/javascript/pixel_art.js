let slideIndex = 1;

function openModal(name) {
    let modal = document.getElementById(`myModal ${name}`);
    modal.style.display = "block";
    slideIndex = 1
    showSlides(slideIndex, name);
}

function closeModal(name) {
    let modal = document.getElementById(`myModal ${name}`);
    modal.style.display = "none";
}

function plusSlides(n, name) {
    showSlides(slideIndex += n, name);
}

function showSlides(n, name) {
    let i
    let slides = document.getElementsByClassName(`img${name}`)
    console.log(`img${name}`)
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    console.log(slides.length, slideIndex, n)
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex-1].style.display = "block";
    console.log(slideIndex)
}