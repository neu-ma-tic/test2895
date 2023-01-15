module.exports = {
  name: "ws",
  run: async (app, m, args, prefix, id) => {
    m.reply(
      {
        content: `WebSocket Ping \`${app.ws.ping}ms\``
      }
    );
  }
}
