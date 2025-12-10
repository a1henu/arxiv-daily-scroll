---
layout: default
title: Fused Gromov-Wasserstein Contrastive Learning for Effective Enzyme-Reaction Screening
---

# Fused Gromov-Wasserstein Contrastive Learning for Effective Enzyme-Reaction Screening
**arXiv**：[2512.08508v1](https://arxiv.org/abs/2512.08508) · [PDF](https://arxiv.org/pdf/2512.08508.pdf)  
**作者**：Gengmo Zhou, Feng Yu, Wenda Wang, Zhifeng Gao, Guolin Ke, Zhewei Wei, Zhen Wang  

**一句话要点**：提出FGW-CLIP对比学习框架以优化酶-反应筛选任务

**关键词**：酶-反应筛选, 对比学习, Gromov-Wasserstein距离, 生物信息学, 深度学习

## 3 点简述
- 核心问题：传统酶筛选方法耗时且忽略酶与反应域内层次关系
- 方法要点：基于融合Gromov-Wasserstein距离，结合域间与域内对齐
- 实验或效果：在EnzymeMap和ReactZyme基准上实现最优性能，泛化性强

## 摘要（原文）

> Enzymes are crucial catalysts that enable a wide range of biochemical reactions. Efficiently identifying specific enzymes from vast protein libraries is essential for advancing biocatalysis. Traditional computational methods for enzyme screening and retrieval are time-consuming and resource-intensive. Recently, deep learning approaches have shown promise. However, these methods focus solely on the interaction between enzymes and reactions, overlooking the inherent hierarchical relationships within each domain. To address these limitations, we introduce FGW-CLIP, a novel contrastive learning framework based on optimizing the fused Gromov-Wasserstein distance. FGW-CLIP incorporates multiple alignments, including inter-domain alignment between reactions and enzymes and intra-domain alignment within enzymes and reactions. By introducing a tailored regularization term, our method minimizes the Gromov-Wasserstein distance between enzyme and reaction spaces, which enhances information integration across these domains. Extensive evaluations demonstrate the superiority of FGW-CLIP in challenging enzyme-reaction tasks. On the widely-used EnzymeMap benchmark, FGW-CLIP achieves state-of-the-art performance in enzyme virtual screening, as measured by BEDROC and EF metrics. Moreover, FGW-CLIP consistently outperforms across all three splits of ReactZyme, the largest enzyme-reaction benchmark, demonstrating robust generalization to novel enzymes and reactions. These results position FGW-CLIP as a promising framework for enzyme discovery in complex biochemical settings, with strong adaptability across diverse screening scenarios.

