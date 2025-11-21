const express = require("express");
const { spawn } = require("child_process");
const path = require("path");

const app = express();
const PORT = 3000;

// serve static files
app.use("/static", express.static(path.join(__dirname, "static")));

// homepage
app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "templates/index.html"));
});

// scan route
app.get("/scan", (req, res) => {
    const target = req.query.target;

    let python;
    if (target) {
        // Manual IP scan
        python = spawn("python", ["scanner.py", target]);
    } else {
        // Auto network scan
        python = spawn("python", ["scanner.py"]);
    }

    python.stdout.on("data", (data) => {
        try {
            const json = JSON.parse(data.toString());
            res.json(json);
        } catch (err) {
            console.log("JSON parse error:", err);
        }
    });

    python.stderr.on("data", (data) => {
        console.error("PYTHON ERROR:", data.toString());
    });
});

app.listen(PORT, () => {
    console.log("Server running on http://localhost:" + PORT);
});
