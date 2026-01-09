---
layout: default
title: Surface-based Molecular Design with Multi-modal Flow Matching
---

# Surface-based Molecular Design with Multi-modal Flow Matching
**arXiv**：[2601.04506v1](https://arxiv.org/abs/2601.04506) · [PDF](https://arxiv.org/pdf/2601.04506.pdf)  
**作者**：Fang Wu, Zhengyuan Zhou, Shuting Jin, Xiangxiang Zeng, Jure Leskovec, Jinbo Xu  

**一句话要点**：提出SurfFlow表面生成算法，以多模态流匹配实现肽序列、结构和表面的全面协同设计。

**关键词**：表面生成, 多模态流匹配, 肽设计, 蛋白质-蛋白质相互作用, 条件生成模型

## 3 点简述
- 问题：分子表面在蛋白质-蛋白质相互作用中作用关键，但现有肽设计方法对此探索不足。
- 方法：采用多模态条件流匹配架构，学习表面几何和生化性质分布，提升肽结合准确性。
- 效果：在PepMerge基准测试中，SurfFlow在所有指标上均优于全原子基线模型。

## 摘要（原文）

> Therapeutic peptides show promise in targeting previously undruggable binding sites, with recent advancements in deep generative models enabling full-atom peptide co-design for specific protein receptors. However, the critical role of molecular surfaces in protein-protein interactions (PPIs) has been underexplored. To bridge this gap, we propose an omni-design peptides generation paradigm, called SurfFlow, a novel surface-based generative algorithm that enables comprehensive co-design of sequence, structure, and surface for peptides. SurfFlow employs a multi-modality conditional flow matching (CFM) architecture to learn distributions of surface geometries and biochemical properties, enhancing peptide binding accuracy. Evaluated on the comprehensive PepMerge benchmark, SurfFlow consistently outperforms full-atom baselines across all metrics. These results highlight the advantages of considering molecular surfaces in de novo peptide discovery and demonstrate the potential of integrating multiple protein modalities for more effective therapeutic peptide discovery.

