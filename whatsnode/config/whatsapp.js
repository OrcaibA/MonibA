const { Client, LocalAuth } = require("whatsapp-web.js");
const env = require("./env");

const client = new Client({

    authStrategy: new LocalAuth({

        clientId: env.clientId

    }),

    puppeteer: {

        executablePath: env.chromePath,

        headless: env.headless,

        args: [
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu"
        ]
    }

});

module.exports = client;