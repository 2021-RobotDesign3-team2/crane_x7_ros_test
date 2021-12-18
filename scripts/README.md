# scripts
本パッケージはオリジナルである[rt-net/crane_x7_ros](https://github.com/rt-net/crane_x7_ros)をもとに、未来ロボティクス学科で開講された講義内でのグループ2021-RobotDesign-team2が作成したものです。

---
## 実装内容

### color.py  

RealSenseから受け取った色画像をカメラ座標に変換するプログラムです。  

### ready.py  

カメラを下に向け、color.pyを起動するまでのプログラムです。

### search.py  

カメラ座標をアーム座標に変換し、フライパンを認識して掴み、main_move.pyを起動するプログラムです。  

### main_move.py

フライパンを掴んだあとに持ち上げフライ返しをして置くまでのプログラムです。  
