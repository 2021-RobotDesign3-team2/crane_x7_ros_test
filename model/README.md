# model

Inventor（モデルを作成するアプリケーション）などで作成したモデルをGAZEBOのシュミレーション内に反映させるための方法です。
<br>
これはwslではなくネイティブ環境のUbuntuで行っています。

---
## 動作環境と使用したアプリケーション

### Windows10
### Ubuntu 20.04.3
### Autodesk Inventor Professional 2021
### blender
---
## windows側での操作

1 Inventorで反映させたいモデルを作成する。（モデルの寸法の設定と作業平面に注意する）
<br>
2 作成したモデルをsdfファイルで保存する。
<br>
3 保存したファイルをUSBに移動する。

## Ubuntu側での操作

1 blenderで作成したモデルのsdfファイルをインポートし、COLLADA形式(.dae)でエクスポートする。（単位がメートルになっていることを確認する）
<br>
2 model.sdfとmodel.configをデフォルトモデル（wood_cube_5cmとtable）を参考にして作成する。
<br>
3 wordファイルを作成する。（この時に作成したモデルの慣性モーメントが必要）
<br>
https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test/tree/main/worlds
<br>
4 launchファイルを作成する。
<br>
https://github.com/2021-RobotDesign3-team2/crane_x7_ros_test/tree/main/launch
<br>
5 package.xmlを編集し、自分の作成したモデルがあるディレクトリと紐続ける。 

![image](https://user-images.githubusercontent.com/91268353/146216437-0514c6fa-5f22-4cb5-acc9-1e9399cce0cb.png)

参考にさせて頂いたサイト
<br>
https://qiita.com/srs/items/ac242e46177c2b797a7b
