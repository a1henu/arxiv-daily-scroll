---
layout: default
title: Facial Expression Recognition Using Residual Masking Network
---

# Facial Expression Recognition Using Residual Masking Network
**arXiv**：[2603.05937v1](https://arxiv.org/abs/2603.05937) · [PDF](https://arxiv.org/pdf/2603.05937.pdf)  
**作者**：Luan Pham, The Huynh Vu, Tuan Anh Tran  

**一句话要点**：提出残差掩码网络以提升面部表情识别性能，结合注意力机制优化特征图。

**关键词**：面部表情识别, 残差网络, 注意力机制, 特征掩码, 深度学习架构, 计算机视觉

## 3 点简述
- 核心问题：自动面部表情识别在深度学习中需提升特征聚焦能力。
- 方法要点：引入掩码思想，通过分割网络精炼特征图，增强相关区域注意力。
- 实验或效果：在FER2013和VEMO数据集上达到SOTA准确率，代码开源。

## 摘要（原文）

> Automatic facial expression recognition (FER) has gained much attention due to its applications in human-computer interaction. Among the approaches to improve FER tasks, this paper focuses on deep architecture with the attention mechanism. We propose a novel Masking idea to boost the performance of CNN in facial expression task. It uses a segmentation network to refine feature maps, enabling the network to focus on relevant information to make correct decisions. In experiments, we combine the ubiquitous Deep Residual Network and Unet-like architecture to produce a Residual Masking Network. The proposed method holds state-of-the-art (SOTA) accuracy on the well-known FER2013 and private VEMO datasets. The source code is available at https://github.com/phamquiluan/ResidualMaskingNetwork.

