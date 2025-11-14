document.getElementById("formDoacao").addEventListener("submit", function (event) {
  event.preventDefault();

  const nome = document.querySelector("input[name='nome']").value.trim();
  const email = document.querySelector("input[name='email']").value.trim();
  const valor = document.querySelector("input[name='valor']").value.trim();
  const formaPagamento = document.querySelector("select[name='forma-pagamento']").value;
  const mensagemResultado = document.getElementById("mensagem-resultado");

  // Validações (sem restrição de caracteres no nome)
  if (!email.includes("@")) {
    mensagemResultado.textContent = "Erro: O email deve conter '@' corretamente.";
    mensagemResultado.style.color = "red";
    return;
  }

  if (nome && email && valor && formaPagamento) {
    mensagemResultado.textContent = "Doação enviada com sucesso! Muito obrigado pela sua contribuição.";
    mensagemResultado.style.color = "green";
  } else {
    mensagemResultado.textContent = "Erro: Preencha todos os campos obrigatórios corretamente.";
    mensagemResultado.style.color = "red";
  }
});

// Botões de valores sugeridos
document.querySelectorAll(".valor-btn").forEach(btn => {
  btn.addEventListener("click", function () {
    const valorInput = document.querySelector("input[name='valor']");
    if (this.textContent.includes("Outro")) {
      valorInput.value = "";
      valorInput.focus();
    } else {
      valorInput.value = this.textContent.replace("R$", "").trim();
    }
  });
});

