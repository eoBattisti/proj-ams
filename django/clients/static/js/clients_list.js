
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
          return gridjs.html(`
              <a
              class="btn btn-secondary btn-md"
              href="/clients/${row.cells[2].data}/">
                <i class="bi bi-file-text"></i>
              </a>
              <a
                class="btn btn-primary btn-md"
              href="/clients/update/${row.cells[2].data}/">
                <i class="bi bi-pencil"></i>
              </a>
              <button
              class="btn btn-danger btn-md"
              data-bs-toggle="modal"
              data-bs-target="#deleteModal"
              onclick="confirmDelete()">
              <i class="bi bi-trash"></i>
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
        obj.id,
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
