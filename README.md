# DINO-MC: Self-supervised Contrastive Learning for Remote Sensing Imagery with Multi-sized Local Crops

PyTorch implementation and pretrained models for DINO-MC and DINO-TP. For details, please see <a href="https://arxiv.org/abs/2303.06670">our paper</a>.

## Pretrained models
Our models are pre-trained on SeCo-100K, and we list their k-nn and linear probing accuracy on EuroSAT.
You can download the full checkpoint of pre-trained model with training infomation as well as weights of teacher and student networks used for the downstream tasks.

<table>
  <tr>
    <th>model</th>
    <th>arch</th>
    <th>params</th>
    <th>k-nn</th>
    <th>linear</th>
    <th>download</th>
  </tr>
  <tr>
    <td>DINO-MC</td>
    <td>ViT-S/8</td>
    <td>21M</td>
    <td>93.41%</td>
    <td>94.09%</td>
    <td><a href="https://drive.google.com/file/d/18RqKqZYzigOjwbyNzLsys8bmwqxrNhyt/view?usp=share_link">pre-trained ckpt</a></td>
  </tr>
  <tr>
    <td>DINO-MC</td>
    <td>ResNet-50</td>
    <td>23M</td>
    <td>93.94%</td>
    <td>95.59%</td>
    <td><a href="https://drive.google.com/file/d/1Tku4QoQDc3BU1BOr8PzQWFPyVStUDsVE/view?usp=share_link">pre-trained ckpt</a></td>
  </tr>
  <tr>
    <td>DINO-MC</td>
    <td>WRN-50</td>
    <td>69M</td>
    <td>95.65%</td>
    <td>95.70%</td>
    <td><a href="https://drive.google.com/file/d/1WlNDoks3Uo_Al5pUHWrhQpljDrt4Ip__/view?usp=share_link">pre-trained ckpt</a></td>
  </tr>
  <tr>
    <td>DINO-MC</td>
    <td>Swin-t</td>
    <td>28M</td>
    <td>93.22%</td>
    <td>90.54%</td>
    <td><a href="https://drive.google.com/file/d/1rod3PxdZ2OGqNJxLp5CAtXm7vIsLO7us/view?usp=share_link">pre-trained ckpt</a></td>
  </tr>
  <tr>
    <td>DINO-TP</td>
    <td>ViT-S/8</td>
    <td>21M</td>
    <td>93.15%</td>
    <td>93.89%</td>
    <td><a href="https://drive.google.com/file/d/1BIRR56wCwTDlB4_eQTA0DpYYPHACHfxN/view?usp=share_link">pre-trained ckpt</a></td>
  </tr>
  <tr>
    <td>DINO-TP</td>
    <td>ResNet-50</td>
    <td>23M</td>
    <td>79.05%</td>
    <td>86.70%</td>
    <td><a href="https://drive.google.com/file/d/1mHR9uv5G7-9FpEzGBvdEOcJcWbnHOGEV/view?usp=share_link">pre-trained ckpt</a></td>
  </tr>
  <tr>
    <td>DINO-TP</td>
    <td>WRN-50</td>
    <td>69M</td>
    <td>86.27%</td>
    <td>88.15%</td>
    <td><a href="https://drive.google.com/file/d/1MoclNnRlSGOKhudm5lreDYSxYJqciQar/view?usp=share_link">pre-trained ckpt</a></td>
  </tr>
  <tr>
    <td>DINO-TP</td>
    <td>Swin-t</td>
    <td>28M</td>
    <td>92.83%</td>
    <td>91.94%</td>
    <td><a href="https://drive.google.com/file/d/1E00rYPB2wFvnq7exmQwVRe1koQ98BECL/view?usp=share_link">pre-trained ckpt</a></td>
  </tr>
</table>


## Training
Our codes refer to <a href="https://github.com/facebookresearch/dino">DINO</a> and <a href="https://github.com/ServiceNow/seasonal-contrast">SeCo</a>. 
If you want to pre-train DINO-MC based on your datasets: 
```
python  main_dino_mc.py --arch resnet50 --data_path ../datasets/seasonal_contrast_100k/ --output_dir output --data_mode mc
```

## Fine-tuning

After pre-training, you can evaluate the representations on three end-to-end fine-tuning downstream tasks.

Finetune for the change detection on OSCD downstrean task:
```
python main_oscd.py --data_path ../datasets/oscd --arch resnet50 --output_dir output --log_name log --epochs 100 --pretrained_weights checkpoints/rn_mc_checkpoint300.pth
```

Evaluate checkpoints of the change detection on OSCD downstrean task:
```
python main_oscd.py --data_path ../datasets/oscd --arch resnet50 --output_dir output --log_name log --pretrained_weights checkpoints/oscd_mc_rn.ckpt   --trained_weights checkpoints/oscd_mc_rn.ckpt --evaluate TRUE
```

