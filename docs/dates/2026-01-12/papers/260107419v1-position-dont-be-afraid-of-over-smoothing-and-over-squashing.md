---
layout: default
title: Position: Don't be Afraid of Over-Smoothing And Over-Squashing
---

# Position: Don't be Afraid of Over-Smoothing And Over-Squashing
**arXiv**：[2601.07419v1](https://arxiv.org/abs/2601.07419) · [PDF](https://arxiv.org/pdf/2601.07419.pdf)  
**作者**：Niklas Kormann, Benjamin Doerr, Johannes F. Lutzeyer  

**一句话要点**：挑战图神经网络中过度平滑与过度挤压的普遍关注，强调实际应用中其影响有限

**关键词**：图神经网络, 过度平滑, 过度挤压, 感受野分析, 信息局部化, 基准实验

## 3 点简述
- 核心问题：质疑过度平滑和过度挤压在图神经网络研究中的重要性，认为性能下降常源于无信息感受野而非这些现象
- 方法要点：通过实验分析，表明准确性与过度平滑基本无关，且缓解技术下最优模型深度仍小
- 实验或效果：在标准基准数据集上，缓解过度挤压的架构干预未能带来显著性能提升，支持信息分布常局部化

## 摘要（原文）

> Over-smoothing and over-squashing have been extensively studied in the literature on Graph Neural Networks (GNNs) over the past years. We challenge this prevailing focus in GNN research, arguing that these phenomena are less critical for practical applications than assumed. We suggest that performance decreases often stem from uninformative receptive fields rather than over-smoothing. We support this position with extensive experiments on several standard benchmark datasets, demonstrating that accuracy and over-smoothing are mostly uncorrelated and that optimal model depths remain small even with mitigation techniques, thus highlighting the negligible role of over-smoothing. Similarly, we challenge that over-squashing is always detrimental in practical applications. Instead, we posit that the distribution of relevant information over the graph frequently factorises and is often localised within a small k-hop neighbourhood, questioning the necessity of jointly observing entire receptive fields or engaging in an extensive search for long-range interactions. The results of our experiments show that architectural interventions designed to mitigate over-squashing fail to yield significant performance gains. This position paper advocates for a paradigm shift in theoretical research, urging a diligent analysis of learning tasks and datasets using statistics that measure the underlying distribution of label-relevant information to better understand their localisation and factorisation.

