---
layout: default
title: On the Unreasonable Effectiveness of Last-layer Retraining
---

# On the Unreasonable Effectiveness of Last-layer Retraining
**arXiv**：[2512.01766v1](https://arxiv.org/abs/2512.01766) · [PDF](https://arxiv.org/pdf/2512.01766.pdf)  
**作者**：John C. Hill, Tyler LaBonte, Xinchen Zhang, Vidya Muthukumar  

**一句话要点**：揭示最后一层重训练有效性的原因，强调保留集组平衡的关键作用

**关键词**：最后一层重训练, 虚假相关性, 组平衡, 鲁棒性, 梯度下降隐式偏差

## 3 点简述
- 研究最后一层重训练在缓解虚假相关性和提升少数群体性能中的高效性
- 通过实验否定神经崩溃缓解假说，证明保留集组平衡是主要驱动因素
- 展示CB-LLR和AFR算法通过隐式组平衡实现鲁棒性改进

## 摘要（原文）

> Last-layer retraining (LLR) methods -- wherein the last layer of a neural network is reinitialized and retrained on a held-out set following ERM training -- have garnered interest as an efficient approach to rectify dependence on spurious correlations and improve performance on minority groups. Surprisingly, LLR has been found to improve worst-group accuracy even when the held-out set is an imbalanced subset of the training set. We initially hypothesize that this ``unreasonable effectiveness'' of LLR is explained by its ability to mitigate neural collapse through the held-out set, resulting in the implicit bias of gradient descent benefiting robustness. Our empirical investigation does not support this hypothesis. Instead, we present strong evidence for an alternative hypothesis: that the success of LLR is primarily due to better group balance in the held-out set. We conclude by showing how the recent algorithms CB-LLR and AFR perform implicit group-balancing to elicit a robustness improvement.

