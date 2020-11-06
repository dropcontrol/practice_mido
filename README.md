# practice_mido

## TL;DR

* GM, GS, XGのMIDIのデータをチェックするスクリプト
* SysExを見て判別する(以下の表の通り。F0がSysExの先頭を示している。次がメーカーID、xxはデバイスID（機器固有のID)、最後がモデルIDになる（ローランドのGSの聞きならモデルID42のようなのでそれでGS音源を判別できる。
* 詳しくはここに記事を書いた＞https://qiita.com/dropcontrol/items/c9f434fb3b9b5806f14e

|MIDIデータ規格の種類|System Exclusive|
| --- | --- |
|GM (General MIDI)|F0 7E xx 09|
|GS (ローランドのGM拡張)|F0 41 xx 42|
|XG (YamahaのGM拡張|F0 43 xx 4C|

## GMMidiCheck.ipynb

* midiFileDir ... 判定したいMIDIファイルが入っているディレクトリ。ここに親ディレクトリを指定すれば、再起的に全ての.midもしくは.MIDのファイルパスを取得します。
* GMMidiFileDir ... 判定してGM/GS/XGだと思われるSysEXが含まれているMIDIファイルをここに指定したディレクトリにコピーします。ディレクトリがなければ作成します。ファイル名が重複した場合は上書きされます。

## midi_utill.py

* 上記のファイルを実行するにあたっての関数をまとめたもの。
