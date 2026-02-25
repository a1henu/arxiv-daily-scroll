---
layout: default
title: MAST: A Multi-fidelity Augmented Surrogate model via Spatial Trust-weighting
---

# MAST: A Multi-fidelity Augmented Surrogate model via Spatial Trust-weighting
**arXiv**：[2602.20974v1](https://arxiv.org/abs/2602.20974) · [PDF](https://arxiv.org/pdf/2602.20974.pdf)  
**作者**：Ahmed Mohamed Eisa Nasr, Haris Moazam Sheikh  

**一句话要点**：提出MAST方法以解决多保真度代理建模中训练成本高和全局相关性假设失效的问题。

**关键词**：多保真度代理建模, 高斯过程, 异方差建模, 空间信任加权, 工程优化, 计算成本降低

## 3 点简述
- 核心问题：现有方法训练成本高，且依赖全局相关性假设，难以捕捉输入空间中保真度关系的局部变化。
- 方法要点：通过显式差异建模和基于距离的加权，结合校正低保真度观测和高保真度预测，构建单一异方差高斯过程。
- 实验或效果：在合成基准测试中，MAST优于当前最先进技术，并在不同总预算和保真度差距下保持稳健性能。

## 摘要（原文）

> In engineering design and scientific computing, computational cost and predictive accuracy are intrinsically coupled. High-fidelity simulations provide accurate predictions but at substantial computational costs, while lower-fidelity approximations offer efficiency at the expense of accuracy. Multi-fidelity surrogate modelling addresses this trade-off by combining abundant low-fidelity data with sparse high-fidelity observations. However, existing methods suffer from expensive training cost or rely on global correlation assumptions that often fail in practice to capture how fidelity relationships vary across the input space, leading to poor performance particularly under tight budget constraints. We introduce MAST, a method that blends corrected low-fidelity observations with high-fidelity predictions, trusting high-fidelity near observed samples and relying on corrected low-fidelity elsewhere. MAST achieves this through explicit discrepancy modelling and distance-based weighting with closed-form variance propagation, producing a single heteroscedastic Gaussian process. Across multi-fidelity synthetic benchmarks, MAST shows a marked improvement over the current state-of-the-art techniques. Crucially, MAST maintains robust performance across varying total budget and fidelity gaps, conditions under which competing methods exhibit significant degradation or unstable behaviour.

