package main;

import net.dv8tion.jda.api.entities.Emoji;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import net.dv8tion.jda.api.interactions.components.selections.SelectMenu;

public class MenuCommand extends ListenerAdapter {

    public void onMessageReceived(MessageReceivedEvent event) {

        if (event.getMessage().getContentStripped().equals("!c.menu")) {
            event.getChannel().sendTyping().queue();
            event.getChannel().sendMessage("Menu:").setActionRow(sendInformations()).queue();
        }

    }

    private static SelectMenu sendInformations() {
        return SelectMenu.create("infos")
                .setPlaceholder("Wähle die Station")
                .addOption("Energy", "energy", "Klicke um Energy zu Spielen", Emoji.fromUnicode("▶"))
                .addOption("1Live", "1live", "Klicke um 1Live zu Spielen", Emoji.fromUnicode("▶"))
                .addOption("Reyfm", "reyfm", "Klicke um Reyfm zu Spielen", Emoji.fromUnicode("▶"))
                .setRequiredRange(1, 1)
                .build();
    }

}
