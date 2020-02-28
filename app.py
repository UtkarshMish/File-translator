from googletrans import Translator
import codecs

translate = Translator()
if __name__ == '__main__':
    filename = input("Enter Filename(with extension) to translate: ")
    try:
        with codecs.open(filename, 'r', "utf-8") as file:
            file_data = file.readlines()
        current_Lng = translate.detect(file_data)
        option = 'y'

        while True:
            option = str(input(f'Currently written in {current_Lng[0]}.Want to Change(y/n) ?'))
            if option == 'y' or option == 'n':
                break

        if option.lower() == 'y':
            change_Lng = input("Enter the Language Code: ")
            try:
                translations = [str(translate.translate(data, change_Lng).text) for data in file_data]
                print(' '.join([t for t in translations]))
            except UnicodeEncodeError:
                print("couldn't translate!!")
                exit(1)
            except ValueError:
                print("Code doesn't exist!!")
                exit(0)

        with codecs.open(filename[:-4]+f'-{change_Lng}.txt', 'w', "utf-8") as file:
            for data in translations:
                file.writelines(data)

    except FileNotFoundError as err:
        print("file not found !!!!", end=' ')
    except KeyboardInterrupt:
        exit(1)
    finally:
        print("---------PROGRAM ENDS------------")
        exit(0)
