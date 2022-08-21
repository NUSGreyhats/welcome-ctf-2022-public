// const TelegramBot = require('node-telegram-bot-api');
import TelegramBot from 'node-telegram-bot-api'
import dotenv from 'dotenv';
import {Database} from './db.js'

import {Console} from 'console'
import fs from 'fs'

const fileLogger = new Console({
    stdout: fs.createWriteStream("./chat.log", {'flags':'a'}),
    stderr: fs.createWriteStream("./chat.err.log", {'flags':'a'})
})

dotenv.config()

async function main() {
    const apiKey = process.env.BOT_API;
    if (!apiKey) {
        throw Error("API KEY NOT FOUND");
    }

    const STATE = {
        START: 0,
        REGISTER_USERNAME: 1,
        REGISTER_PHONE: 2,
        JOIN_TEAM: 3,
        DONE: 4
    }

    let userStates = {}
    let stagingUser = {}
    
    const bot = new TelegramBot(apiKey, {polling: true});
    const db = new Database();


    bot.onText(/^\/echo (.+)/, (msg, match) => {
        const chatId = msg.chat.id;
        const resp = match[1];

        bot.sendMessage(chatId, resp);
    })

    bot.onText(/^\/start/, async (msg) => {
        const chatId = msg.chat.id;
        const welcome = "Welcome to welcome ctf. This is a beta test bot for registrations"
        await bot.sendMessage(chatId, welcome);
        userStates[msg.chat.id] = STATE.REGISTER_USERNAME;
        await bot.sendMessage(chatId, "Please enter your username:")
    })

    const handleUser = async (user) => {
        console.log("Submitting");
        try {
            await db.insertUser(user);
            const members = await db.getTeamMembers(user.userId);
            showTeam(user.userId, members);
        } catch {
            await bot.sendMessage(user.userId, "Internal error, try again by replying /start");
        }
    }

    const showTeam = (chatId, members) => {
        bot.sendMessage(chatId, `Your team members are\n ${members.join("\n")}`);
    }

    const validateTeam = (name) => {
        if (!name) {
            return false;
        }
        const ban = ["drop", "delete", "update", "set"]
        const t = name.toLowerCase()
        const isInvalid = ban.some((word) => t.includes(word))
        return !isInvalid;
    }

    bot.on("message", async (msg) => {
        fileLogger.log(`[${msg.date}] - [${msg.chat.id}] - ${msg.from.username}: ${msg.text}`)
        if (msg.text && msg.text.startsWith('/')) {
            return;
        }

        const chatId = msg.chat.id;
        const curState = userStates[chatId];
        switch (curState) {
            case STATE.REGISTER_USERNAME:
                if (!msg.text) {
                    await bot.sendMessage(chatId, "Invalid name");
                    await bot.sendMessage(chatId, "Please enter name:");
                    return
                }
                stagingUser[msg.chat.id] = {
                    ...stagingUser[msg.chat.id],
                    username: msg.text
                }

                bot.sendMessage(chatId, "Please enter your phone number:")
                userStates[msg.chat.id] = STATE.REGISTER_PHONE;
                break
            case STATE.REGISTER_PHONE:
                const number = parseInt(msg.text)
                if (!number || msg.text.length != 8) {
                    await bot.sendMessage(chatId, "Invalid phone number");
                    await bot.sendMessage(chatId, "Please enter your phone number:");
                    return
                }

                stagingUser[msg.chat.id] = {
                    ...stagingUser[msg.chat.id],
                    phoneNumber: msg.text
                }
                bot.sendMessage(chatId, "Please enter your team:")
                userStates[msg.chat.id] = STATE.JOIN_TEAM;
                break

            case STATE.JOIN_TEAM:
                if (!validateTeam(msg.text)) {
                    await bot.sendMessage(chatId, "Invalid team name")
                    await bot.sendMessage(chatId, "Please enter your team:")
                    return
                }

                stagingUser[msg.chat.id] = {
                    ...stagingUser[msg.chat.id],
                    team: msg.text,
                    userId: msg.chat.id
                }
                userStates[msg.chat.id] = STATE.DONE;
                handleUser(stagingUser[msg.chat.id])
                bot.sendMessage(chatId, "You have completed the registration.")
                break
        }
    })

}

main()