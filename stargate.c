#include <stdio.h>
#include <allegro5/allegro.h>
#include <allegro5/allegro_image.h>
#include <allegro5/allegro_native_dialog.h>

int main(int argc, char *argv[])
{
    ALLEGRO_DISPLAY *display = NULL;
    ALLEGRO_BITMAP *stargate = NULL;
    ALLEGRO_BITMAP *symbols[7];
    ALLEGRO_EVENT_QUEUE *event_queue = NULL;


    if(!al_init()) {
      al_show_native_message_box(display, "Error", "Error", "Failed to initialize allegro!", NULL, ALLEGRO_MESSAGEBOX_ERROR);
      return 0;
    }

    display = al_create_display(800,600);
    if(!display) {
      al_show_native_message_box(display, "Error", "Error", "Failed to initialize display!", NULL, ALLEGRO_MESSAGEBOX_ERROR);
      return 0;
    }

    event_queue = al_create_event_queue();
    if(!event_queue) {
      fprintf(stderr, "failed to create event_queue!\n");
      al_destroy_display(display);
      return -1;
    }

    al_register_event_source(event_queue, al_get_display_event_source(display));

    if(!al_init_image_addon()) {
      al_show_native_message_box(display, "Error", "Error", "Failed to initialize al_init_image_addon!", NULL, ALLEGRO_MESSAGEBOX_ERROR);
      return 0;
    }

    stargate = al_load_bitmap("stargate.png");
    if(!stargate) {
      al_show_native_message_box(display, "Error", "Error", "Failed to load image!", NULL, ALLEGRO_MESSAGEBOX_ERROR);
      al_destroy_display(display);
      return 0;
    }

    symbols[0] = al_load_bitmap("glyphs/glyph27.gif");
    symbols[1] = al_load_bitmap("glyphs/glyph07.gif");
    symbols[2] = al_load_bitmap("glyphs/glyph15.gif");
    symbols[3] = al_load_bitmap("glyphs/glyph32.gif");
    symbols[4] = al_load_bitmap("glyphs/glyph12.gif");
    symbols[5] = al_load_bitmap("glyphs/glyph30.gif");
    symbols[6] = al_load_bitmap("glyphs/glyph01.gif");


    while(1) {
      ALLEGRO_EVENT ev;
      ALLEGRO_TIMEOUT timeout;
      al_init_timeout(&timeout, 0.06);

      bool get_event = al_wait_for_event_until(event_queue, &ev, &timeout);

      if(get_event && ev.type == ALLEGRO_EVENT_DISPLAY_CLOSE) {
         break;
      }
      al_draw_bitmap(stargate, 10, 10,0);

      int symbol_x = 650;
      int symbol_y = 5;
      for (int i = 0; i < 7; i++) {
        al_draw_bitmap(symbols[i], symbol_x, (symbol_y+= 70), 0);
      }

      al_flip_display();
    }

    al_destroy_display(display);
    al_destroy_bitmap(stargate);
    al_destroy_bitmap(*symbols);
    al_destroy_event_queue(event_queue);

    return 0;
}
