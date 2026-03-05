---
layout: default
title: Glass Segmentation with Fusion of Learned and General Visual Features
---

# Glass Segmentation with Fusion of Learned and General Visual Features
**arXiv**：[2603.03718v1](https://arxiv.org/abs/2603.03718) · [PDF](https://arxiv.org/pdf/2603.03718.pdf)  
**作者**：Risto Ojala, Tristan Ellison, Mo Chen  

**一句话要点**：提出融合通用与任务特定视觉特征的双骨干网络，用于RGB图像中的玻璃表面分割。

**关键词**：玻璃分割, 双骨干网络, 视觉特征融合, DINOv3, Swin Transformer, Mask2Former

## 3 点简述
- 核心问题：玻璃作为透明材料缺乏视觉特征，分割困难但关键于场景理解和机器人应用。
- 方法要点：结合冻结DINOv3的通用特征和Swin模型的任务特定特征，经残差SE通道降维后输入Mask2Former解码器。
- 实验或效果：在四个数据集上实现SOTA精度，推理速度具竞争力，轻量DINOv3变体更优。

## 摘要（原文）

> Glass surface segmentation from RGB images is a challenging task, since glass as a transparent material distinctly lacks visual characteristics. However, glass segmentation is critical for scene understanding and robotics, as transparent glass surfaces must be identified as solid material. This paper presents a novel architecture for glass segmentation, deploying a dual-backbone producing general visual features as well as task-specific learned visual features. General visual features are produced by a frozen DINOv3 vision foundation model, and the task-specific features are generated with a Swin model trained in a supervised manner. Resulting multi-scale feature representations are downsampled with residual Squeeze-and-Excitation Channel Reduction, and fed into a Mask2Former Decoder, producing the final segmentation masks. The architecture was evaluated on four commonly used glass segmentation datasets, achieving state-of-the-art results on several accuracy metrics. The model also has a competitive inference speed compared to the previous state-of-the-art method, and surpasses it when using a lighter DINOv3 backbone variant. The implementation source code and model weights are available at: https://github.com/ojalar/lgnet

