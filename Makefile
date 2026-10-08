.PHONY: serve build check clean

THEME ?= microclub-modern
HUGO = hugo --theme "$(THEME)"

serve:
	$(HUGO) server --buildDrafts --disableFastRender

build:
	$(HUGO) --gc --minify

check:
	$(HUGO) --gc --minify --printPathWarnings

clean:
	rm -rf .hugo .hugo_nokdrive public resources
