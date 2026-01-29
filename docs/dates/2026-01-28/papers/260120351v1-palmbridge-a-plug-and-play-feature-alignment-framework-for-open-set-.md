---
layout: default
title: PalmBridge: A Plug-and-Play Feature Alignment Framework for Open-Set Palmprint Verification
---

# PalmBridge: A Plug-and-Play Feature Alignment Framework for Open-Set Palmprint Verification
**arXiv**：[2601.20351v1](https://arxiv.org/abs/2601.20351) · [PDF](https://arxiv.org/pdf/2601.20351.pdf)  
**作者**：Chenke Zhang, Ziyuan Yang, Licheng Yan, Shuyi Li, Andrew Beng Jin Teoh, Bob Zhang, Yi Zhang  

**一句话要点**：提出PalmBridge框架以解决开放集掌纹验证中的特征分布偏移问题

**关键词**：掌纹识别, 开放集验证, 特征对齐, 向量量化, 域泛化, 嵌入空间优化

## 3 点简述
- 核心问题：掌纹识别在异构部署条件下因特征分布偏移导致性能下降，现有模型易过拟合数据集特定纹理。
- 方法要点：基于向量量化学习代表性向量，通过映射与混合抑制域偏移噪声，保留身份判别信息，结合任务监督和正则化优化。
- 实验或效果：在多个数据集和骨干架构上，PalmBridge降低等错误率，提升跨数据集泛化能力，运行时开销可忽略至适度。

## 摘要（原文）

> Palmprint recognition is widely used in biometric systems, yet real-world performance often degrades due to feature distribution shifts caused by heterogeneous deployment conditions. Most deep palmprint models assume a closed and stationary distribution, leading to overfitting to dataset-specific textures rather than learning domain-invariant representations. Although data augmentation is commonly used to mitigate this issue, it assumes augmented samples can approximate the target deployment distribution, an assumption that often fails under significant domain mismatch. To address this limitation, we propose PalmBridge, a plug-and-play feature-space alignment framework for open-set palmprint verification based on vector quantization. Rather than relying solely on data-level augmentation, PalmBridge learns a compact set of representative vectors directly from training features. During enrollment and verification, each feature vector is mapped to its nearest representative vector under a minimum-distance criterion, and the mapped vector is then blended with the original vector. This design suppresses nuisance variation induced by domain shifts while retaining discriminative identity cues. The representative vectors are jointly optimized with the backbone network using task supervision, a feature-consistency objective, and an orthogonality regularization term to form a stable and well-structured shared embedding space. Furthermore, we analyze feature-to-representative mappings via assignment consistency and collision rate to assess model's sensitivity to blending weights. Experiments on multiple palmprint datasets and backbone architectures show that PalmBridge consistently reduces EER in intra-dataset open-set evaluation and improves cross-dataset generalization with negligible to modest runtime overhead.

