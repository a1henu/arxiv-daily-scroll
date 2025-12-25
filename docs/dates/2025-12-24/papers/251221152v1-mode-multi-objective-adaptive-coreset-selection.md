---
layout: default
title: MODE: Multi-Objective Adaptive Coreset Selection
---

# MODE: Multi-Objective Adaptive Coreset Selection
**arXiv**：[2512.21152v1](https://arxiv.org/abs/2512.21152) · [PDF](https://arxiv.org/pdf/2512.21152.pdf)  
**作者**：Tanmoy Mukherjee, Pierre Marquis, Zied Bouraoui  

**一句话要点**：提出MODE框架以动态组合核心集选择策略，提升数据效率与模型性能。

**关键词**：核心集选择, 数据效率, 自适应学习, 多目标优化, 模型训练优化

## 3 点简述
- 核心问题：静态核心集选择方法无法适应训练阶段变化，影响数据利用效率。
- 方法要点：MODE根据训练阶段动态调整选择标准，早期强调类别平衡，中期关注多样性，后期聚焦不确定性。
- 实验或效果：MODE在降低内存需求的同时，保持竞争性准确率，并提供数据效用演化的可解释性洞察。

## 摘要（原文）

> We present Mode(Multi-Objective adaptive Data Efficiency), a framework that dynamically combines coreset selection strategies based on their evolving contribution to model performance. Unlike static methods, \mode adapts selection criteria to training phases: emphasizing class balance early, diversity during representation learning, and uncertainty at convergence. We show that MODE achieves (1-1/e)-approximation with O(n \log n) complexity and demonstrates competitive accuracy while providing interpretable insights into data utility evolution. Experiments show \mode reduces memory requirements

