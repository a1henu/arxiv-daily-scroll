---
layout: default
title: HERE: Hierarchical Active Exploration of Radiance Field with Epistemic Uncertainty Minimization
---

# HERE: Hierarchical Active Exploration of Radiance Field with Epistemic Uncertainty Minimization
**arXiv**：[2601.07242v1](https://arxiv.org/abs/2601.07242) · [PDF](https://arxiv.org/pdf/2601.07242.pdf)  
**作者**：Taekbeom Lee, Dabin Kim, Youngseok Jang, H. Jin Kim  

**一句话要点**：提出HERE框架，基于认知不确定性最小化实现神经辐射场的主动三维场景重建

**关键词**：神经辐射场, 主动三维重建, 认知不确定性, 分层探索, 相机轨迹生成

## 3 点简述
- 核心问题：主动三维重建中如何高效识别未探索区域以提升重建完整度
- 方法要点：利用证据深度学习量化认知不确定性，结合分层探索策略生成相机轨迹
- 实验或效果：在模拟场景中实现更高重建完整度，硬件演示验证现实适用性

## 摘要（原文）

> We present HERE, an active 3D scene reconstruction framework based on neural radiance fields, enabling high-fidelity implicit mapping. Our approach centers around an active learning strategy for camera trajectory generation, driven by accurate identification of unseen regions, which supports efficient data acquisition and precise scene reconstruction. The key to our approach is epistemic uncertainty quantification based on evidential deep learning, which directly captures data insufficiency and exhibits a strong correlation with reconstruction errors. This allows our framework to more reliably identify unexplored or poorly reconstructed regions compared to existing methods, leading to more informed and targeted exploration. Additionally, we design a hierarchical exploration strategy that leverages learned epistemic uncertainty, where local planning extracts target viewpoints from high-uncertainty voxels based on visibility for trajectory generation, and global planning uses uncertainty to guide large-scale coverage for efficient and comprehensive reconstruction. The effectiveness of the proposed method in active 3D reconstruction is demonstrated by achieving higher reconstruction completeness compared to previous approaches on photorealistic simulated scenes across varying scales, while a hardware demonstration further validates its real-world applicability.

