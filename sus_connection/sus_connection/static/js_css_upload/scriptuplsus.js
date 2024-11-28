function uploadSUScartao() {
    const suscartaoInput = document.getElementById("sus_cartao");
    const suscartaoImage = document.getElementById("sus_cartao_image");

    const file = suscartaoInput.files[0];
    const reader = new FileReader();

    reader.onload = function(event) {
        const image = document.createElement("img");
        image.src = event.target.result;
        suscartaoImage.innerHTML = "";
        suscartaoImage.appendChild(image);
    }

    reader.readAsDataURL(file);
}
