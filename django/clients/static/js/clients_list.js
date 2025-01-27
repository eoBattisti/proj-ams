console.log(client_data);

console.log(typeof client_data);

const obj = JSON.parse(client_data);
console.log(obj);

document.addEventListener("DOMContentLoaded", function () {
  new gridjs.Grid({
    columns: [
      "name",
      "Nome",
      "Telefone",
      "Anotações",
      {
        name: "Ações",
        formatter: (_, row) => {
          const clientId = row.cells[0].client_data;
          const clientName = row.cells[1].client_data;
          const clientPhone = row.cells[2].client_data;
          const clientAnnotations = row.cells[3].client_data;

          return gridjs.html(`
              <button
              class="btn btn-primary btn-sm"
                data-bs-toggle="modal"
                data-bs-target="#exampleModal"
                onclick="mostrarDetalhes('')">
                Detalhes
              </button>
              <button
              class="btn btn-danger btn-sm"
              data-bs-toggle="modal"
              data-bs-target="#deleteModal"
              onclick="confirmDelete('${clientId}')">
              Excluir
            </button>
            `);
        },
      },
    ],
    data: [client_data],
    pagination: 2,
    search: true,
    sort: true,
    language: {
      search: {
        placeholder: "🔍 Search...",
      },
    },
  }).render(document.getElementById("tabela-clientes"));
});
