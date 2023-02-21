BIN_DIR="$$HOME/.local/bin"
DATA_DIR="$$HOME/.local/share"

install:
	mkdir -p $(DATA_DIR)/min
	cp src/* $(DATA_DIR)/min/
	cp min $(BIN_DIR)/
	cp min-client $(BIN_DIR)/
	chmod +x $(BIN_DIR)/min $(BIN_DIR)/min-client

uninstall:
	rm -rf $(DATA_DIR)/min
	rm $(BIN_DIR)/min /usr/local/bin/min-client
