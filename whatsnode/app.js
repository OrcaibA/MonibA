const express = require("express");
const cors = require("cors");

const routes = require("./routes/routes");
const errorHandler = require("./middlewares/error");

const app = express();

app.use(cors());

app.use(express.json({
    limit: "10mb"
}));

app.use("/api/whatsapp", routes);

app.use(errorHandler);

module.exports = app;