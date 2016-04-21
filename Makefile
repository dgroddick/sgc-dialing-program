CC=gcc
CFLAGS=-Wall -Werror -std=c99 
SRC=stargate.c
TARGET=stargate
LIBS=allegro-5 allegro_main-5


stargate:
	$(CC) $(CFLAGS) $(SRC) -o $(TARGET) `pkg-config --cflags --libs $(LIBS)`

clean:
	rm $(TARGET) 
