---
layout: default
title: Improved Convergence Rates of Muon Optimizer for Nonconvex Optimization
---

# Improved Convergence Rates of Muon Optimizer for Nonconvex Optimization
**arXiv**：[2601.19400v1](https://arxiv.org/abs/2601.19400) · [PDF](https://arxiv.org/pdf/2601.19400.pdf)  
**作者**：Shuntaro Nagashima, Hideaki Iiduka  

**一句话要点**：提出简化分析以改进Muon优化器在非凸优化中的收敛率理论保证

**关键词**：非凸优化, Muon优化器, 收敛率分析, 正交化一阶方法, 理论保证

## 3 点简述
- 核心问题：现有Muon优化器收敛理论在非凸优化中较粗糙或依赖限制性假设
- 方法要点：通过直接简化分析，避免对更新规则的严格假设，建立更尖锐的收敛保证
- 实验或效果：改进现有边界，实现更快收敛率，覆盖更广泛问题设置

## 摘要（原文）

> The Muon optimizer has recently attracted attention due to its orthogonalized first-order updates, and a deeper theoretical understanding of its convergence behavior is essential for guiding practical applications; however, existing convergence guarantees are either coarse or obtained under restrictive analytical settings. In this work, we establish sharper convergence guarantees for the Muon optimizer through a direct and simplified analysis that does not rely on restrictive assumptions on the update rule. Our results improve upon existing bounds by achieving faster convergence rates while covering a broader class of problem settings. These findings provide a more accurate theoretical characterization of Muon and offer insights applicable to a broader class of orthogonalized first-order methods.

