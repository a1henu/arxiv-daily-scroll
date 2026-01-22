---
layout: default
title: UniRoute: Unified Routing Mixture-of-Experts for Modality-Adaptive Remote Sensing Change Detection
---

# UniRoute: Unified Routing Mixture-of-Experts for Modality-Adaptive Remote Sensing Change Detection
**arXiv**：[2601.14797v1](https://arxiv.org/abs/2601.14797) · [PDF](https://arxiv.org/pdf/2601.14797.pdf)  
**作者**：Qingling Shu, Sibao Chen, Wei Lu, Zhihui You, Chengzhuang Liu  

**一句话要点**：提出UniRoute统一框架，通过条件路由解决遥感变化检测中的模态自适应问题。

**关键词**：遥感变化检测, 模态自适应学习, 混合专家路由, 自蒸馏训练, 统一部署

## 3 点简述
- 核心问题：现有遥感变化检测方法依赖专用模型，难以适应不同模态数据，导致边界模糊或噪声干扰。
- 方法要点：引入AR2-MoE和MDR-MoE模块，自适应提取特征和融合差异，结合CASD策略稳定训练。
- 实验或效果：在五个公开数据集上验证，实现强整体性能和精度-效率平衡。

## 摘要（原文）

> Current remote sensing change detection (CD) methods mainly rely on specialized models, which limits the scalability toward modality-adaptive Earth observation. For homogeneous CD, precise boundary delineation relies on fine-grained spatial cues and local pixel interactions, whereas heterogeneous CD instead requires broader contextual information to suppress speckle noise and geometric distortions. Moreover, difference operator (e.g., subtraction) works well for aligned homogeneous images but introduces artifacts in cross-modal or geometrically misaligned scenarios. Across different modality settings, specialized models based on static backbones or fixed difference operations often prove insufficient. To address this challenge, we propose UniRoute, a unified framework for modality-adaptive learning by reformulating feature extraction and fusion as conditional routing problems. We introduce an Adaptive Receptive Field Routing MoE (AR2-MoE) module to disentangle local spatial details from global semantic context, and a Modality-Aware Difference Routing MoE (MDR-MoE) module to adaptively select the most suitable fusion primitive at each pixel. In addition, we propose a Consistency-Aware Self-Distillation (CASD) strategy that stabilizes unified training under data-scarce heterogeneous settings by enforcing multi-level consistency. Extensive experiments on five public datasets demonstrate that UniRoute achieves strong overall performance, with a favorable accuracy-efficiency trade-off under a unified deployment setting.

