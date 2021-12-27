# scripts
本パッケージはオリジナルである[rt-net/crane_x7_ros](https://github.com/rt-net/crane_x7_ros)をもとに、未来ロボティクス学科で開講された講義内でのグループ2021-RobotDesign-team2が作成したものです。

---
## 実装内容

### color.py  
実行方法
```  
$ rosrun crane_x7_ros_test color.py  
```  

RealSenseから受け取った色画像をカメラ座標に変換するプログラムです。  
青色の重心をカメラ座標として画面中央からどれだけずれているかx/y座標をPublishしています。分かりやすいように水色でマークしています。  

![color](https://user-images.githubusercontent.com/71488443/146658743-bf92baa9-8963-40da-93b2-385ffefd5f0d.gif)  

実行時に青色が検出されず、以下のようなERRORが出た場合、カメラの前に青色を用意してください。  
![Screenshot from 2021-12-20 08-26-35](https://user-images.githubusercontent.com/71488443/146697076-b2e5d9bf-3de7-4f2f-9d40-b2ca85933929.png)



### ready.py  

実行方法
```  
$ rosrun crane_x7_ros_test ready.py  
```  

カメラを下に向け、search.pyを起動するまでのプログラムです。  
角度制御でアームを動かしています。  
![ready](https://user-images.githubusercontent.com/71488443/146658376-03381f92-7338-4c2e-b58a-268dcd97c92d.gif)

### search.py  

実行方法
```  
$ rosrun crane_x7_ros_test search.py  
```  

カメラ座標をアーム座標に変換し、フライパンを認識して掴み、main_move.pyを起動するプログラムです。  
位置制御でアームを動かしています。  
color.pyが動いている必要があります。  
![search](https://user-images.githubusercontent.com/71488443/146658449-0756c2c5-6b67-4671-8c85-cf222c16fa12.gif)


### main_move.py

実行方法
```  
$ rosrun crane_x7_ros_test main_move.py  
```  

フライパンを持ち上げフライ返しをし、フライパンを置いて最初の姿勢に戻るプログラムです。  
角度制御でアームを動かしています。  
![フライ返し_1](https://user-images.githubusercontent.com/71488443/147443629-96d2b1aa-20c0-4e5c-a70d-fb22961f0dcc.gif)
![フライ返し_2](https://user-images.githubusercontent.com/71488443/147449642-afb58c17-7eb4-4222-9b9c-4b0d3504b052.gif)

---  
### 使用・参考にしたコード一覧  
|コード|コード引用元|著作権者|元のライセンス|
|:--:|:---:|:---:|:---:|
|[color.py](https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test/blob/main/scripts/color.py)||OpenCV|[Apache License 2.0](https://github.com/opencv/opencv/blob/4.x/LICENSE)|
|[color.py](https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test/blob/main/scripts/color.py)/[main_move.py](https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test/blob/main/scripts/main_move.py)/[ready.py](https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test/blob/main/scripts/ready.py)/[search.py](https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test/blob/main/scripts/search.py)||Robot Operating System|[BSD-3-Clause License](https://github.com/ros/ros/blob/noetic-devel/LICENSE)|
|[color.py](https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test/blob/main/scripts/color.py)|[find_red.py](https://github.com/robotcreating2020-1/cola_with_crane_x7_ros/blob/master/cola_examples/scripts/find_red.py)|[robotcreating2021-1](https://github.com/robotcreating2020-1/cola_with_crane_x7_ros/tree/master)|[BSD-3-Clause License](https://github.com/robotcreating2020-1/cola_with_crane_x7_ros/blob/master/LICENSE)|
|[main_move.py](https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test/blob/main/scripts/main_move.py)|[nagi_uda.py](https://github.com/8group-robotdesign3/crane_x7_ros_modified_by_group8/blob/master/crane_x7_examples/scripts/nagi_uda.py)|[8group-robotdesign3](https://github.com/8group-robotdesign3/crane_x7_ros_modified_by_group8)|[LICENCE](https://github.com/8group-robotdesign3/crane_x7_ros_modified_by_group8/blob/master/LICENSE)|
