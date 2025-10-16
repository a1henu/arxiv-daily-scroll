---
layout: default
title: The Mechanistic Emergence of Symbol Grounding in Language Models
---

# The Mechanistic Emergence of Symbol Grounding in Language Models
**arXiv**：[2510.13796v1](https://arxiv.org/abs/2510.13796) · [PDF](https://arxiv.org/pdf/2510.13796.pdf)  
**作者**：Shuyu Wu, Ziqiao Ma, Xiaoxi Luo, Yidong Huang, Josue Torres-Fonseca, Freda Shi, Joyce Chai  

**一句话要点**：提出受控评估框架以揭示语言模型中符号接地的涌现机制

**关键词**：符号接地, 语言模型, 机制分析, 注意力机制, 多模态对话, Transformer模型

## 3 点简述
- 核心问题：符号接地在语言模型中的具体涌现位置和机制未知
- 方法要点：通过机制性和因果分析追踪内部计算过程
- 实验或效果：接地集中于中间层，通过注意力头聚合环境信息实现

## 摘要（原文）

> Symbol grounding (Harnad, 1990) describes how symbols such as words acquire
> their meanings by connecting to real-world sensorimotor experiences. Recent
> work has shown preliminary evidence that grounding may emerge in
> (vision-)language models trained at scale without using explicit grounding
> objectives. Yet, the specific loci of this emergence and the mechanisms that
> drive it remain largely unexplored. To address this problem, we introduce a
> controlled evaluation framework that systematically traces how symbol grounding
> arises within the internal computations through mechanistic and causal
> analysis. Our findings show that grounding concentrates in middle-layer
> computations and is implemented through the aggregate mechanism, where
> attention heads aggregate the environmental ground to support the prediction of
> linguistic forms. This phenomenon replicates in multimodal dialogue and across
> architectures (Transformers and state-space models), but not in unidirectional
> LSTMs. Our results provide behavioral and mechanistic evidence that symbol
> grounding can emerge in language models, with practical implications for
> predicting and potentially controlling the reliability of generation.

