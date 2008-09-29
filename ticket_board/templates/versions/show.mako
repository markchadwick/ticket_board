<h1>${c.version}</h1>

<ul>
    <li>Start</li>
    % for issue in c.issues:
        <li>${issue}</li>
    % endfor
    <li>End</li>
</ul>