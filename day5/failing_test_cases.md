
function -> expected_output actual_output

```
make_abba('x', 'y') → 'xyyx'	'xyyx'
make_abba('x', '') → 'xx'	    False
```

```
string_match('aabbccdd', 'abbbxxd') → 1	3
string_match('aaxxaaxx', 'iaxxai')  → 3	5
string_match('iaxxai', 'aaxxaaxx')  → 3	5
```
