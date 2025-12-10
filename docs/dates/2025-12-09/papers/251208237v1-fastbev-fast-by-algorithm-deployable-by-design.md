---
layout: default
title: FastBEV++: Fast by Algorithm, Deployable by Design
---

# FastBEV++: Fast by Algorithm, Deployable by Design
**arXiv**：[2512.08237v1](https://arxiv.org/abs/2512.08237) · [PDF](https://arxiv.org/pdf/2512.08237.pdf)  
**作者**：Yuanpeng Chen, Hui Song, Wei Tao, ShanHui Mo, Shuang Zhang, Xiao Hua, TianKun Zhao  

**一句话要点**：提出FastBEV++框架，通过算法优化与设计可部署性解决相机BEV感知的性能与部署矛盾。

**关键词**：鸟瞰图感知, 视图变换, 实时部署, 深度融合, 自动驾驶系统

## 3 点简述
- 核心问题：相机BEV感知依赖计算密集的视图变换和定制内核，导致性能与部署效率冲突。
- 方法要点：采用分解视图变换为标准索引-聚集-重塑流程，结合深度感知融合，提升几何保真度。
- 实验或效果：在nuScenes基准上达到0.359 NDS，Tesla T4硬件上超过134 FPS，实现高精度与实时性。

## 摘要（原文）

> The advancement of camera-only Bird's-Eye-View(BEV) perception is currently impeded by a fundamental tension between state-of-the-art performance and on-vehicle deployment tractability. This bottleneck stems from a deep-rooted dependency on computationally prohibitive view transformations and bespoke, platform-specific kernels. This paper introduces FastBEV++, a framework engineered to reconcile this tension, demonstrating that high performance and deployment efficiency can be achieved in unison via two guiding principles: Fast by Algorithm and Deployable by Design. We realize the "Deployable by Design" principle through a novel view transformation paradigm that decomposes the monolithic projection into a standard Index-Gather-Reshape pipeline. Enabled by a deterministic pre-sorting strategy, this transformation is executed entirely with elementary, operator native primitives (e.g Gather, Matrix Multiplication), which eliminates the need for specialized CUDA kernels and ensures fully TensorRT-native portability. Concurrently, our framework is "Fast by Algorithm", leveraging this decomposed structure to seamlessly integrate an end-to-end, depth-aware fusion mechanism. This jointly learned depth modulation, further bolstered by temporal aggregation and robust data augmentation, significantly enhances the geometric fidelity of the BEV representation.Empirical validation on the nuScenes benchmark corroborates the efficacy of our approach. FastBEV++ establishes a new state-of-the-art 0.359 NDS while maintaining exceptional real-time performance, exceeding 134 FPS on automotive-grade hardware (e.g Tesla T4). By offering a solution that is free of custom plugins yet highly accurate, FastBEV++ presents a mature and scalable design philosophy for production autonomous systems. The code is released at: https://github.com/ymlab/advanced-fastbev

