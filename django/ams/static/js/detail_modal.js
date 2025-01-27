function mostrarDetalhes(title, details) {
  document.getElementById("exampleModalLabel").innerText = title;

  for (const [key, value] of Object.entries(details)) {
    console.log(`${key}: ${value}`);
  }

  // Preenche o corpo do modal com as informações do cliente
  document.getElementById("modal-body").innerHTML = `
      <p><strong>Telefone:</strong> ${phone}</p>
      <p><strong>Anotações:</strong> ${annotations}</p>`;
}

console.log("caiu aqui");
