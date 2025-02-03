
const table = document.getElementById("tabela-clientes");
var url = table.getAttribute("data-url");
var nextButtonLabel = table.getAttribute("data-next-button-label");
var previousButtonLabel = table.getAttribute("data-previous-button-label");
var searchPlaceholder = table.getAttribute("data-search-placeholder");

document.addEventListener("DOMContentLoaded", function () {
  new gridjs.Grid({
    columns: [
      { id: "name", name: "Nome", sort: true }, 
      { id: "phone", name: "Telefone", sort: false },
      {
        id: "actions",
        name: "Ações",
        sort: false,
        width: "20%",
        formatter: (_, row) => {
            console.log("Row:", row.cells);
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
              onclick="confirmDelete()">
              Excluir
            </button>
            `);
        },
      },
    ],
    server: {
      url: url,
      then: data => data.data.map(obj => [
        obj.name,
        obj.phone,
      ]),
      total: data => data.total
    },
    pagination: {
      enabled: true,
      limit: 10,
      server: {
        url: (prev, page, limit) => `${url}?page=${page}&pageSize=${limit}`,
        total: data => data.total
      }, 
    },
    search: true,
    sort: true,
    language: {
      search: {
        placeholder: searchPlaceholder,
      },
      pagination: {
        previous: previousButtonLabel,
        next: nextButtonLabel,
      },
    },
  }).render(table);
});
