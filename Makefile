.PHONY: install uninstall

BIN_DIR=/usr/local/bin
DATA_DIR=/usr/local/share/min/

DATA_FILES=$(subst src/,$(DATA_DIR),$(wildcard src/*))
BIN_FILES=$(addprefix $(BIN_DIR)/,$(wildcard min*))
REQ_XDOTOOLS := $(if $(shell which xdotool),,$(error "xdotool is not installed!"))
REQ_DMENU := \
			 $(if $(shell which rofi),\
			 	$(info rofi installation detected. Configuring for use with rofi ...),\
			 	$(if $(shell which dmenu),\
					$(info dmenu installation detected. Configuring for use with dmenu ...);\
					$(shell sed -i 's/rofi -dmenu/dmenu/' min-recover),\
			 		$(error "Please install either rofi or dmenu!")))


install: $(DATA_FILES) $(BIN_FILES)

$(DATA_FILES): $(DATA_DIR)
	cp -r src/$(@F) $@ && chmod 755 $@

$(DATA_DIR):
	mkdir $@ && chmod 777 $@

$(BIN_FILES): $(BIN_DIR)/%: ./%
	cp $< $@ && chmod 755 $@

uninstall:
	rm -rf $(DATA_DIR)
	rm $(BIN_FILES)

define requirements_installed
	$(warning "Installing requirements ...")
endef

