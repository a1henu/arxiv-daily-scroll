---
layout: default
title: Good Allocations from Bad Estimates
---

# Good Allocations from Bad Estimates
**arXiv**：[2601.05597v1](https://arxiv.org/abs/2601.05597) · [PDF](https://arxiv.org/pdf/2601.05597.pdf)  
**作者**：Sílvia Casacuberta, Moritz Hardt  

**一句话要点**：提出基于粗估计的分配方法以减少样本需求，优化异质人群治疗分配

**关键词**：条件平均治疗效应, 治疗分配, 样本复杂度, 异质人群, 随机对照试验

## 3 点简述
- 核心问题：传统CATE估计需大量样本以精确估计治疗效应，但分配目标可能不需要高精度
- 方法要点：利用治疗效应的自然分布，通过粗估计实现近最优分配，样本复杂度从O(M/ε²)降至O(M/ε)
- 实验或效果：在真实RCT数据集上验证，算法能以较少样本找到近最优治疗分配

## 摘要（原文）

> Conditional average treatment effect (CATE) estimation is the de facto gold standard for targeting a treatment to a heterogeneous population. The method estimates treatment effects up to an error $ε> 0$ in each of $M$ different strata of the population, targeting individuals in decreasing order of estimated treatment effect until the budget runs out. In general, this method requires $O(M/ε^2)$ samples. This is best possible if the goal is to estimate all treatment effects up to an $ε$ error. In this work, we show how to achieve the same total treatment effect as CATE with only $O(M/ε)$ samples for natural distributions of treatment effects. The key insight is that coarse estimates suffice for near-optimal treatment allocations. In addition, we show that budget flexibility can further reduce the sample complexity of allocation. Finally, we evaluate our algorithm on various real-world RCT datasets. In all cases, it finds nearly optimal treatment allocations with surprisingly few samples. Our work highlights the fundamental distinction between treatment effect estimation and treatment allocation: the latter requires far fewer samples.

