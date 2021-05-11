from distutils.core import setup, Extension

def main():
    setup(name="snake",
          version="1.0.0",
          description="snake game in pure python",
          author="<your name>",
          author_email="your_email@gmail.com",
          ext_modules=[Extension("snake", ["pySnake.c", "snake/snake.c"])])

if __name__ == "__main__":
    main()
