# practice_mido

## GMMidiCheck.ipynb

* GM, GS, XGのMIDIのデータをチェックするスクリプト
* SysExを見て判別する(以下の表の通り。F0がSysExの先頭を示している。次がメーカーID、xxはデバイスID（機器固有のID)、最後がモデルIDになる（ローランドのGSの聞きならモデルID42のようなのでそれでGS音源を判別できる。

|MIDIデータ規格の種類|System Exclusive|
| --- | --- |
|GM (General MIDI)|F0 7E xx 09|
|GS (ローランドのGM拡張)|F0 41 xx 42|
|XG (YamahaのGM拡張|F0 43 xx 4C|

## midi_utill.py

* 上記のファイルを実行するにあたっての関数をまとめたもの。
