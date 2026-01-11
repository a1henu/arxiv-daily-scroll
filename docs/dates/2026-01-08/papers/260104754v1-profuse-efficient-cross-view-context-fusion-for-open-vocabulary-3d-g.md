---
layout: default
title: ProFuse: Efficient Cross-View Context Fusion for Open-Vocabulary 3D Gaussian Splatting
---

# ProFuse: Efficient Cross-View Context Fusion for Open-Vocabulary 3D Gaussian Splatting
**arXiv**：[2601.04754v1](https://arxiv.org/abs/2601.04754) · [PDF](https://arxiv.org/pdf/2601.04754.pdf)  
**作者**：Yen-Jen Chiou, Wei-Tse Cheng, Yuan-Fu Yang  

**一句话要点**：提出ProFuse框架，通过高效跨视图上下文融合实现开放词汇3D高斯泼溅场景理解。

**关键词**：开放词汇3D场景理解, 3D高斯泼溅, 跨视图上下文融合, 密集对应引导, 语义附着, 高效优化

## 3 点简述
- 核心问题：开放词汇3D场景理解中跨视图一致性和掩码内聚性不足，现有方法效率低。
- 方法要点：引入密集对应引导预注册，构建3D上下文提案并融合全局特征，无需额外优化。
- 实验或效果：在标准重建上实现语义附着，每场景约5分钟，比SOTA快两倍，保持几何细化。

## 摘要（原文）

> We present ProFuse, an efficient context-aware framework for open-vocabulary 3D scene understanding with 3D Gaussian Splatting (3DGS). The pipeline enhances cross-view consistency and intra-mask cohesion within a direct registration setup, adding minimal overhead and requiring no render-supervised fine-tuning. Instead of relying on a pretrained 3DGS scene, we introduce a dense correspondence-guided pre-registration phase that initializes Gaussians with accurate geometry while jointly constructing 3D Context Proposals via cross-view clustering. Each proposal carries a global feature obtained through weighted aggregation of member embeddings, and this feature is fused onto Gaussians during direct registration to maintain per-primitive language coherence across views. With associations established in advance, semantic fusion requires no additional optimization beyond standard reconstruction, and the model retains geometric refinement without densification. ProFuse achieves strong open-vocabulary 3DGS understanding while completing semantic attachment in about five minutes per scene, which is two times faster than SOTA.

