.PHONY: serve build check

serve:
	hugo server --buildDrafts --disableFastRender

build:
	hugo --gc --minify

check:
	hugo --gc --minify --printPathWarnings
