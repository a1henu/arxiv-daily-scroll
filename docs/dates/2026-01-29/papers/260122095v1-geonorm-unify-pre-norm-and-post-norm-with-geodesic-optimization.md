---
layout: default
title: GeoNorm: Unify Pre-Norm and Post-Norm with Geodesic Optimization
---

# GeoNorm: Unify Pre-Norm and Post-Norm with Geodesic Optimization
**arXiv**：[2601.22095v1](https://arxiv.org/abs/2601.22095) · [PDF](https://arxiv.org/pdf/2601.22095.pdf)  
**作者**：Chuanyang Zheng, Jiankai Sun, Yihang Gao, Chi Wang, Yuehao Wang, Jing Xiong, Liliang Ren, Bo Peng, Qingmei Wang, Xiaoran Shang, Mac Schwager, Anderson Schneider, Yuriy Nevmyvaka, Xiaodong Liu  

**一句话要点**：提出GeoNorm方法，通过流形优化统一Transformer中的Pre-Norm和Post-Norm，提升性能且计算成本低。

**关键词**：Transformer架构, 归一化层, 流形优化, 测地线更新, 性能提升, 计算效率

## 3 点简述
- 核心问题：Transformer中归一化层（Pre-Norm和Post-Norm）的放置位置仍是一个开放性问题。
- 方法要点：基于流形优化视角，将FFN和注意力层输出解释为优化方向，用测地线更新替代标准归一化。
- 实验或效果：在Transformer模型中，GeoNorm一致优于现有归一化方法，集成简便且额外计算成本可忽略。

## 摘要（原文）

> The placement of normalization layers, specifically Pre-Norm and Post-Norm, remains an open question in Transformer architecture design. In this work, we rethink these approaches through the lens of manifold optimization, interpreting the outputs of the Feed-Forward Network (FFN) and attention layers as update directions in optimization. Building on this perspective, we introduce GeoNorm, a novel method that replaces standard normalization with geodesic updates on the manifold. Furthermore, analogous to learning rate schedules, we propose a layer-wise update decay for the FFN and attention components. Comprehensive experiments demonstrate that GeoNorm consistently outperforms existing normalization methods in Transformer models. Crucially, GeoNorm can be seamlessly integrated into standard Transformer architectures, achieving performance improvements with negligible additional computational cost.

