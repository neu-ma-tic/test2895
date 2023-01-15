const discord = require("discord.js");

const filesystem = require("fs");
const colors = require("chalk");

const operation = require("os");

const processID = process.pid; 

const client = new discord.Client(
    {
        fetchAllMembers: true, 
        messageCacheMaxSize: 1000,
        messageCacheLifetime: 30, 
        messageSweepInterval: 60, 
        shardCount: 2 
    }
);

let client_config = require("./client_configurations/client_settings.json");

let client_token = client_config.Client.Token;

let client_prefix = client_config.Client.Prefix;

client.login(client_token);