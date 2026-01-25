---
layout: default
title: Probably Approximately Correct Maximum A Posteriori Inference
---

# Probably Approximately Correct Maximum A Posteriori Inference
**arXiv**：[2601.16083v1](https://arxiv.org/abs/2601.16083) · [PDF](https://arxiv.org/pdf/2601.16083.pdf)  
**作者**：Matthew Shorvon, Frederik Mallmann-Trenn, David S. Watson  

**一句话要点**：提出PAC-MAP算法，在计算预算下提供概率近似正确的最大后验推断最优解。

**关键词**：最大后验推断, 概率近似正确, 概率电路, 计算复杂度, 信息论度量, 启发式算法

## 3 点简述
- 核心问题：最大后验推断通常难解，即使有结构约束或近似方案。
- 方法要点：基于信息论度量设计PAC算法，利用概率电路高效实现。
- 实验或效果：在多种基准测试中验证方法优势，可增强启发式算法的理论保证。

## 摘要（原文）

> Computing the conditional mode of a distribution, better known as the $\mathit{maximum\ a\ posteriori}$ (MAP) assignment, is a fundamental task in probabilistic inference. However, MAP estimation is generally intractable, and remains hard even under many common structural constraints and approximation schemes. We introduce $\mathit{probably\ approximately\ correct}$ (PAC) algorithms for MAP inference that provide provably optimal solutions under variable and fixed computational budgets. We characterize tractability conditions for PAC-MAP using information theoretic measures that can be estimated from finite samples. Our PAC-MAP solvers are efficiently implemented using probabilistic circuits with appropriate architectures. The randomization strategies we develop can be used either as standalone MAP inference techniques or to improve on popular heuristics, fortifying their solutions with rigorous guarantees. Experiments confirm the benefits of our method in a range of benchmarks.

