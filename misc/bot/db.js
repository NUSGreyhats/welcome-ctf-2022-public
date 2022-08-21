import sqlite3 from 'sqlite3';
import {open} from 'sqlite';

const THE_FLAG = "greyhats{Th4nk_y0u_f0r_pl4y1ng!}"

class Database {
    constructor() {
        this.init();
    }

    async openDb() {
        return open({
            filename: './users.db',
            driver: sqlite3.Database
        })
    }

    init() {
        this.openDb().then((db) => {
            db.exec(`
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY NOT NULL,
                    username TEXT NOT NULL, 
                    phone_number int NOT NULL,
                    team TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS flag (
                    id INTEGER PRIMARY KEY NOT NULL,
                    flag TEXT NOT NULL
                );
                INSERT INTO flag (id, flag) VALUES(1, "${THE_FLAG}")
                ON CONFLICT(id) DO UPDATE SET
                flag=excluded.flag;
            `)
        })
    }

    async insertUser(user) {
        const db = await this.openDb()
        const query = await db.prepare(
            `
            INSERT INTO users (user_id, username, phone_number, team) VALUES(?, ?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
            username=excluded.username,
            phone_number=excluded.phone_number,
            team=excluded.team;
            `, 
            user.userId, 
            user.username, 
            user.phoneNumber, 
            user.team
        );
        await query.run();
    }

    async getTeamMembers(userId) {
        const db = await this.openDb()
        const query = `
            SELECT team FROM users WHERE user_id=${userId};
        `
        // console.log(query)
        let team = (await db.get(query)).team;
        if (team) {
            const query2 = `
                SELECT username FROM users WHERE team="${team}";
            `
            // console.log(query2)
            const members = (await db.all(query2)).map(r => r.username);
            return members;
        }

        return undefined
    }
}

export {Database}