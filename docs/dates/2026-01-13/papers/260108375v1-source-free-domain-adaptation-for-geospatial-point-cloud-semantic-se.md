---
layout: default
title: Source-Free Domain Adaptation for Geospatial Point Cloud Semantic Segmentation
---

# Source-Free Domain Adaptation for Geospatial Point Cloud Semantic Segmentation
**arXiv**：[2601.08375v1](https://arxiv.org/abs/2601.08375) · [PDF](https://arxiv.org/pdf/2601.08375.pdf)  
**作者**：Yuan Gao, Di Cao, Xiaohuan Xi, Sheng Nie, Shaobo Xia, Cheng Wang  

**一句话要点**：提出LoGo框架以解决地理点云语义分割中的源自由域适应问题

**关键词**：源自由域适应, 地理点云语义分割, 长尾分布, 最优传输, 伪标签过滤, 自训练

## 3 点简述
- 核心问题：地理点云语义分割中，域偏移和长尾分布导致模型性能下降，且源域数据不可用。
- 方法要点：LoGo框架结合局部类平衡原型估计和全局最优传输对齐，通过双一致性伪标签过滤进行自训练。
- 实验或效果：未知，但方法旨在缓解特征崩溃和类别偏差，提升目标域分割性能。

## 摘要（原文）

> Semantic segmentation of 3D geospatial point clouds is pivotal for remote sensing applications. However, variations in geographic patterns across regions and data acquisition strategies induce significant domain shifts, severely degrading the performance of deployed models. Existing domain adaptation methods typically rely on access to source-domain data. However, this requirement is rarely met due to data privacy concerns, regulatory policies, and data transmission limitations. This motivates the largely underexplored setting of source-free unsupervised domain adaptation (SFUDA), where only a pretrained model and unlabeled target-domain data are available. In this paper, we propose LoGo (Local-Global Dual-Consensus), a novel SFUDA framework specifically designed for geospatial point clouds. At the local level, we introduce a class-balanced prototype estimation module that abandons conventional global threshold filtering in favor of an intra-class independent anchor mining strategy. This ensures that robust feature prototypes can be generated even for sample-scarce tail classes, effectively mitigating the feature collapse caused by long-tailed distributions. At the global level, we introduce an optimal transport-based global distribution alignment module that formulates pseudo-label assignment as a global optimization problem. By enforcing global distribution constraints, this module effectively corrects the over-dominance of head classes inherent in local greedy assignments, preventing model predictions from being severely biased towards majority classes. Finally, we propose a dual-consistency pseudo-label filtering mechanism. This strategy retains only high-confidence pseudo-labels where local multi-augmented ensemble predictions align with global optimal transport assignments for self-training.

