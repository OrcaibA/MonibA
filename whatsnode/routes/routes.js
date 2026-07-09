const router = require("express").Router();

const controller = require("../controllers/controller");

router.post("/sendMessage", controller.sendMessage);

router.post("/send-image", controller.sendImage);

module.exports = router;