---
layout: default
title: Admissibility Alignment
---

# Admissibility Alignment
**arXiv**：[2601.01816v1](https://arxiv.org/abs/2601.01816) · [PDF](https://arxiv.org/pdf/2601.01816.pdf)  
**作者**：Chris Duffey  

**一句话要点**：提出可容许对齐框架，通过蒙特卡洛策略评估在不确定性下实现AI决策对齐。

**关键词**：AI对齐, 不确定性决策, 蒙特卡洛估计, 策略评估, 分布对齐, 可容许控制

## 3 点简述
- 核心问题：将AI对齐重新定义为不确定性下基于结果分布的可容许行动与决策选择属性。
- 方法要点：引入MAP-AI架构，通过蒙特卡洛估计和可容许控制策略选择，评估策略在分布上的对齐性。
- 实验或效果：提供可执行方法，评估企业AI系统的信任与对齐，支持不修改模型下的策略行为调整。

## 摘要（原文）

> This paper introduces Admissibility Alignment: a reframing of AI alignment as a property of admissible action and decision selection over distributions of outcomes under uncertainty, evaluated through the behavior of candidate policies. We present MAP-AI (Monte Carlo Alignment for Policy) as a canonical system architecture for operationalizing admissibility alignment, formalizing alignment as a probabilistic, decision-theoretic property rather than a static or binary condition.
>   MAP-AI, a new control-plane system architecture for aligned decision-making under uncertainty, enforces alignment through Monte Carlo estimation of outcome distributions and admissibility-controlled policy selection rather than static model-level constraints. The framework evaluates decision policies across ensembles of plausible futures, explicitly modeling uncertainty, intervention effects, value ambiguity, and governance constraints. Alignment is assessed through distributional properties including expected utility, variance, tail risk, and probability of misalignment rather than accuracy or ranking performance. This approach distinguishes probabilistic prediction from decision reasoning under uncertainty and provides an executable methodology for evaluating trust and alignment in enterprise and institutional AI systems. The result is a practical foundation for governing AI systems whose impact is determined not by individual forecasts, but by policy behavior across distributions and tail events. Finally, we show how distributional alignment evaluation can be integrated into decision-making itself, yielding an admissibility-controlled action selection mechanism that alters policy behavior under uncertainty without retraining or modifying underlying models.

