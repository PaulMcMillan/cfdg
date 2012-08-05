SRC=$(wildcard *.cfdg)
OBJS=$(SRC:.cfdg=.png)

all: $(OBJS)


%.png: %.cfdg
	cfdg -s 750x750 $^ $@

clean:
	rm *.png

.PHONY: run run-changed

run-changed:
	while true; do make 1>/dev/null; sleep .3; done

# force remake even if targets exist
run:
	while true; do make -B 1>/dev/null; sleep 1; done
