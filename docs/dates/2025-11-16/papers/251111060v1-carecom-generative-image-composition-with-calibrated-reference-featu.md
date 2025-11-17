---
layout: default
title: CareCom: Generative Image Composition with Calibrated Reference Features
---

# CareCom: Generative Image Composition with Calibrated Reference Features
**arXiv**：[2511.11060v1](https://arxiv.org/abs/2511.11060) · [PDF](https://arxiv.org/pdf/2511.11060.pdf)  
**作者**：Jiaxuan Chen, Bo Zhang, Qingdong He, Jinlong Peng, Li Niu  

**一句话要点**：提出多参考生成图像合成方法，通过校准参考特征解决细节保持与姿态调整问题。

**关键词**：生成图像合成, 多参考模型, 特征校准, 细节保持, 姿态调整

## 3 点简述
- 现有方法难以同时保持前景细节和调整姿态/视角。
- 扩展为多参考模型，并校准参考特征以兼容背景信息。
- 在MVImgNet和MureCom数据集上验证，校准特征提升合成效果。

## 摘要（原文）

> Image composition aims to seamlessly insert foreground object into background. Despite the huge progress in generative image composition, the existing methods are still struggling with simultaneous detail preservation and foreground pose/view adjustment. To address this issue, we extend the existing generative composition model to multi-reference version, which allows using arbitrary number of foreground reference images. Furthermore, we propose to calibrate the global and local features of foreground reference images to make them compatible with the background information. The calibrated reference features can supplement the original reference features with useful global and local information of proper pose/view. Extensive experiments on MVImgNet and MureCom demonstrate that the generative model can greatly benefit from the calibrated reference features.

