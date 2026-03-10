---
layout: default
title: Enhancing Unregistered Hyperspectral Image Super-Resolution via Unmixing-based Abundance Fusion Learning
---

# Enhancing Unregistered Hyperspectral Image Super-Resolution via Unmixing-based Abundance Fusion Learning
**arXiv**：[2603.07918v1](https://arxiv.org/abs/2603.07918) · [PDF](https://arxiv.org/pdf/2603.07918.pdf)  
**作者**：Yingkai Zhang, Tao Zhang, Jing Nie, Ying Fu  

**一句话要点**：提出基于解混的丰度融合学习框架，以增强未配准高光谱图像超分辨率

**关键词**：高光谱图像超分辨率, 未配准图像融合, 解混学习, 可变形聚合, 空间-通道注意力, 丰度图增强

## 3 点简述
- 核心问题：未配准高光谱图像超分辨率中，参考图像未对齐影响融合效果与模型学习能力。
- 方法要点：通过解耦空间-光谱信息，利用奇异值分解进行初始解混，并设计粗到细可变形聚合模块与空间-通道注意力块优化丰度图。
- 实验或效果：在模拟和真实数据集上验证了方法达到最先进的超分辨率性能，代码将开源。

## 摘要（原文）

> Unregistered hyperspectral image (HSI) super-resolution (SR) typically aims to enhance a low-resolution HSI using an unregistered high-resolution reference image. In this paper, we propose an unmixing-based fusion framework that decouples spatial-spectral information to simultaneously mitigate the impact of unregistered fusion and enhance the learnability of SR models. Specifically, we first utilize singular value decomposition for initial spectral unmixing, preserving the original endmembers while dedicating the subsequent network to enhancing the initial abundance map. To leverage the spatial texture of the unregistered reference, we introduce a coarse-to-fine deformable aggregation module, which first estimates a pixel-level flow and a similarity map using a coarse pyramid predictor. It further performs fine sub-pixel refinement to achieve deformable aggregation of the reference features. The aggregative features are then refined via a series of spatial-channel abundance cross-attention blocks. Furthermore, a spatial-channel modulated fusion module is presented to merge encoder-decoder features using dynamic gating weights, yielding a high-quality, high-resolution HSI. Experimental results on simulated and real datasets confirm that our proposed method achieves state-of-the-art super-resolution performance. The code will be available at https://github.com/yingkai-zhang/UAFL.

