---
layout: default
title: Cross-view geo-localization, Image retrieval, Multiscale geometric modeling, Frequency domain enhancement
---

# Cross-view geo-localization, Image retrieval, Multiscale geometric modeling, Frequency domain enhancement
**arXiv**：[2603.02726v1](https://arxiv.org/abs/2603.02726) · [PDF](https://arxiv.org/pdf/2603.02726.pdf)  
**作者**：Hongying Zhang, ShuaiShuai Ma  

**一句话要点**：提出SFDE网络，通过空间与频域增强解决跨视角地理定位中的几何不对称与纹理不一致问题。

**关键词**：跨视角地理定位, 图像检索, 多尺度几何建模, 频域增强, 特征对齐

## 3 点简述
- 核心问题：跨视角地理定位面临几何不对称、纹理不一致和局部信息退化挑战。
- 方法要点：采用三分支并行架构，建模全局语义、局部几何和频域统计稳定性。
- 实验或效果：在实验中表现优异，超越现有方法，同时保持轻量高效设计。

## 摘要（原文）

> Cross-view geo-localization (CVGL) aims to establish spatial correspondences between images captured from significantly different viewpoints and constitutes a fundamental technique for visual localization in GNSS-denied environments. Nevertheless, CVGL remains challenging due to severe geometric asymmetry, texture inconsistency across imaging domains, and the progressive degradation of discriminative local information. Existing methods predominantly rely on spatial domain feature alignment, which is inherently sensitive to large scale viewpoint variations and local disturbances. To alleviate these limitations, this paper proposes the Spatial and Frequency Domain Enhancement Network (SFDE), which leverages complementary representations from spatial and frequency domains. SFDE adopts a three branch parallel architecture to model global semantic context, local geometric structure, and statistical stability in the frequency domain, respectively, thereby characterizing consistency across domains from the perspectives of scene topology, multiscale structural patterns, and frequency invariance. The resulting complementary features are jointly optimized in a unified embedding space via progressive enhancement and coupled constraints, enabling the learning of cross-view representations with consistency across multiple granularities. Comprehensive experiments show that SFDE achieves competitive performance and in many cases even surpasses state-of-the-art methods, while maintaining a lightweight and computationally efficient design. {Our code is available at https://github.com/Mashuaishuai669/SFDE

