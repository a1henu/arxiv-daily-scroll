---
layout: default
title: MoRel: Long-Range Flicker-Free 4D Motion Modeling via Anchor Relay-based Bidirectional Blending with Hierarchical Densification
---

# MoRel: Long-Range Flicker-Free 4D Motion Modeling via Anchor Relay-based Bidirectional Blending with Hierarchical Densification
**arXiv**：[2512.09270v1](https://arxiv.org/abs/2512.09270) · [PDF](https://arxiv.org/pdf/2512.09270.pdf)  
**作者**：Sangwoon Kwak, Weeyoung Kwon, Jun Young Jeong, Geonho Kim, Won-Sik Cheong, Jihyong Oh  

**一句话要点**：提出MoRel框架，通过锚点接力双向混合与分层致密化，解决长程动态视频建模中的内存爆炸和闪烁问题。

**关键词**：4D高斯溅射, 长程动态建模, 时间一致性, 锚点接力, 分层致密化, 内存优化

## 3 点简述
- 核心问题：现有4D高斯溅射方法在长程动态视频建模中面临内存爆炸、时间闪烁和遮挡处理失败。
- 方法要点：采用锚点接力双向混合机制，在关键帧构建局部规范锚点空间，学习双向变形以增强时间一致性。
- 实验或效果：引入特征方差引导分层致密化，并在新数据集SelfCap_LR上验证，实现内存高效、无闪烁的长程4D重建。

## 摘要（原文）

> Recent advances in 4D Gaussian Splatting (4DGS) have extended the high-speed rendering capability of 3D Gaussian Splatting (3DGS) into the temporal domain, enabling real-time rendering of dynamic scenes. However, one of the major remaining challenges lies in modeling long-range motion-contained dynamic videos, where a naive extension of existing methods leads to severe memory explosion, temporal flickering, and failure to handle appearing or disappearing occlusions over time. To address these challenges, we propose a novel 4DGS framework characterized by an Anchor Relay-based Bidirectional Blending (ARBB) mechanism, named MoRel, which enables temporally consistent and memory-efficient modeling of long-range dynamic scenes. Our method progressively constructs locally canonical anchor spaces at key-frame time index and models inter-frame deformations at the anchor level, enhancing temporal coherence. By learning bidirectional deformations between KfA and adaptively blending them through learnable opacity control, our approach mitigates temporal discontinuities and flickering artifacts. We further introduce a Feature-variance-guided Hierarchical Densification (FHD) scheme that effectively densifies KfA's while keeping rendering quality, based on an assigned level of feature-variance. To effectively evaluate our model's capability to handle real-world long-range 4D motion, we newly compose long-range 4D motion-contained dataset, called SelfCap$_{\text{LR}}$. It has larger average dynamic motion magnitude, captured at spatially wider spaces, compared to previous dynamic video datasets. Overall, our MoRel achieves temporally coherent and flicker-free long-range 4D reconstruction while maintaining bounded memory usage, demonstrating both scalability and efficiency in dynamic Gaussian-based representations.

