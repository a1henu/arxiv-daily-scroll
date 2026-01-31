---
layout: default
title: Negatives-Dominant Contrastive Learning for Generalization in Imbalanced Domains
---

# Negatives-Dominant Contrastive Learning for Generalization in Imbalanced Domains
**arXiv**：[2601.21999v1](https://arxiv.org/abs/2601.21999) · [PDF](https://arxiv.org/pdf/2601.21999.pdf)  
**作者**：Meng Cao, Jiexi Liu, Songcan Chen  

**一句话要点**：提出负样本主导对比学习以解决不平衡领域泛化中的决策边界偏差问题

**关键词**：不平衡领域泛化, 对比学习, 决策边界优化, 后验一致性, 长尾分布

## 3 点简述
- 核心问题：不平衡领域泛化需同时处理领域和标签偏移，决策边界易偏向多数类，缺乏理论基础。
- 方法要点：通过负样本主导对比学习增强类间分离，重加权交叉熵促进类内紧凑，预测中心对齐强制领域后验一致性。
- 实验或效果：在基准测试中验证了NDCL的有效性，代码已开源。

## 摘要（原文）

> Imbalanced Domain Generalization (IDG) focuses on mitigating both domain and label shifts, both of which fundamentally shape the model's decision boundaries, particularly under heterogeneous long-tailed distributions across domains. Despite its practical significance, it remains underexplored, primarily due to the technical complexity of handling their entanglement and the paucity of theoretical foundations. In this paper, we begin by theoretically establishing the generalization bound for IDG, highlighting the role of posterior discrepancy and decision margin. This bound motivates us to focus on directly steering decision boundaries, marking a clear departure from existing methods. Subsequently, we technically propose a novel Negative-Dominant Contrastive Learning (NDCL) for IDG to enhance discriminability while enforce posterior consistency across domains. Specifically, inter-class decision-boundary separation is enhanced by placing greater emphasis on negatives as the primary signal in our contrastive learning, naturally amplifying gradient signals for minority classes to avoid the decision boundary being biased toward majority classes. Meanwhile, intra-class compactness is encouraged through a re-weighted cross-entropy strategy, and posterior consistency across domains is enforced through a prediction-central alignment strategy. Finally, rigorous yet challenging experiments on benchmarks validate the effectiveness of our NDCL. The code is available at https://github.com/Alrash/NDCL.

