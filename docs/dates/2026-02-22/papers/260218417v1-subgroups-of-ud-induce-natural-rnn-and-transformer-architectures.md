---
layout: default
title: Subgroups of $U(d)$ Induce Natural RNN and Transformer Architectures
---

# Subgroups of $U(d)$ Induce Natural RNN and Transformer Architectures
**arXiv**：[2602.18417v1](https://arxiv.org/abs/2602.18417) · [PDF](https://arxiv.org/pdf/2602.18417.pdf)  
**作者**：Joshua Nunley  

**一句话要点**：提出基于U(d)闭子群的序列模型框架，推导RNN和Transformer架构并实验验证正交状态模型。

**关键词**：序列模型, 群论框架, 正交状态, RNN架构, Transformer架构, 切空间扩展

## 3 点简述
- 核心问题：序列模型中隐藏状态的设计缺乏统一框架，需结合群论结构。
- 方法要点：基于U(d)闭子群构建通用骨架，通过子群选择替换状态空间、切空间投影和更新映射。
- 实验或效果：在O(d)子群上评估正交状态RNN和Transformer，参数匹配下测试Tiny Shakespeare和Penn Treebank。

## 摘要（原文）

> This paper presents a direct framework for sequence models with hidden states on closed subgroups of U(d). We use a minimal axiomatic setup and derive recurrent and transformer templates from a shared skeleton in which subgroup choice acts as a drop-in replacement for state space, tangent projection, and update map. We then specialize to O(d) and evaluate orthogonal-state RNN and transformer models on Tiny Shakespeare and Penn Treebank under parameter-matched settings. We also report a general linear-mixing extension in tangent space, which applies across subgroup choices and improves finite-budget performance in the current O(d) experiments.

