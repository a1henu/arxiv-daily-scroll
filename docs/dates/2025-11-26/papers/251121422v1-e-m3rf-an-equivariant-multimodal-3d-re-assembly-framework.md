---
layout: default
title: E-M3RF: An Equivariant Multimodal 3D Re-assembly Framework
---

# E-M3RF: An Equivariant Multimodal 3D Re-assembly Framework
**arXiv**：[2511.21422v1](https://arxiv.org/abs/2511.21422) · [PDF](https://arxiv.org/pdf/2511.21422.pdf)  
**作者**：Adeela Islam, Stefano Fiorini, Manuel Lecha, Theodore Tsesmelis, Stuart James, Pietro Morerio, Alessio Del Bue  

**一句话要点**：提出E-M3RF框架，利用多模态特征解决3D碎片重组的几何模糊问题

**关键词**：3D重组, 多模态特征, SE(3)流匹配, 旋转等变编码, 文化遗产修复

## 3 点简述
- 核心问题：3D重组中仅依赖几何特征易受碎片小、侵蚀或对称性影响，且缺乏物理约束防止重叠
- 方法要点：结合几何和颜色特征，使用SE(3)流匹配预测变换，实现旋转等变编码
- 实验或效果：在RePAIR数据集上，旋转误差降低23.1%，平移误差降低13.2%，Chamfer距离减少18.4%

## 摘要（原文）

> 3D reassembly is a fundamental geometric problem, and in recent years it has increasingly been challenged by deep learning methods rather than classical optimization. While learning approaches have shown promising results, most still rely primarily on geometric features to assemble a whole from its parts. As a result, methods struggle when geometry alone is insufficient or ambiguous, for example, for small, eroded, or symmetric fragments. Additionally, solutions do not impose physical constraints that explicitly prevent overlapping assemblies. To address these limitations, we introduce E-M3RF, an equivariant multimodal 3D reassembly framework that takes as input the point clouds, containing both point positions and colors of fractured fragments, and predicts the transformations required to reassemble them using SE(3) flow matching. Each fragment is represented by both geometric and color features: i) 3D point positions are encoded as rotationconsistent geometric features using a rotation-equivariant encoder, ii) the colors at each 3D point are encoded with a transformer. The two feature sets are then combined to form a multimodal representation. We experimented on four datasets: two synthetic datasets, Breaking Bad and Fantastic Breaks, and two real-world cultural heritage datasets, RePAIR and Presious, demonstrating that E-M3RF on the RePAIR dataset reduces rotation error by 23.1% and translation error by 13.2%, while Chamfer Distance decreases by 18.4% compared to competing methods.

