<h1>Projects</h1>

<ul>
    % for project in c.projects:
        <li><a href="/projects/show/${project.id}">${project.name}</a></li>
    % endfor
</ul>