# Stratasys_J750  

データ入稿について要確認。  

[https://help.grabcad.com/article/230-guide-to-voxel-printing?locale=ja&fbclid=IwAR3PvdP71KfqY1herjNa87oGvXnszbsXIcaNfOUYNfbDLn_kIZydNeyYXes](https://help.grabcad.com/article/230-guide-to-voxel-printing?locale=ja&fbclid=IwAR3PvdP71KfqY1herjNa87oGvXnszbsXIcaNfOUYNfbDLn_kIZydNeyYXes)  


---  


# 形、寸法について  

### Layer Height  

> 準備するスライスのレイヤーの厚さをプリントされたレイヤーの厚さに一致させることをお勧めします。プリンタのレイヤーの厚さは次のとおりです。  
> 0.014 mm = 高品質  
> 0.027 mm = 高速 & ��イミックス  
> スライスのプリント時に、スライスの厚さがプリンタのレイヤーの厚さと一致していない場合、プリンタはこの差を補正します。これにより、スライスの重複やスキップが発生する場合があります。たとえば、スライスの厚さを 0.0135 mm に設定し、プリンティングモードがハイミックスである場合、プリンタは、プリンタのレイヤーの厚さである 0.027 mm に達するまで、各イメージを 2 回プリントします。  
 

### XY 解像度  

> J750 は X と Y で解像度が異なります。  
> X 解像度 = 600 DPI  
> Y 解像度 = 300 DPI  
> したがって、パーツが 1 インチのキューブの場合、各スライスは 600x300 ピクセルのサイズになります。  

1インチ立法の箱については多分こう。  
この理解で正しければ、最後に 1:2 にスケール変更をかければ良さそう。  

![cube](images/Example_Cube.png)  


---  


# 色、マテリアルについて  


---  