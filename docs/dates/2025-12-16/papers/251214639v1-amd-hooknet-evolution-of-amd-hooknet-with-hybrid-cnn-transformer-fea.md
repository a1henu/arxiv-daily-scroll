---
layout: default
title: AMD-HookNet++: Evolution of AMD-HookNet with Hybrid CNN-Transformer Feature Enhancement for Glacier Calving Front Segmentation
---

# AMD-HookNet++: Evolution of AMD-HookNet with Hybrid CNN-Transformer Feature Enhancement for Glacier Calving Front Segmentation
**arXiv**：[2512.14639v1](https://arxiv.org/abs/2512.14639) · [PDF](https://arxiv.org/pdf/2512.14639.pdf)  
**作者**：Fei Wu, Marcel Dreier, Nora Gourmelon, Sebastian Wind, Jianlin Zhang, Thorsten Seehaus, Matthias Braun, Andreas Maier, Vincent Christlein  

**一句话要点**：提出AMD-HookNet++，通过混合CNN-Transformer特征增强解决冰川崩解前沿分割问题。

**关键词**：冰川分割, 混合CNN-Transformer, 特征增强, 空间-通道注意力, 像素对比监督, 合成孔径雷达图像

## 3 点简述
- 核心问题：卷积神经网络在冰川分割中难以保持长程依赖，导致边缘锯齿化。
- 方法要点：结合Transformer分支捕获全局上下文和CNN分支保留局部细节，并设计增强空间-通道注意力模块。
- 实验或效果：在CaFFe数据集上实现78.2 IoU和1,318 m HD95，生成更平滑的崩解前沿轮廓。

## 摘要（原文）

> The dynamics of glaciers and ice shelf fronts significantly impact the mass balance of ice sheets and coastal sea levels. To effectively monitor glacier conditions, it is crucial to consistently estimate positional shifts of glacier calving fronts. AMD-HookNet firstly introduces a pure two-branch convolutional neural network (CNN) for glacier segmentation. Yet, the local nature and translational invariance of convolution operations, while beneficial for capturing low-level details, restricts the model ability to maintain long-range dependencies. In this study, we propose AMD-HookNet++, a novel advanced hybrid CNN-Transformer feature enhancement method for segmenting glaciers and delineating calving fronts in synthetic aperture radar images. Our hybrid structure consists of two branches: a Transformer-based context branch to capture long-range dependencies, which provides global contextual information in a larger view, and a CNN-based target branch to preserve local details. To strengthen the representation of the connected hybrid features, we devise an enhanced spatial-channel attention module to foster interactions between the hybrid CNN-Transformer branches through dynamically adjusting the token relationships from both spatial and channel perspectives. Additionally, we develop a pixel-to-pixel contrastive deep supervision to optimize our hybrid model by integrating pixelwise metric learning into glacier segmentation. Through extensive experiments and comprehensive quantitative and qualitative analyses on the challenging glacier segmentation benchmark dataset CaFFe, we show that AMD-HookNet++ sets a new state of the art with an IoU of 78.2 and a HD95 of 1,318 m, while maintaining a competitive MDE of 367 m. More importantly, our hybrid model produces smoother delineations of calving fronts, resolving the issue of jagged edges typically seen in pure Transformer-based approaches.

