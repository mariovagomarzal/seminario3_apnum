from invoke import task


@task
def clean(c):
    c.run("latexmk -C")


@task
def build(c, pythontex=False):
    c.run("latexmk main.tex", warn=True)
    if pythontex:
        c.run("pythontex main.tex")
        c.run("latexmk main.tex")
