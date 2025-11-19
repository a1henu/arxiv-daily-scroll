---
layout: default
title: Co-Me: Confidence-Guided Token Merging for Visual Geometric Transformers
---

# Co-Me: Confidence-Guided Token Merging for Visual Geometric Transformers
**arXiv**：[2511.14751v1](https://arxiv.org/abs/2511.14751) · [PDF](https://arxiv.org/pdf/2511.14751.pdf)  
**作者**：Yutian Chen, Yuheng Qiu, Ruogu Li, Ali Agha, Shayegan Omidshafiei, Jay Patrikar, Sebastian Scherer  

**一句话要点**：提出置信引导令牌合并以加速视觉几何变换器，无需重训练。

**关键词**：令牌合并, 视觉几何变换器, 置信预测, 实时3D感知, 多视图视觉, 计算加速

## 3 点简述
- 视觉几何变换器计算量大，难以实时应用。
- 通过轻量置信预测器评估令牌不确定性，选择性合并低置信令牌。
- 在VGGT和MapAnything上实现最高11.3倍和7.2倍加速，性能未降。

## 摘要（原文）

> We propose Confidence-Guided Token Merging (Co-Me), an acceleration mechanism for visual geometric transformers without retraining or finetuning the base model. Co-Me distilled a light-weight confidence predictor to rank tokens by uncertainty and selectively merge low-confidence ones, effectively reducing computation while maintaining spatial coverage. Compared to similarity-based merging or pruning, the confidence signal in Co-Me reliably indicates regions emphasized by the transformer, enabling substantial acceleration without degrading performance. Co-Me applies seamlessly to various multi-view and streaming visual geometric transformers, achieving speedups that scale with sequence length. When applied to VGGT and MapAnything, Co-Me achieves up to $11.3\times$ and $7.2\times$ speedup, making visual geometric transformers practical for real-time 3D perception and reconstruction.

