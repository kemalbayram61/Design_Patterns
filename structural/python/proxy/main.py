from subject import Subject
from real_subject import RealSubject
from proxy import Proxy

def client_code(subject: Subject):
    subject.request()


if __name__ == '__main__':
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)