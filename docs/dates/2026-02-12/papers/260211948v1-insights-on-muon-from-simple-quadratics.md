---
layout: default
title: Insights on Muon from Simple Quadratics
---

# Insights on Muon from Simple Quadratics
**arXiv**：[2602.11948v1](https://arxiv.org/abs/2602.11948) · [PDF](https://arxiv.org/pdf/2602.11948.pdf)  
**作者**：Antoine Gonon, Andreea-Alexandra Muşat, Nicolas Boumal  

**一句话要点**：分析Muon优化器在简单二次函数上的动态，揭示极因子近似误差和结构性质的影响。

**关键词**：Muon优化器, 极因子近似, 离散时间动态, 有限时间性能, 结构性质, 二次函数分析

## 3 点简述
- 核心问题：现有理论对Muon性能的解释不足，尤其在简单强凸函数上。
- 方法要点：通过分析极因子近似误差如何改变离散时间动态，提升可达性和有限时间性能。
- 实验或效果：指出结构性质影响有限预算常数，超越基于条件数的解释。

## 摘要（原文）

> Muon updates weight matrices along (approximate) polar factors of the gradients and has shown strong empirical performance in large-scale training. Existing attempts at explaining its performance largely focus on single-step comparisons (on quadratic proxies) and worst-case guarantees that treat the inexactness of the polar-factor as a nuisance ``to be argued away''. We show that already on simple strongly convex functions such as $L(W)=\frac12\\|W\\|_{\text{F}}^2$, these perspectives are insufficient, suggesting that understanding Muon requires going beyond local proxies and pessimistic worst-case bounds. Instead, our analysis exposes two observations that already affect behavior on simple quadratics and are not well captured by prevailing abstractions: (i) approximation error in the polar step can qualitatively alter discrete-time dynamics and improve reachability and finite-time performance -- an effect practitioners exploit to tune Muon, but that existing theory largely treats as a pure accuracy compromise; and (ii) structural properties of the objective affect finite-budget constants beyond the prevailing conditioning-based explanations. Thus, any general theory covering these cases must either incorporate these ingredients explicitly or explain why they are irrelevant in the regimes of interest.

