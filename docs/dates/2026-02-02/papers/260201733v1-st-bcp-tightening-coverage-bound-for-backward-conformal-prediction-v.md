---
layout: default
title: ST-BCP: Tightening Coverage Bound for Backward Conformal Prediction via Non-Conformity Score Transformation
---

# ST-BCP: Tightening Coverage Bound for Backward Conformal Prediction via Non-Conformity Score Transformation
**arXiv**：[2602.01733v1](https://arxiv.org/abs/2602.01733) · [PDF](https://arxiv.org/pdf/2602.01733.pdf)  
**作者**：Junxian Liu, Hao Zeng, Hongxin Wei  

**一句话要点**：提出ST-BCP方法，通过非一致性分数变换收紧后向共形预测的覆盖界

**关键词**：共形预测, 后向共形预测, 不确定性量化, 非一致性分数, 覆盖界, 统计框架

## 3 点简述
- 后向共形预测中马尔可夫不等式导致覆盖界估计与经验覆盖存在显著差距
- 引入数据依赖的非一致性分数变换以缩小覆盖差距，并证明优于基线变换
- 实验显示平均覆盖差距从4.20%降至1.12%，验证方法有效性

## 摘要（原文）

> Conformal Prediction (CP) provides a statistical framework for uncertainty quantification that constructs prediction sets with coverage guarantees. While CP yields uncontrolled prediction set sizes, Backward Conformal Prediction (BCP) inverts this paradigm by enforcing a predefined upper bound on set size and estimating the resulting coverage guarantee. However, the looseness induced by Markov's inequality within the BCP framework causes a significant gap between the estimated coverage bound and the empirical coverage. In this work, we introduce ST-BCP, a novel method that introduces a data-dependent transformation of nonconformity scores to narrow the coverage gap. In particular, we develop a computable transformation and prove that it outperforms the baseline identity transformation. Extensive experiments demonstrate the effectiveness of our method, reducing the average coverage gap from 4.20\% to 1.12\% on common benchmarks.

