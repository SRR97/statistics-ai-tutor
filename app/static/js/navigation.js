// Navegación entre las secciones académicas de MU

function showSection(sectionId) {
    // Mostrar únicamente la sección seleccionada
    const sections = document.querySelectorAll("[data-section]");

    sections.forEach((section) => {
        section.hidden = section.id !== sectionId;
    });

    // Actualizar el botón activo en la barra lateral
    const navButtons = document.querySelectorAll(
        ".sidebar-navigation button.nav-link"
    );

    navButtons.forEach((button) => {
        const isActive =
            button.getAttribute("onclick") ===
            `showSection('${sectionId}')`;

        button.classList.toggle("active", isActive);
        button.setAttribute("aria-pressed", String(isActive));
    });
}