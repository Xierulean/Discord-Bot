const Discord = require('discord.js');
const client = new Discord.Client();

client.login('bot token here');


client.on('ready', () => {
  console.log('Ready for commands!');
});

client.on('message', (message) => {
  if (message.content.startsWith('ping')) {
    message.channel.send('pong!');
  }
});


