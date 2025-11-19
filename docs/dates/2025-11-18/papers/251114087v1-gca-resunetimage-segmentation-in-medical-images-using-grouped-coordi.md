---
layout: default
title: GCA-ResUNet:Image segmentation in medical images using grouped coordinate attention
---

# GCA-ResUNet:Image segmentation in medical images using grouped coordinate attention
**arXiv**：[2511.14087v1](https://arxiv.org/abs/2511.14087) · [PDF](https://arxiv.org/pdf/2511.14087.pdf)  
**作者**：Jun Ding, Shang Gao  

**一句话要点**：提出GCA-ResUNet以高效解决医学图像分割中的长程依赖问题

**关键词**：医学图像分割, 分组坐标注意力, 长程依赖建模, 高效卷积网络, 全局上下文编码

## 3 点简述
- 核心问题：U-Net类网络难以捕获长程依赖，Transformer变体计算量大且需大数据
- 方法要点：集成分组坐标注意力到ResNet-50块，联合编码通道和空间全局依赖
- 实验或效果：在Synapse和ACDC数据集上Dice分数达86.11%和92.64%，超越基线且高效

## 摘要（原文）

> Medical image segmentation underpins computer-aided diagnosis and therapy by supporting clinical diagnosis, preoperative planning, and disease monitoring. While U-Net style convolutional neural networks perform well due to their encoder-decoder structures with skip connections, they struggle to capture long-range dependencies. Transformer-based variants address global context but often require heavy computation and large training datasets. This paper proposes GCA-ResUNet, an efficient segmentation network that integrates Grouped Coordinate Attention (GCA) into ResNet-50 residual blocks. GCA uses grouped coordinate modeling to jointly encode global dependencies across channels and spatial locations, strengthening feature representation and boundary delineation while adding minimal parameter and FLOP overhead compared with self-attention. On the Synapse dataset, GCA-ResUNet achieves a Dice score of 86.11%, and on the ACDC dataset, it reaches 92.64%, surpassing several state-of-the-art baselines while maintaining fast inference and favorable computational efficiency. These results indicate that GCA offers a practical way to enhance convolutional architectures with global modeling capability, enabling high-accuracy and resource-efficient medical image segmentation.

