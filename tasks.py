from invoke import task


@task
def clean(c):
    c.run("latexmk -C")


@task
def build(c, python=False):
    if python:
        c.run("python metrovalencia4.py")
    c.run("latexmk main.tex")
