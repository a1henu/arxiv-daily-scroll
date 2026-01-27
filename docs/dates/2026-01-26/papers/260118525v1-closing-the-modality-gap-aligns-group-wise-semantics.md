---
layout: default
title: Closing the Modality Gap Aligns Group-Wise Semantics
---

# Closing the Modality Gap Aligns Group-Wise Semantics
**arXiv**：[2601.18525v1](https://arxiv.org/abs/2601.18525) · [PDF](https://arxiv.org/pdf/2601.18525.pdf)  
**作者**：Eleonora Grassucci, Giordano Cicchetti, Emanuele Frasca, Aurelio Uncini, Danilo Comminiello  

**一句话要点**：提出新方法以减少模态差距，显著提升多模态学习中的组级任务性能。

**关键词**：模态差距, 多模态学习, 组级语义对齐, CLIP, 聚类任务

## 3 点简述
- 核心问题：CLIP等方法的模态差距在组级任务中影响显著，而实例级任务中影响有限。
- 方法要点：设计新方法在双模态设置中一致减少模态差距，可扩展至多模态场景。
- 实验或效果：减少模态差距对实例级任务改进有限，但显著增强聚类等组级任务性能。

## 摘要（原文）

> In multimodal learning, CLIP has been recognized as the \textit{de facto} method for learning a shared latent space across multiple modalities, placing similar representations close to each other and moving them away from dissimilar ones. Although CLIP-based losses effectively align modalities at the semantic level, the resulting latent spaces often remain only partially shared, revealing a structural mismatch known as the modality gap. While the necessity of addressing this phenomenon remains debated, particularly given its limited impact on instance-wise tasks (e.g., retrieval), we prove that its influence is instead strongly pronounced in group-level tasks (e.g., clustering). To support this claim, we introduce a novel method designed to consistently reduce this discrepancy in two-modal settings, with a straightforward extension to the general $n$-modal case. Through our extensive evaluation, we demonstrate our novel insight: while reducing the gap provides only marginal or inconsistent improvements in traditional instance-wise tasks, it significantly enhances group-wise tasks. These findings may reshape our understanding of the modality gap, highlighting its key role in improving performance on tasks requiring semantic grouping.

