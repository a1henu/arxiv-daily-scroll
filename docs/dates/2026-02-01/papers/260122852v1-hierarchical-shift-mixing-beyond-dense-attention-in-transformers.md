---
layout: default
title: Hierarchical Shift Mixing -- Beyond Dense Attention in Transformers
---

# Hierarchical Shift Mixing -- Beyond Dense Attention in Transformers
**arXiv**：[2601.22852v1](https://arxiv.org/abs/2601.22852) · [PDF](https://arxiv.org/pdf/2601.22852.pdf)  
**作者**：Robert Forchheimer  

**一句话要点**：提出分层移位混合框架以解决Transformer中注意力层二次复杂度问题

**关键词**：Transformer架构, 令牌混合, 线性复杂度, 注意力机制, 计算效率

## 3 点简述
- 核心问题：Transformer的softmax注意力层计算复杂度高，为二次时间，影响效率
- 方法要点：引入HSM框架，通过分层分布令牌交互实现线性时间复杂度的令牌混合
- 实验或效果：HSM变体性能接近softmax注意力，混合架构可超越基线并降低计算成本

## 摘要（原文）

> Since the introduction of the Transformer architecture for large language models, the softmax-based attention layer has faced increasing scrutinity due to its quadratic-time computational complexity. Attempts have been made to replace it with less complex methods, at the cost of reduced performance in most cases. We introduce Hierarchical Shift Mixing (HSM), a general framework for token mixing that distributes pairwise token interactions across Transformer layers rather than computing them densely within each layer. HSM enables linear-time complexity while remaining agnostic to the specific mixing function. We show that even simple HSM variants achieve performance close to softmax attention, and that hybrid architectures combining HSM with softmax attention can outperform a GPT-style Transformer baseline while reducing computational cost during both training and inference.

