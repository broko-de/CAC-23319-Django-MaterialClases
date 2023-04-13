const renderProyecto = (proyecto) => {
    html = `
        <div class="col">
            <div class="card shadow-sm">
                <img class="bd-placeholder-img card-img-top" width="100%" src="${proyecto.portada}"
                    alt="${proyecto.autor}" width="20%">
                <div class="card-body">
                    <a href="${proyecto.url}" target="_blank"><h3>${proyecto.autor}</h3></a>
                </div>
            </div>
        </div>
    `;
    return html;
}

const divProyectos = document.querySelector("#divProyectos");

fetch('/api_proyectos')
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
    let proyectos = data.data;
    proyectos.forEach(proyecto => {
        let html = renderProyecto(proyecto);
        divProyectos.insertAdjacentHTML('beforeend', html);
    });
  });