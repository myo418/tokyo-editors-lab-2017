### JIS形式からUTF8のtsvファイルへの変換
$ nkf -d -w asahi_jis.txt > asahi_utf8.tsv
$ nkf -d -w yomiuri_jis.txt > yomiuri_utf8.tsv
$ nkf -d -w nikkei_jis.txt > nikkei_utf8.tsv
$ nkf -d -w sankei_jis.txt > sankei_utf8.tsv
$ nkf -d -w mainichi_jis.txt > mainichi_utf8.tsv

### google apiを使う前に
$ export GOOGLE_APPLICATION_CREDENTIALS=/Users/mmyojin/git/tokyo-editors-lab-2017/tokyo-editors-lab-2017-cae345b616a2.json
