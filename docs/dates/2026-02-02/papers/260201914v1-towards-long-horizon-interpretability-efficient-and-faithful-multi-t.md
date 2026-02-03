---
layout: default
title: Towards Long-Horizon Interpretability: Efficient and Faithful Multi-Token Attribution for Reasoning LLMs
---

# Towards Long-Horizon Interpretability: Efficient and Faithful Multi-Token Attribution for Reasoning LLMs
**arXiv**：[2602.01914v1](https://arxiv.org/abs/2602.01914) · [PDF](https://arxiv.org/pdf/2602.01914.pdf)  
**作者**：Wenbo Pan, Zhichao Liu, Xianlong Wang, Haining Yu, Xiaohua Jia  

**一句话要点**：提出FlashTrace方法以解决长上下文推理LLMs中多令牌归因的效率与忠实性问题

**关键词**：令牌归因, 长上下文推理, 多步推理, 效率优化, 忠实性分析, 递归归因

## 3 点简述
- 现有令牌归因方法在长上下文推理中面临效率瓶颈和忠实性下降问题
- FlashTrace采用跨令牌聚合和递归归因机制，实现高效且忠实的多令牌归因
- 实验显示FlashTrace在长上下文检索和多步推理任务上速度提升超130倍，并保持更高忠实性

## 摘要（原文）

> Token attribution methods provide intuitive explanations for language model outputs by identifying causally important input tokens. However, as modern LLMs increasingly rely on extended reasoning chains, existing schemes face two critical challenges: (1) efficiency bottleneck, where attributing a target span of M tokens within a context of length N requires O(M*N) operations, making long-context attribution prohibitively slow; and (2) faithfulness drop, where intermediate reasoning tokens absorb attribution mass, preventing importance from propagating back to the original input. To address these, we introduce FlashTrace, an efficient multi-token attribution method that employs span-wise aggregation to compute attribution over multi-token targets in a single pass, while maintaining faithfulness. Moreover, we design a recursive attribution mechanism that traces importance through intermediate reasoning chains back to source inputs. Extensive experiments on long-context retrieval (RULER) and multi-step reasoning (MATH, MorehopQA) tasks demonstrate that FlashTrace achieves over 130x speedup over existing baselines while maintaining superior faithfulness. We further analyze the dynamics of recursive attribution, showing that even a single recursive hop improves faithfulness by tracing importance through the reasoning chain.

