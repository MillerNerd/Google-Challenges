def solution(versions):
    versions.sort(key=lambda s: map(int, s.split('.')))
    return versions
