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

- Ubuntu 18.04.6LTS  
- ROS Melodic  
    - Gazebo 9.0.0+dfsg5-3ubuntu1+ppa2  
    - Rviz 1.12.4+dfsg-3  
    - MoveIt 1.0.8-1  
    - RealSense SDK 2.0  
- OpneCV 4.5.1

---
## 環境構築

1 ROSのインストール

```sh
$ git clone https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu18.04_desktop.git
$ cd ros_setup_scripts_Ubuntu18.04_desktop/
$ sudo apt update
$ sudo apt upgrade
$ ./locale.ja.bash
$ ./step0.bash
$ ./step1.bash
```

2 動作確認

```sh
$ cd     
$ source ~/.bashrc
$ roscore
```
Ctrl+Cでプログラムの終了

3 ワークスペースを作成し、~/.bashrcを編集

```sh
$ cd
$ mkdir -p catkin_ws/src
$ cd ~/catkin_ws/src/
$ catkin_init_workspace
$ cd ..
$ catkin_make
$ vi ~/.bashrc
source /opt/ros/melodic/setup.bash
source ~/catkin_ws/devel/setup.bash       #この行を追加
export ROS_MASTER_URI=http://localhost:11311
$ source ~/.bashrc
$ cd ~/catkin_ws/
$ catkin_make
```

4 CRANE-X7のROSパッケージのインストール

```sh
$ cd ~/catkin_ws/src/  
$ git clone https://github.com/rt-net/crane_x7_ros.git
$ git clone https://github.com/roboticsgroup/roboticsgroup_gazebo_plugins.git
$ rosdep install -r -y --from-paths --ignore-src crane_x7_ros
$ ( cd ~/catkin_ws/ && catkin_make )
```  
詳しくは[こちら](https://github.com/rt-net/crane_x7_ros)を参照してください。

5 RVISの動作確認

```sh
$ source ~/.bashrc
$ roscore &
$ rviz
```

6 GAZEBOの動作確認

```sh
$ mkdir ~/.ignition/fuel
$ vi config.yaml
config.yamlに以下を追加
servers:
-
  name: osrf
  url: https://api.ignitionrobotics.org
$ roslaunch crane_x7_gazebo crane_x7_with_table.launch
```
  
7 本パッケージのインストール

```sh
$ cd ~/catkin_ws/src  
$ git clone  https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test
$ cd ~/catkin_ws
$ catkin_make
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

![image](https://user-images.githubusercontent.com/91268353/146878311-86ecc456-c7db-422e-9c56-37abd7a97057.png)

![iOS の画像 (2) (1)](https://user-images.githubusercontent.com/91268353/146890295-7ff7b9e3-a9f2-4ec6-88d8-9e4ef5dbca3d.jpg)

1 IntelRealSenseとCRANE-X7を接続します。

2 CRANE-X7の制御信号ケーブルを制御用パソコンに接続し、以下を実行する。

```sh
$ sudo chmod 666 /dev/ttyUSB*
```
3 [rt-net/crane_x7_ros](https://github.com/rt-net/crane_x7_ros/blob/master/crane_x7_moveit_config/launch/demo.launch)の以下のコードを実行する。

```sh
$ roslaunch crane_x7_moveit_config demo.launch
```  
4 color.pyを実行する前に以下のコードを実行する。  
```  
$ roslaunch realsense2_camera rs_camera.launch  
```  

5 本パッケージの以下の2つのコードを順に実行する。  
ready.pyを実行するとcrane_x7が動き出します。

```sh
$ rosrun crane_x7_ros_test color.py
$ rosrun crane_x7_ros_test ready.py
```
---
### 知的財産権について  
CRANE-X7は、アールティが開発した研究用アームロボットです。 このリポジトリのデータ等に関するライセンスについては、[LICENSEファイル](https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test/blob/main/LICENSE)をご参照ください。 企業による使用については、自社内において研究開発をする目的に限り、本データの使用を許諾します。 本データを使って自作されたい方は、義務ではありませんが弊社ロボットショップで部品をお買い求めいただければ、励みになります。 商業目的をもって本データを使用する場合は、商業用使用許諾の条件等について弊社までお問合せください。

サーボモータのXM540やXM430に関するCADモデルの使用については、ROBOTIS社より使用許諾を受けています。 CRANE-X7に使用されているROBOTIS社の部品類にかかる著作権、商標権、その他の知的財産権は、ROBOTIS社に帰属します。  
### Proprietary Rights  
CRANE-X7 is an arm robot developed by RT Corporation for research purposes. Please read [the license information](https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test/blob/main/LICENSE) contained in this repository to find out more about licensing. Companies are permitted to use CRANE-X7 and the materials made available here for internal, research and development purposes only. If you are interested in building your own robot for your personal use by utilizing the information made available here, take your time to visit our website and purchase relevant components and parts – that will certainly help us keep going! Otherwise, if you are interested in manufacturing and commercializing products based on the information herein, please contact us to arrange a license and collaboration agreement with us.

We have obtained permission from ROBOTIS Co., Ltd. to use CAD models relating to servo motors XM540 and XM430. The proprietary rights relating to any components or parts manufactured by ROBOTIS and used in this product, including but not limited to copyrights, trademarks, and other intellectual property rights, shall remain vested in ROBOTIS.  
