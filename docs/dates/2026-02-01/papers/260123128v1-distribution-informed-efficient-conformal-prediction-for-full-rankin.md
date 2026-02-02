---
layout: default
title: Distribution-informed Efficient Conformal Prediction for Full Ranking
---

# Distribution-informed Efficient Conformal Prediction for Full Ranking
**arXiv**：[2601.23128v1](https://arxiv.org/abs/2601.23128) · [PDF](https://arxiv.org/pdf/2601.23128.pdf)  
**作者**：Wenbo Liao, Huipeng Huang, Chen Jia, Huajun Xi, Hao Zeng, Hongxin Wei  

**一句话要点**：提出分布感知的保形排序方法，以提升全排序场景中预测集效率

**关键词**：保形预测, 全排序, 不确定性量化, 负超几何分布, 预测集效率

## 3 点简述
- 核心问题：现有全排序保形预测方法依赖非一致性分数上界，导致预测集过大且保守
- 方法要点：基于相对排序推导绝对排序的负超几何分布，精确计算非一致性分数分布以确定阈值
- 实验或效果：实验显示DCR平均预测集大小减少达36%，同时保持有效覆盖保证

## 摘要（原文）

> Quantifying uncertainty is critical for the safe deployment of ranking models in real-world applications. Recent work offers a rigorous solution using conformal prediction in a full ranking scenario, which aims to construct prediction sets for the absolute ranks of test items based on the relative ranks of calibration items. However, relying on upper bounds of non-conformity scores renders the method overly conservative, resulting in substantially large prediction sets. To address this, we propose Distribution-informed Conformal Ranking (DCR), which produces efficient prediction sets by deriving the exact distribution of non-conformity scores. In particular, we find that the absolute ranks of calibration items follow Negative Hypergeometric distributions, conditional on their relative ranks. DCR thus uses the rank distribution to derive non-conformity score distribution and determine conformal thresholds. We provide theoretical guarantees that DCR achieves improved efficiency over the baseline while ensuring valid coverage under mild assumptions. Extensive experiments demonstrate the superiority of DCR, reducing average prediction set size by up to 36%, while maintaining valid coverage.

