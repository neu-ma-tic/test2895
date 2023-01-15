package main;

import net.dv8tion.jda.api.events.interaction.component.SelectMenuInteractionEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import java.io.File;

public class MenuCommandSelection extends ListenerAdapter {

    public void onSelectMenuInteraction(SelectMenuInteractionEvent event) {


        if (event.getComponent().getId().equals("infos")) {

            for (int i = 0; i < event.getValues().size(); i++)

                switch (event.getValues().get(i)) {

                    case "energy":
                        File __energy = new File("C:\\Users\\pasca\\Desktop\\MeinDiscordBot\\_energy.png");
                        event.getUser().openPrivateChannel().queue( privateChannel -> privateChannel.sendFile(__energy));
                        break;

                    case "1live":
                        event.getUser().openPrivateChannel().queue( privateChannel -> privateChannel.sendMessage("***Nowplaying: 1Live - Der beste Mix!***").queue());
                        break;

                    case "reyfm":
                        event.getUser().openPrivateChannel().queue( privateChannel -> privateChannel.sendMessage("***Nowplaying: Reyfm - #HITSONLY***").queue());
                        break;


                    default:
                        break;
                }

        }

        event.reply("Die ausgewählte Station wird gleich Abgespielt!").setEphemeral(true).queue();

    }

}
