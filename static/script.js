function autoScan() {
    document.getElementById("output").innerHTML = "<p>Scanning network...</p>";

    fetch("/scan")
        .then(res => res.json())
        .then(data => showTable(data));
}

function manualScan() {
    const target = document.getElementById("target").value;
    if (!target) return alert("Enter an IP address");

    document.getElementById("output").innerHTML = "<p>Scanning target...</p>";

    fetch("/scan?target=" + target)
        .then(res => res.json())
        .then(data => showTable(data));
}

function showTable(data) {
    let html = `
        <table class="table table-dark table-striped mt-4">
            <thead>
                <tr>
                    <th>IP</th>
                    <th>Hostname</th>
                    <th>MAC</th>
                </tr>
            </thead>
            <tbody>
    `;

    data.forEach(row => {
        html += `
            <tr>
                <td>${row.ip}</td>
                <td>${row.hostname}</td>
                <td>${row.mac}</td>
            </tr>
        `;
    });

    html += "</tbody></table>";

    document.getElementById("output").innerHTML = html;
}
