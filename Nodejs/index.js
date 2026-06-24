import express from "express";
import OpenAI from "openai";
import fs from "fs/promises";
import cors from "cors";
const app = express();
app.use(express.json());
app.use(cors());

const client = new OpenAI({
    baseURL: "https://openrouter.ai/api/v1",
    // apiKey: ""
});
app.get("/chat", async (req, res) => {
    try {
        const prompt = req.query.prompt?.trim();

        if (!prompt) {
            return res.status(400).json({
                message: "Invalid query!"
            });
        }

        const stream = await client.chat.completions.create({
            model: "openrouter/owl-alpha",
            stream: true,
            messages: [
                {
                    role: "user",
                    content: prompt
                }
            ]
        });

        res.setHeader("Content-Type", "text/plain");
        res.setHeader("Transfer-Encoding", "chunked");

        for await (const chunk of stream) {
            const content =
                chunk.choices?.[0]?.delta?.content || "";

            if (content) {
                res.write(content); // send chunk directly
            }
        }

        res.end();
    }
    catch (error) {
        console.error(error);
        res.status(500).end();
    }
});

app.listen(8080);