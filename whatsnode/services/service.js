const client = require("../config/whatsapp");
const { MessageMedia } = require("whatsapp-web.js");
const env = require("../config/env");

class Service {

    async sendMessage(message) {

        try {

            await client.sendMessage(env.groupId, message);

            return true;

        } catch (err) {

            throw new Error(`Failed to send message: ${err.message}`);

        }

    }

    async sendGroupMessage(message) {

        return client.sendMessage(env.groupId, message);

    }

    async sendImage(message, imageBuffer) {

        const media = new MessageMedia(

            "image/png",

            imageBuffer.toString("base64"),

            "image.png"

        );

        return client.sendMessage(env.groupId, media, {

            caption: message

        });

    }

    async sendByGroupName(groupName, message) {

        const chats = await client.getChats();

        const group = chats.find(chat =>

            chat.isGroup ||
            chat.name.trim().toLowerCase() === groupName.trim().toLowerCase()

        );

        if (!group)
            throw new Error("Group not found");

        return group.sendMessage(message);
    }

}

module.exports = new Service();