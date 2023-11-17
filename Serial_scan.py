import socket

def find_open_port():
    # 소켓 생성
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 임시 포트 할당
    s.bind(('localhost', 0))
    
    # 현재 사용 중인 포트 가져오기
    port = s.getsockname()[1]
    
    # 소켓 닫기
    s.close()
    
    return port

# 함수 호출하여 현재 사용 중인 포트 얻기
current_port = find_open_port()

print(f"현재 사용 중인 포트: {current_port}")
