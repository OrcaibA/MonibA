const service = require("../services/service");

exports.sendMessage = async (req, res) => {

    try {

        const { message } = req.body;

        await service.sendMessage(message);

        return res.json({
            success: true,
            message: "Sent successfully"
        });

    } catch (err) {
        console.error(err);

        return res.status(500).json({
            success: false,
            error: err.message
        });
    }

};

exports.sendImage = async (req, res, next) => {

    try {

        const { message, image } = req.body;

        const buffer = Buffer.from(image, "base64");

        await service.sendImage(message, buffer);

        res.json({
            success: true
        });

    } catch (err) {

        next(err);

    }

};