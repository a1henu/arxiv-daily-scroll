---
layout: default
title: PSQE: A Theoretical-Practical Approach to Pseudo Seed Quality Enhancement for Unsupervised MMEA
---

# PSQE: A Theoretical-Practical Approach to Pseudo Seed Quality Enhancement for Unsupervised MMEA
**arXiv**：[2602.22903v1](https://arxiv.org/abs/2602.22903) · [PDF](https://arxiv.org/pdf/2602.22903.pdf)  
**作者**：Yunpeng Hong, Chenyang Bu, Jie Zhang, Yi He, Di Wu, Xindong Wu  

**一句话要点**：提出PSQE以增强无监督多模态实体对齐中伪种子质量，提升精度与图覆盖平衡。

**关键词**：多模态实体对齐, 无监督学习, 伪种子增强, 对比学习, 图覆盖平衡, 聚类重采样

## 3 点简述
- 核心问题：多模态信息导致伪种子在图覆盖中不平衡，影响对齐性能。
- 方法要点：通过多模态信息和聚类重采样优化伪种子，理论分析其对对比学习的影响。
- 实验或效果：PSQE作为即插即用模块显著提升基线模型性能，验证理论发现。

## 摘要（原文）

> Multimodal Entity Alignment (MMEA) aims to identify equivalent entities across different data modalities, enabling structural data integration that in turn improves the performance of various large language model applications. To lift the requirement of labeled seed pairs that are difficult to obtain, recent methods shifted to an unsupervised paradigm using pseudo-alignment seeds. However, unsupervised entity alignment in multimodal settings remains underexplored, mainly because the incorporation of multimodal information often results in imbalanced coverage of pseudo-seeds within the knowledge graph. To overcome this, we propose PSQE (Pseudo-Seed Quality Enhancement) to improve the precision and graph coverage balance of pseudo seeds via multimodal information and clustering-resampling. Theoretical analysis reveals the impact of pseudo seeds on existing contrastive learning-based MMEA models. In particular, pseudo seeds can influence the attraction and the repulsion terms in contrastive learning at once, whereas imbalanced graph coverage causes models to prioritize high-density regions, thereby weakening their learning capability for entities in sparse regions. Experimental results validate our theoretical findings and show that PSQE as a plug-and-play module can improve the performance of baselines by considerable margins.

