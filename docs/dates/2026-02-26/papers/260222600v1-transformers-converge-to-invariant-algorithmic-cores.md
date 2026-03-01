---
layout: default
title: Transformers converge to invariant algorithmic cores
---

# Transformers converge to invariant algorithmic cores
**arXiv**：[2602.22600v1](https://arxiv.org/abs/2602.22600) · [PDF](https://arxiv.org/pdf/2602.22600.pdf)  
**作者**：Joshua S. Schiffman  

**一句话要点**：提出算法核心概念以揭示Transformer跨训练和规模的内部计算不变性

**关键词**：Transformer模型, 算法核心, 机制可解释性, 训练不变性, 低维结构, 计算本质

## 3 点简述
- 核心问题：训练选择行为而非电路，导致权重配置多样，难以识别反映计算的内在结构
- 方法要点：提取算法核心作为紧凑子空间，独立训练的Transformer收敛到相同核心
- 实验或效果：在Markov链、模加法和GPT-2中验证核心不变性，如模加法在顿悟时发现循环算子

## 摘要（原文）

> Large language models exhibit sophisticated capabilities, yet understanding how they work internally remains a central challenge. A fundamental obstacle is that training selects for behavior, not circuitry, so many weight configurations can implement the same function. Which internal structures reflect the computation, and which are accidents of a particular training run? This work extracts algorithmic cores: compact subspaces necessary and sufficient for task performance. Independently trained transformers learn different weights but converge to the same cores. Markov-chain transformers embed 3D cores in nearly orthogonal subspaces yet recover identical transition spectra. Modular-addition transformers discover compact cyclic operators at grokking that later inflate, yielding a predictive model of the memorization-to-generalization transition. GPT-2 language models govern subject-verb agreement through a single axis that, when flipped, inverts grammatical number throughout generation across scales. These results reveal low-dimensional invariants that persist across training runs and scales, suggesting that transformer computations are organized around compact, shared algorithmic structures. Mechanistic interpretability could benefit from targeting such invariants -- the computational essence -- rather than implementation-specific details.

