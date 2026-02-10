---
layout: default
title: Revisiting [CLS] and Patch Token Interaction in Vision Transformers
---

# Revisiting [CLS] and Patch Token Interaction in Vision Transformers
**arXiv**：[2602.08626v1](https://arxiv.org/abs/2602.08626) · [PDF](https://arxiv.org/pdf/2602.08626.pdf)  
**作者**：Alexis Marouani, Oriane Siméoni, Hervé Jégou, Piotr Bojanowski, Huy V. Vo  

**一句话要点**：提出专门化处理路径以提升视觉Transformer中补丁表示质量，用于密集预测任务。

**关键词**：视觉Transformer, 令牌交互, 专门化处理, 密集预测, 分割性能, 标准化层

## 3 点简述
- 分析[CLS]与补丁令牌交互，发现标准化层导致隐式差异。
- 设计专门化路径，在标准化层和早期投影中分离令牌计算流。
- 实验显示分割性能提升超2 mIoU点，参数仅增8%，无额外计算开销。

## 摘要（原文）

> Vision Transformers have emerged as powerful, scalable and versatile representation learners. To capture both global and local features, a learnable [CLS] class token is typically prepended to the input sequence of patch tokens. Despite their distinct nature, both token types are processed identically throughout the model. In this work, we investigate the friction between global and local feature learning under different pre-training strategies by analyzing the interactions between class and patch tokens. Our analysis reveals that standard normalization layers introduce an implicit differentiation between these token types. Building on this insight, we propose specialized processing paths that selectively disentangle the computational flow of class and patch tokens, particularly within normalization layers and early query-key-value projections. This targeted specialization leads to significantly improved patch representation quality for dense prediction tasks. Our experiments demonstrate segmentation performance gains of over 2 mIoU points on standard benchmarks, while maintaining strong classification accuracy. The proposed modifications introduce only an 8% increase in parameters, with no additional computational overhead. Through comprehensive ablations, we provide insights into which architectural components benefit most from specialization and how our approach generalizes across model scales and learning frameworks.

