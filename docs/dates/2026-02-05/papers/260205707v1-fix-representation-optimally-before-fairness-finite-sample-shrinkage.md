---
layout: default
title: Fix Representation (Optimally) Before Fairness: Finite-Sample Shrinkage Population Correction and the True Price of Fairness Under Subpopulation Shift
---

# Fix Representation (Optimally) Before Fairness: Finite-Sample Shrinkage Population Correction and the True Price of Fairness Under Subpopulation Shift
**arXiv**：[2602.05707v1](https://arxiv.org/abs/2602.05707) · [PDF](https://arxiv.org/pdf/2602.05707.pdf)  
**作者**：Amir Asiaee, Kaveh Aryan  

**一句话要点**：提出最优收缩重加权方法，在子群比例偏移下修正表示并揭示公平性真实代价

**关键词**：子群比例偏移, 收缩重加权, 公平性评估, 表示修正, 机器学习公平性, 有限样本优化

## 3 点简述
- 核心问题：训练数据子群比例偏移导致公平性与准确性权衡失真
- 方法要点：基于收缩重加权最优修正表示，隔离公平性干预的真实影响
- 实验或效果：在合成和真实数据集验证理论，消除虚假权衡，揭示公平性-效用前沿

## 摘要（原文）

> Machine learning practitioners frequently observe tension between predictive accuracy and group fairness constraints -- yet sometimes fairness interventions appear to improve accuracy. We show that both phenomena can be artifacts of training data that misrepresents subgroup proportions. Under subpopulation shift (stable within-group distributions, shifted group proportions), we establish: (i) full importance-weighted correction is asymptotically unbiased but finite-sample suboptimal; (ii) the optimal finite-sample correction is a shrinkage reweighting that interpolates between target and training mixtures; (iii) apparent "fairness helps accuracy" can arise from comparing fairness methods to an improperly-weighted baseline. We provide an actionable evaluation protocol: fix representation (optimally) before fairness -- compare fairness interventions against a shrinkage-corrected baseline to isolate the true, irreducible price of fairness. Experiments on synthetic and real-world benchmarks (Adult, COMPAS) validate our theoretical predictions and demonstrate that this protocol eliminates spurious tradeoffs, revealing the genuine fairness-utility frontier.

