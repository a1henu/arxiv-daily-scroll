---
layout: default
title: Distributionally Robust Classification for Multi-source Unsupervised Domain Adaptation
---

# Distributionally Robust Classification for Multi-source Unsupervised Domain Adaptation
**arXiv**：[2601.21315v1](https://arxiv.org/abs/2601.21315) · [PDF](https://arxiv.org/pdf/2601.21315.pdf)  
**作者**：Seonghwi Kim, Sung Ho Jo, Wooseok Ha, Minwoo Chae  

**一句话要点**：提出分布鲁棒学习框架以解决多源无监督域适应中目标数据稀缺和伪相关问题

**关键词**：无监督域适应, 分布鲁棒学习, 多源域适应, 伪相关, 泛化性能, 不确定性建模

## 3 点简述
- 核心问题：无监督域适应中目标数据有限或源域伪相关导致泛化性能下降
- 方法要点：建模协变量和条件标签分布的不确定性，适用于多源和单源场景
- 实验或效果：在多种分布偏移场景下优于基线，尤其在目标数据极稀缺时表现突出

## 摘要（原文）

> Unsupervised domain adaptation (UDA) is a statistical learning problem when the distribution of training (source) data is different from that of test (target) data. In this setting, one has access to labeled data only from the source domain and unlabeled data from the target domain. The central objective is to leverage the source data and the unlabeled target data to build models that generalize to the target domain. Despite its potential, existing UDA approaches often struggle in practice, particularly in scenarios where the target domain offers only limited unlabeled data or spurious correlations dominate the source domain. To address these challenges, we propose a novel distributionally robust learning framework that models uncertainty in both the covariate distribution and the conditional label distribution. Our approach is motivated by the multi-source domain adaptation setting but is also directly applicable to the single-source scenario, making it versatile in practice. We develop an efficient learning algorithm that can be seamlessly integrated with existing UDA methods. Extensive experiments under various distribution shift scenarios show that our method consistently outperforms strong baselines, especially when target data are extremely scarce.

