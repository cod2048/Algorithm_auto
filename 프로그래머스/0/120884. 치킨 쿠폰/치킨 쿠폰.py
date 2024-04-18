def solution(chicken):
    if chicken < 10:
        return 0

    service_chicken = chicken // 10
    
    return service_chicken + solution(service_chicken + (chicken % 10))