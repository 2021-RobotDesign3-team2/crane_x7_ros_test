# scripts
本パッケージはオリジナルである[rt-net/crane_x7_ros](https://github.com/rt-net/crane_x7_ros)をもとに、未来ロボティクス学科で開講された講義内でのグループ2021-RobotDesign-team2が作成したものです。

---
## 実装内容

### color.py  

RealSenseから受け取った色画像をカメラ座標に変換するプログラムです。  
![color](https://user-images.githubusercontent.com/71488443/146658743-bf92baa9-8963-40da-93b2-385ffefd5f0d.gif)

### ready.py  

カメラを下に向け、search.pyを起動するまでのプログラムです。  
![ready](https://user-images.githubusercontent.com/71488443/146658376-03381f92-7338-4c2e-b58a-268dcd97c92d.gif)

### search.py  

カメラ座標をアーム座標に変換し、フライパンを認識して掴み、main_move.pyを起動するプログラムです。  
![search](https://user-images.githubusercontent.com/71488443/146658449-0756c2c5-6b67-4671-8c85-cf222c16fa12.gif)


### main_move.py

フライパンを持ち上げフライ返しをし、フライパンを置いて最初の姿勢に戻るプログラムです。  
![main_move](https://user-images.githubusercontent.com/71488443/146658587-4e80f99c-eefb-488c-ac66-16f43f750b95.gif)

