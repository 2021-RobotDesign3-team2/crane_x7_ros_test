# crane_x7_ros_test
設計製作論3 
<br>
こちらはCRANE-x7で自作のフライパンを使ってフライ返しをするためのROSパッケージです。
<br>
本パッケージはオリジナルである[rt-net/crane_x7_ros](https://github.com/rt-net/crane_x7_ros)をもとに、未来ロボティクス学科で開講された講義内でのグループ2021-RobotDesign-team2が作成したものです。

 ## 実装内容
 
 [crane_x7](https://rt-net.jp/products/crane-x7/)を用いてフライパンのフライ返しを動きをさせるサンプルコードです。
 <br>
 crane_x7とIntelRealSenseを用いて実機動作を行っています。
 
 ---
## 動作環境

・ubuntu 20.04.3LTS  or  ubuntu 18.04.5LTS
<br>
・Gazebo 11.5.1
<br>
・Rviz 1.13.7
<br>
・[rt-net/crane_x7_ros](https://github.com/rt-net/crane_x7_ros)
<br>
・[IntelRealSense/realsense-ros](https://github.com/IntelRealSense/realsense-ros)

---
## 環境構築

1 ROSのインストール

```sh
cd ~/catkin_ws/src  
git clone https://github.com/rt-net/crane_x7_ros.git  
```  
詳しくは[こちら](https://github.com/rt-net/crane_x7_ros)を参照してください。  

2 本パッケージのインストール

```sh
cd ~/catkin_ws/src  
git clone  https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test
cd ~/catkin_ws
catkin_make
```  

---
## 実行方法

### シュミレータを使う場合

このシュミレータではIntelRealSenseを用いた動作はできません。
<br>
実際にCRANE-X7を動かすときの動作を確認するために使用してください。

1 シュミレータの起動

```sh
$ roslaunch crane_x7_ros_test crane_x7_with_table_flypan.launch 
```

2 本パッケージのサンプルコードの実行

```sh
$ rosrun crane_x7_ros_test main_move.py 
```
サンプルコードの詳細は[crane_x7_ros_test/scripts](https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test/tree/main/scripts)を参照してください。

### 実機を使う場合

1 IntelRealSenseとCRANE-X7を接続します。

2 CRANE-X7の制御信号ケーブルを制御用パソコンに接続し、以下を実行する。

```sh
$ sudo chmod 666 /dev/ttyUSB*
```
3 [rt-net/crane_x7_ros](https://github.com/rt-net/crane_x7_ros/tree/master/crane_x7_bringup/launch)の以下のコードを実行する。

```sh
$ roslaunch crane_x7_bringup demo.launch
```

4 本パッケージの以下の2つのコードを順に実行する。

```sh
$ rosrun crane_x7_ros_test color.py
$ rosrun crane_x7_ros_test ready.py
```


