<h1>${ c.project.name }</h1>

<ul>
    % for version in c.versions:
        <li>
            <a href="/versions/show/${version.id}?project_id=${c.project.id}">
                ${version.name}
            </a>
        </li>
    % endfor
</ul>