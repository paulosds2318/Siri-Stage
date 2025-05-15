/* Formulário Candidatos */
const candidateForm = document.getElementById("candidate-form");
if (candidateForm) {
    candidateForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const form = this;
        const senhaInput = form.querySelector("#senha");
        const senhaConfirmaInput = form.querySelector("#senhaConfirma");
        const senha = senhaInput.value;
        const senhaConfirma = senhaConfirmaInput.value;
        const erroSenha = form.querySelector(".erro-senha");

        if (senha !== senhaConfirma) {
            senhaConfirmaInput.classList.add("incorreto");
            erroSenha.style.display = 'block';
        } else {
            senhaConfirmaInput.classList.remove("incorreto");
            erroSenha.style.display = 'none';
            window.location.href = "vagas.html";
        }
    });
}

/* Formulário Empresas */
const enterpriseForm = document.getElementById("enterprise-form");
if (enterpriseForm) {
    enterpriseForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const form = this;
        const senhaInput = form.querySelector("#senha");
        const senhaConfirmaInput = form.querySelector("#senhaConfirma");
        const senha = senhaInput.value;
        const senhaConfirma = senhaConfirmaInput.value;
        const erroSenha = form.querySelector(".erro-senha");

        if (senha !== senhaConfirma) {
            senhaConfirmaInput.classList.add("incorreto");
            erroSenha.style.display = 'block';
        } else {
            senhaConfirmaInput.classList.remove("incorreto");
            erroSenha.style.display = 'none';
            window.location.href = "criar_vagas.html";
        }
    });
}
