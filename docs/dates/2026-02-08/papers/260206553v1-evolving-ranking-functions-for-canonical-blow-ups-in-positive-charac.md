---
layout: default
title: Evolving Ranking Functions for Canonical Blow-Ups in Positive Characteristic
---

# Evolving Ranking Functions for Canonical Blow-Ups in Positive Characteristic
**arXiv**：[2602.06553v1](https://arxiv.org/abs/2602.06553) · [PDF](https://arxiv.org/pdf/2602.06553.pdf)  
**作者**：Gergely Bérczi  

**一句话要点**：提出进化搜索候选排序函数以探索正特征奇点消解中的延迟下降准则

**关键词**：正特征奇点消解, 进化搜索, 排序函数, 典范爆破, 延迟下降准则, AlphaEvolve模型

## 3 点简述
- 核心问题：正特征奇点消解中缺乏通用排序函数，Frobenius病理导致经典不变量停滞或增加
- 方法要点：使用AlphaEvolve进化搜索模型，针对4维特征3的玩具典范爆破过程设计候选排序函数
- 实验或效果：获得离散化五分量字典序排序函数，在基准测试中满足零违反的延迟下降准则

## 摘要（原文）

> Resolution of singularities in positive characteristic remains a long-standing open problem in algebraic geometry. In characteristic zero, the problem was solved by Hironaka in 1964, work for which he was awarded the Fields Medal. Modern proofs proceed by constructing suitable ranking functions, that is, invariants shown to strictly decrease along canonical sequences of blow-ups, ensuring termination. In positive characteristic, however, no such general ranking function is known: Frobenius-specific pathologies, such as the kangaroo phenomenon, can cause classical characteristic-zero invariants to plateau or even temporarily increase, presenting a fundamental obstruction to existing approaches. In this paper we report a sequence of experiments using the evolutionary search model AlphaEvolve, designed to discover candidate ranking functions for a toy canonical blow-up process. Our test benchmarks consist of carefully selected hypersurface singularities in dimension $4$ and characteristic $p=3$, with monic purely inseparable leading term, a regime in which naive order-based invariants often fail. After iteratively refining the experimental design, we obtained a discretized five-component lexicographic ranking function satisfying a bounded-delay descent criterion with zero violations across the benchmark. These experiments in turn motivated our main results: the conjectural delayed ranking functions in characteristic $3$ formulated in two conjectures.

