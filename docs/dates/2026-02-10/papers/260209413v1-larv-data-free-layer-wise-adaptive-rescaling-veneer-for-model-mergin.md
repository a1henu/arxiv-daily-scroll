---
layout: default
title: LARV: Data-Free Layer-wise Adaptive Rescaling Veneer for Model Merging
---

# LARV: Data-Free Layer-wise Adaptive Rescaling Veneer for Model Merging
**arXiv**：[2602.09413v1](https://arxiv.org/abs/2602.09413) · [PDF](https://arxiv.org/pdf/2602.09413.pdf)  
**作者**：Xinyu Wang, Ke Deng, Fei Dou, Jinbo Bi, Jin Lu  

**一句话要点**：提出LARV以解决模型合并中忽略层间异质性的问题，通过层自适应缩放提升任务向量合并性能。

**关键词**：模型合并, 任务向量, 层自适应缩放, 视觉变换器, 数据无关方法

## 3 点简述
- 核心问题：现有任务向量合并方法假设层间均匀，忽略视觉变换器中浅层敏感、深层稳定的异质性。
- 方法要点：LARV为训练无关、数据无关的层自适应缩放层，为每个任务向量分配逐层缩放因子，抑制浅层干扰并放大深层对齐。
- 实验或效果：在FusionBench上，LARV一致改进多种基线，如Iso-C + LARV在ViT模型上达到85.9%-92.6%准确率。

## 摘要（原文）

> Model merging aims to combine multiple fine-tuned models into a single multi-task model without access to training data. Existing task-vector merging methods such as TIES, TSV-M, and Iso-C/CTS differ in their aggregation rules but treat all layers nearly uniformly. This assumption overlooks the strong layer-wise heterogeneity in large vision transformers, where shallow layers are sensitive to interference while deeper layers encode stable task-specific features. We introduce LARV, a training-free, data-free, merger-agnostic Layer-wise Adaptive Rescaling Veneer that plugs into any task-vector merger and assigns a per-layer scale to each task vector before aggregation, and show it consistently boosts diverse merging rules. LARV adaptively suppresses shallow-layer interference and amplifies deeper-layer alignment using a simple deterministic schedule, requiring no retraining or modification to existing mergers. To our knowledge, this is the first work to perform layer-aware scaling for task-vector merging. LARV computes simple data-free layer proxies and turns them into scales through a lightweight rule; we study several instantiations within one framework (e.g., tiered two/three-level scaling with fixed values, or continuous mappings) and show that tiered choices offer the best robustness, while continuous mappings remain an ablation. LARV is orthogonal to the base merger and adds negligible cost. On FusionBench with Vision Transformers, LARV consistently improves all task-vector baselines across 8/14/20-task settings; for example, Iso-C + LARV reaches 85.9% on ViT-B/32, 89.2% on ViT-B/16, and 92.6% on ViT-L/14. Layerwise analysis and corruption tests further indicate that LARV suppresses shallow-layer interference while modestly amplifying deeper, task-stable features, turning model merging into a robust, layer-aware procedure rather than a uniform one.