<table>
  <tr>
    <th>model</th>
    <th>arch</th>
    <th>EuroSAT</th>
    <th>download</th>
  </tr>
  <tr>
    <td>DINO</td>
    <td>ViT-S/8</td>
    <td>97.98%</td>
    <td><a href="https://drive.google.com/file/d/1a9VhL88Zr2kf63gCAvvepjgNHw5Lr3I9/view?usp=share_link">EuroSAT</a></td>
  </tr>
  <tr>
    <td>DINO-MC</td>
    <td>ViT-S/8</td>
    <td>98.15%</td>
    <td><a href="https://drive.google.com/file/d/11RQ4UcWXSDm5FLfHOgeup_rB7oBe9ow4/view?usp=share_link">EuroSAT</a></td>
  </tr>
  <tr>
    <td>DINO-MC</td>
    <td>Swin-tiny</td>
    <td>98.43%</td>
    <td><a href="https://drive.google.com/file/d/1_Yb954b_BxbJ8pAKS9cS2eVytL-6V05D/view?usp=share_link">EuroSAT</a></td>
  </tr>
  <tr>
    <td>DINO-MC</td>
    <td>ResNet-50</td>
    <td>98.69%</td>
    <td><a href="https://drive.google.com/file/d/1Ab0sBv5ob7eOao9q1Nv1oMF3UVV50nq7/view?usp=share_link">EuroSAT</a></td>
  </tr>
  <tr>
    <td>DINO-MC</td>
    <td>WRN-50-2</td>
    <td>98.78%</td>
    <td><a href="https://drive.google.com/file/d/1DSLjLwaZoqeinBDaoqLwpHDYdtXId8R7/view?usp=share_link">EuroSAT</a></td>
  </tr>
</table>


<table>
  <tr>
    <th>model</th>
    <th>arch</th>
    <th>BigEarthNet-10%</th>
    <th>download</th>
    <th>BigEarthNet</th>
    <th>download</th>
  </tr>
  <tr>
    <td>DINO</td>
    <td>ResNet-50</td>
    <td>79.67%</td>
    <td><a href="">BigEarthNet-10% ckpt</a></td>
    <td>85.38%</td>
    <td><a href="">BigEarthNet ckpt</a></td>
  </tr>
  <tr>
    <td>DINO-TP</td>
    <td>ResNet-50</td>
    <td>80.10%</td>
    <td><a href="">BigEarthNet-10% ckpt</a></td>
    <td>85.20%</td>
    <td><a href="">BigEarthNet ckpt</a></td>
  </tr>
  <tr>
    <td>DINO-MC</td>
    <td>ResNet-50</td>
    <td>82.55%</td>
    <td><a href="">BigEarthNet-10% ckpt</a></td>
    <td>86.86%</td>
    <td><a href="">BigEarthNet ckpt</a></td>
  </tr>
  <tr>
    <td>DINO-MC</td>
    <td>WRN-50-2</td>
    <td>82.67%</td>
    <td><a href="">BigEarthNet-10% ckpt</a></td>
    <td>87.22%</td>
    <td><a href="">BigEarthNet ckpt</a></td>
  </tr>
  <tr>
    <td>DINO-MC</td>
    <td>Swin-tiny</td>
    <td>83.84%</td>
    <td><a href="">BigEarthNet-10% ckpt</a></td>
    <td>88.75%</td>
    <td><a href="">BigEarthNet ckpt</a></td>
  </tr>
  <tr>
    <td>DINO-MC</td>
    <td>ViT-S/8</td>
    <td>84.20%</td>
    <td><a href="">BigEarthNet-10% ckpt</a></td>
    <td>88.69%</td>
    <td><a href="">BigEarthNet ckpt</a></td>
  </tr>
</table>


<table>
  <tr>
    <th>model</th>
    <th>arch</th>
    <th>Pre.</th>
    <th>Rec.</th>
    <th>F1</th>
    <th>download</th>
  </tr>
  <tr>
    <td>DINO</td>
    <td>ResNet-50</td>
    <td>57.37</td>
    <td>44.21</td>
    <td>49.53</td>
    <td><a href="https://drive.google.com/file/d/1sWzT81-Hu3AVgXP-VtxljVlw4R3KXGUX/view?usp=share_link">OSCD</a></td>
  </tr>
  <tr>
    <td>DINO-MC</td>
    <td>ResNet-50</td>
    <td>51.94</td>
    <td>54.04</td>
    <td>52.46</td>
    <td><a href="https://drive.google.com/file/d/1CjSwiTC0PnV31bKW4J6_a-gOxAl7M9iL/view?usp=share_link">OSCD</a></td>
  </tr>
  <tr>
    <td>DINO-TP</td>
    <td>ResNet-50</td>
    <td>51.10</td>
    <td>49.03</td>
    <td>49.74</td>
    <td><a href="https://drive.google.com/file/d/10CX5_QhiUBDsVV6sfsXjDELCrvsk19Dd/view?usp=share_link">OSCD</a></td>
  </tr>
  <tr>
    <td>DINO</td>
    <td>WRN-50-2</td>
    <td>53.58</td>
    <td> 52.28 </td>
    <td>52.41</td>
    <td><a href="https://drive.google.com/file/d/1znIQdNornBp7iWuDure39pvD_h7Udkme/view?usp=share_link">OSCD</a></td>
  </tr>
  <tr>
    <td>DINO-MC</td>
    <td>WRN-50-2</td>
    <td>49.99</td>
    <td>56.81</td>
    <td>52.70</td>
    <td><a href="https://drive.google.com/file/d/12a5pndW-asrrVJnJrSWArnt2XCbM4zBE/view?usp=share_link">OSCD</a></td>
  </tr>
  <tr>
    <td>DINO-TP</td>
    <td>WRN-50-2</td>
    <td>55.77</td>
    <td>47.30</td>
    <td>50.61</td>
    <td><a href="https://drive.google.com/file/d/1HQaztXnQhcluBMLtHuCwM8BXmhJ8yTcz/view?usp=share_link">OSCD</a></td>
  </tr>
</table>

## Citation
If you find this repository useful, please consider giving a star :star: and citation:
```
@misc{wanyan2023dinomc,
      title={DINO-MC: Self-supervised Contrastive Learning for Remote Sensing Imagery with Multi-sized Local Crops}, 
      author={Xinye Wanyan and Sachith Seneviratne and Shuchang Shen and Michael Kirley},
      year={2023},
      eprint={2303.06670},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```