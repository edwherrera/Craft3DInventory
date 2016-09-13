from service import service
from exception import exception


def main():
    printer_service = service.Printer()

    try:
        print(printer_service.get(model='Printe'))
    except exception.ObjectNotFoundException:
        print('The object already exists')


if __name__ == '__main__':
    main()
