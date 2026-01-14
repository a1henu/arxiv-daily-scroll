---
layout: default
title: M3SR: Multi-Scale Multi-Perceptual Mamba for Efficient Spectral Reconstruction
---

# M3SR: Multi-Scale Multi-Perceptual Mamba for Efficient Spectral Reconstruction
**arXiv**：[2601.08293v1](https://arxiv.org/abs/2601.08293) · [PDF](https://arxiv.org/pdf/2601.08293.pdf)  
**作者**：Yuze Zhang, Lingjie Li, Qiuzhen Lin, Zhong Ming, Fei Yu, Victor C. M. Leung  

**一句话要点**：提出多尺度多感知Mamba架构M3SR以高效解决高光谱图像重建中的感知与尺度限制问题。

**关键词**：高光谱图像重建, Mamba架构, 多尺度特征提取, 多感知融合, U-Net结构, 计算效率

## 3 点简述
- 核心问题：现有Mamba架构在高光谱重建中面临单空间感知和单尺度特征提取的限制，影响图像理解与细节捕捉。
- 方法要点：设计多感知融合块，结合U-Net结构，实现全局、中间和局部特征的多尺度提取与融合。
- 实验或效果：实验表明M3SR在计算成本较低的情况下，性能优于现有先进方法，实现准确重建。

## 摘要（原文）

> The Mamba architecture has been widely applied to various low-level vision tasks due to its exceptional adaptability and strong performance. Although the Mamba architecture has been adopted for spectral reconstruction, it still faces the following two challenges: (1) Single spatial perception limits the ability to fully understand and analyze hyperspectral images; (2) Single-scale feature extraction struggles to capture the complex structures and fine details present in hyperspectral images. To address these issues, we propose a multi-scale, multi-perceptual Mamba architecture for the spectral reconstruction task, called M3SR. Specifically, we design a multi-perceptual fusion block to enhance the ability of the model to comprehensively understand and analyze the input features. By integrating the multi-perceptual fusion block into a U-Net structure, M3SR can effectively extract and fuse global, intermediate, and local features, thereby enabling accurate reconstruction of hyperspectral images at multiple scales. Extensive quantitative and qualitative experiments demonstrate that the proposed M3SR outperforms existing state-of-the-art methods while incurring a lower computational cost.

