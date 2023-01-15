package main;

import net.dv8tion.jda.api.EmbedBuilder;
import net.dv8tion.jda.api.entities.MessageEmbed;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import java.awt.*;
import java.util.Collection;


public class Energy extends ListenerAdapter {

    public void onMessageReceived(MessageReceivedEvent event) {
        if (event.getMessage().getContentStripped().equals("!c-int-embeds-energy")) {
            event.getChannel().sendMessageEmbeds((Collection<? extends MessageEmbed>) eenergy());
        }

    }

    private static EmbedBuilder eenergy() {

                EmbedBuilder builder = new EmbedBuilder();
                builder.setColor(Color.magenta);
                builder.setTitle("**Currently Playing:**");
                builder.setDescription("***🎶   Reyfm***");
                builder.addField(" ", "`Clydia bot by Trixi199#0001", true);
                builder.addField(" ", "🎵 ▬▬▬▬🔵▬▬▬▬▬▬▬   1:27 / ♾️", true);
                builder.addField(" ", "❤️    ⏮️    🔀    ⏸️    🔁    ⏭️    🔉  ▬▬", true);
                builder.setThumbnail("https://cdn.discordapp.com/attachments/972568301433659452/972653245946269747/584826e6cef1014c0b5e49da.png");

                return builder;

            }

        }