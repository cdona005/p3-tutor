import re, sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
s, n = re.subn(r'\n\s*<details>\s*<summary>Show the answer</summary>.*?</details>', '', s, flags=re.S)
s = s.replace('data-why="Right. ', 'data-why="')
open(p, 'w', encoding='utf-8').write(s)
print('removed', n)
t = re.sub(r'<script.*?</script>|<style.*?</style>', '', s, flags=re.S)
t = re.sub(r'<[^>]+>', ' ', t)
print('words', len(t.split()))
