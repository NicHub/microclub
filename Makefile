.PHONY: serve build check clean

THEME ?= blowfish
HUGO = hugo --theme "$(THEME)"

serve:
	$(HUGO) server --buildDrafts --disableFastRender

build:
	$(HUGO) --gc

check:
	$(HUGO) --gc --printPathWarnings

clean:
	rm -rf .hugo .hugo_nokdrive public resources
