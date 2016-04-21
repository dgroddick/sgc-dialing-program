CC=gcc
CFLAGS=-Wall -Werror -g -std=c99 
SRC=stargate.c
TARGET=stargate
LIBS=allegro-5 allegro_main-5 allegro_image-5 allegro_dialog-5


stargate:
	$(CC) $(CFLAGS) $(SRC) -o $(TARGET) `pkg-config --cflags --libs $(LIBS)`

clean:
	rm $(TARGET) 
