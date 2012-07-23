SRC=$(wildcard *.cfdg)
OBJS=$(SRC:.cfdg=.png)

all: $(OBJS)

%.png: %.cfdg
	cfdg $^ $@

clean:
	rm *.png