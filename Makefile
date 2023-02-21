BIN_DIR="$$HOME/.local/bin"
DATA_DIR="$$HOME/.local/share"

install:
	mkdir -p $(DATA_DIR)/min
	cp src/* $(DATA_DIR)/min/
	cp -p min min-client min-minimize min-recover min-list $(BIN_DIR)/

uninstall:
	rm -rf $(DATA_DIR)/min
	rm $(BIN_DIR)/min $(BIN_DIR)/min-client $(BIN_DIR)/min-minimize $(BIN_DIR)/min-recover $(BIN_DIR)/min-list
