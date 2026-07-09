// const express = require("express");
// const cors = require("cors");
// const qrcode = require("qrcode-terminal");
// const { Client, LocalAuth } = require("whatsapp-web.js");

// const app = express();

// app.use(cors());
// app.use(express.json());

// const client = new Client({
//     authStrategy: new LocalAuth({
//         clientId: "moniba"
//     }),

//     puppeteer: {
//         executablePath: "/usr/lib/chromium/chromium",
//         headless: false,

//         args: [
//             "--no-sandbox",
//             "--disable-setuid-sandbox",
//             "--disable-dev-shm-usage",
//             "--disable-gpu",
//             "--disable-software-rasterizer",
//             "--disable-extensions",
//             "--window-size=1366,768"
//         ]
//     }
// });

// client.on("loading_screen", (percent, message) => {
//     console.log(percent + "%", message);
// });

// client.on("qr", qr => {
//     console.clear();
//     console.log("Scan QR Code\n");
//     qrcode.generate(qr, { small: true });
// });

// client.on("authenticated", () => {
//     console.log("✅ Authenticated");
// });

// client.on("auth_failure", msg => {
//     console.log("❌ Auth Failure:", msg);
// });

// client.on("ready", () => {
//     console.log("==================================");
//     console.log("✅ WhatsApp Ready");
//     console.log("==================================");
// });

// client.on("disconnected", reason => {
//     console.log("Disconnected:", reason);
// });

// client.initialize();

// async function sendGroupMessage(groupName, message) {

//     const chats = await client.getChats();

//     const group = chats.find(chat =>
//         chat.isGroup &&
//         chat.name.trim().toLowerCase() === groupName.trim().toLowerCase()
//     );

//     if (!group) {
//         throw new Error("Group not found");
//     }

//     await group.sendMessage(message);

//     return true;
// }

// app.post("/send", async (req, res) => {

//     try {

//         const { group, message } = req.body;

//         await sendGroupMessage(group, message);

//         res.json({
//             success: true,
//             message: "Message sent successfully"
//         });

//     } catch (err) {

//         console.error(err);

//         res.status(500).json({
//             success: false,
//             error: err.message
//         });

//     }

// });

// const GROUP_ID = "test";

// app.post("/send-group", async (req, res) => {
//     const { message, imagePath } = req.body;

//     console.log("MESSAGE:", message);
//     console.log("IMAGE PATH:", imagePath);

//     try {
//         const media = await MessageMedia.fromFilePath(imagePath);

//         await client.sendMessage(GROUP_ID, media, {
//             caption: message
//         });

//         res.send({ status: "sent" });

//     } catch (err) {
//         console.error("WHATSAPP ERROR:", err);
//         res.status(500).send({
//             error: err.message,
//             stack: err.stack
//         });
//     }
// });

// const { MessageMedia } = require("whatsapp-web.js");

// app.use(express.json({ limit: "10mb" })); // IMPORTANT

// app.post("/send-group-buffer", async(req,res)=>{

//     try {

//         const {message,image}=req.body;


//         const buffer = Buffer.from(image);


//         const media = new MessageMedia(
//             "image/png",
//             buffer.toString("base64"),
//             "case.png"
//         );


//         const chat = await client.getChatById(GROUP_ID);


//         await chat.sendMessage(media,{
//             caption:message
//         });


//         res.json({
//             status:"sent"
//         });


//     }catch(err){

//         console.error(err);

//         res.status(500).json({
//             error:String(err)
//         });
//     }

// });

// app.get("/", (req, res) => {

//     res.json({
//         status: "running",
//         whatsapp: client.info ? "connected" : "connecting"
//     });

// });

// app.listen(3000, () => {

//     console.log("🚀 WhatsApp API Running");
//     console.log("http://localhost:3000");

// });

const app = require("./app");
const env = require("./config/env");
const client = require("./config/whatsapp");
const qrcode = require("qrcode-terminal");

client.on("qr", (qr) => {
    console.log("Scan the QR code:");
    qrcode.generate(qr, { small: true });
});

client.on("authenticated", () => {
    console.log("Authenticated");
});

client.on("ready", async () => {
    console.log("WhatsApp Ready");

//     const chats = await client.getChats();

//     console.log("\n===== GROUPS =====");

//     chats
//         .filter(chat => chat.isGroup)
//         .forEach(chat => {
//             console.log(`Name : ${chat.name}`);
//             console.log(`ID   : ${chat.id._serialized}`);
//             console.log("--------------------------------");
//         });

//     console.log("=====================\n");
});

client.on("disconnected", (reason) => {
    console.log("Disconnected:", reason);
});

client.initialize();

app.listen(env.port, () => {
    console.log(`Server running on ${env.port}`);
});