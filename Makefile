# kacv fog nowcast
CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -g
BIN = kacv

all: $(BIN)

$(BIN): main.c kacv.h
	$(CC) $(CFLAGS) -o $(BIN) main.c

clean:
	rm -f $(BIN) weight_runner
