require("dotenv").config();

module.exports = {
    port: process.env.PORT || 3000,

    clientId: process.env.CLIENT_ID,

    chromePath: process.env.CHROME_PATH,

    groupId: process.env.GROUP_ID,

    headless: process.env.HEADLESS === "true",

    nodeEnv: process.env.NODE_ENV
};