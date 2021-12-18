# scripts
本パッケージはオリジナルである[rt-net/crane_x7_ros](https://github.com/rt-net/crane_x7_ros)をもとに、未来ロボティクス学科で開講された講義内でのグループ2021-RobotDesign-team2が作成したものです。

---
## 実装内容

### color.py  

RealSenseから受け取った色画像をカメラ座標に変換するプログラムです。  

### ready.py  

カメラを下に向け、search.pyを起動するまでのプログラムです。  
![ready](https://user-images.githubusercontent.com/71488443/146645299-08b9c7d9-6c6a-4174-8372-9573e84a2098.gif)

### search.py  

カメラ座標をアーム座標に変換し、フライパンを認識して掴み、main_move.pyを起動するプログラムです。  

### main_move.py

フライパンを掴んだあとに持ち上げフライ返しをして置くまでのプログラムです。  
