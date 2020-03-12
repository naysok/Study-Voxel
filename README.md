# Study-Voxel  


ボクセルを扱う（まずは描画から）。  


Open3D ライブラリを想定。  


##### ファイル形式  

ボクセルを扱うようなファイル形式は、.pcd や、 ~~.ply~~ がありそう。  
他に、富士ゼロックスと慶應 SFC の .fav ファイルがあるっぽい。
[phttps://www.fujixerox.co.jp/company/technical/communication/3d/fav.html](https://www.fujixerox.co.jp/company/technical/communication/3d/fav.html)  

あとは、CG 業界では、OpenVDB というボリュームデータの中間ファイルがあるらしい。Houdini でもサポートされている。  
[https://www.openvdb.org/](https://www.openvdb.org/)  



##### 描画とか  

描画が重いので嫌だなと思っていたら、Open3d に、ダウンサンプリングという関数があるらしい。  
[http://lang.sist.chukyo-u.ac.jp/classes/Open3D/PointCloud.html#Voxel-downsampling](http://lang.sist.chukyo-u.ac.jp/classes/Open3D/PointCloud.html#Voxel-downsampling)  


点群とかポイントクラウドとか言われるものは表面の点の集まりで、ボクセルは内部までみっちりの点の集まりという認識で良いのかな。  



---  



### ファイル形式  

##### .pcd  

> The PCD (Point Cloud Data) file format  

PCL ライブラリのフォーマット。  

[http://pointclouds.org/documentation/tutorials/pcd_file_format.php](http://pointclouds.org/documentation/tutorials/pcd_file_format.php)  

色を持てる  

```
FIELDS x y z rgb # XYZ + colors
```

[http://lang.sist.chukyo-u.ac.jp/Classes/PCL/PCDfileFormat.html](http://lang.sist.chukyo-u.ac.jp/Classes/PCL/PCDfileFormat.html)  



##### .ply  

> PLY は Polygon File Format もしくは Stanford Triangle Format として知られているコンピュータファイル形式である。これは原則として3Dスキャナからの3次元データを格納するために設計された。データ格納形式は、名目上平面ポリゴンのリストとして、単独オブジェクトの比較的簡単な記述をサポートしている。以下を含めた様々なプロパティが格納され得る: 色および透明性、サーフィス法線、テクスチャ座標およびデータ信頼値。また、この形式はポリゴンの表と裏に異なったプロパティを持たせることができる。このファイル形式には、ASCIIとバイナリの二つのバージョンが存在する。（wikipedia より）  

頂点と、面を明示する必要があり、メッシュでした。  



---  
