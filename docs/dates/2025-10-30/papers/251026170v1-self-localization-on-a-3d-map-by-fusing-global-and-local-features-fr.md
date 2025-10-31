---
layout: default
title: Self-localization on a 3D map by fusing global and local features from a monocular camera
---

# Self-localization on a 3D map by fusing global and local features from a monocular camera
**arXiv**：[2510.26170v1](https://arxiv.org/abs/2510.26170) · [PDF](https://arxiv.org/pdf/2510.26170.pdf)  
**作者**：Satoshi Kikuch, Masaya Kato, Tsuyoshi Tasaki  

**一句话要点**：提出融合CNN与Vision Transformer的方法，以在动态障碍物场景中实现单目相机3D自定位

**关键词**：单目相机自定位, 3D地图定位, CNN与Vision Transformer融合, 动态障碍物处理, 自定位精度提升

## 3 点简述
- 核心问题：单目相机自定位在动态障碍物（如行人）存在时，CNN提取局部特征效果不佳
- 方法要点：结合CNN提取局部特征与Vision Transformer提取全局特征，提升鲁棒性
- 实验或效果：在CG数据集上，动态障碍物下准确率提升1.5倍；自定位误差比SOTA减少20.1%

## 摘要（原文）

> Self-localization on a 3D map by using an inexpensive monocular camera is
> required to realize autonomous driving. Self-localization based on a camera
> often uses a convolutional neural network (CNN) that can extract local features
> that are calculated by nearby pixels. However, when dynamic obstacles, such as
> people, are present, CNN does not work well. This study proposes a new method
> combining CNN with Vision Transformer, which excels at extracting global
> features that show the relationship of patches on whole image. Experimental
> results showed that, compared to the state-of-the-art method (SOTA), the
> accuracy improvement rate in a CG dataset with dynamic obstacles is 1.5 times
> higher than that without dynamic obstacles. Moreover, the self-localization
> error of our method is 20.1% smaller than that of SOTA on public datasets.
> Additionally, our robot using our method can localize itself with 7.51cm error
> on average, which is more accurate than SOTA.

