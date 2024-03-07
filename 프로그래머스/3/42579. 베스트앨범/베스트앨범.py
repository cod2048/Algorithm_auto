def solution(genres, plays):
    answer = []
    genre_info = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in genre_info:
            genre_info[genre] = {'total_plays': 0, 'songs': []}
        genre_info[genre]['total_plays'] += play
        genre_info[genre]['songs'].append((play, i))
        
    genre_sorted = sorted(genre_info.items(), key=lambda x: x[1]['total_plays'], reverse=True)
    
    for genre, info in genre_sorted:
        songs_sorted = sorted(info['songs'], key=lambda x: x[0], reverse=True)
        for play, i in songs_sorted[:2]:
            answer.append(i)
    
    
    print(genre_info)
    return answer