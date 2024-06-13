def solution(cacheSize, cities):
    answer = 0
    
    # 캐시 저장할 dict
    cache = {}
    
    # 캐시 사이즈가 0일 경우 항상 cache miss
    if cacheSize == 0:
        return len(cities) * 5
    
    for i in range(len(cities)):
        # 대,소문자 구분을 하지 않기 때문에 전부 소문자로 변환
        city = cities[i].lower()
        
        # 캐시가 꽉 찬 경우
        if len(cache) == cacheSize:
            # 캐시 안에 해당 도시가 있으면 cache hit(+1)
            if city in cache:
                cache[city] = i
                answer += 1
            # 캐시 안에 해당 도시가 없으면 가장 오래 사용된 적 없는 도시 삭제하고, 새로운 도시 넣고, cache miss(+5)
            else:
                min_key = min(cache, key = cache.get)
                del cache[min_key]
                cache[city] = i
                answer += 5
                
        # 캐시에 빈 공간이 있는 경우
        else:
            # cache hit일 경우 value만 최신화하고 (+1)
            if city in cache:
                cache[city] = i
                answer += 1
            
            #cache miss일 경우 새로운 값 넣고 (+5)
            else:
                cache[city] = i
                answer += 5

    return answer