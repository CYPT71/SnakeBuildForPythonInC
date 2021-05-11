from distutils.core import setup, Extension
import shutil

def main():
    setup(name="snake",
          version="1.0.0",
          description="snake game in pure python",
          author="<your name>",
          author_email="your_email@gmail.com",
          ext_modules=[Extension("snake", ["lib/pySnake.c", "lib/snake/snake.c"])])
    shutil.rmtree('build', ignore_errors=True)
if __name__ == "__main__":
    main()
