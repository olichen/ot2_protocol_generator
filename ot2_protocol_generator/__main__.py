from . import protocol_generator

def main():
    pg = protocol_generator.ProtocolGenerator()
    pg.window.mainloop()

if __name__ == '__main__':
    main()
