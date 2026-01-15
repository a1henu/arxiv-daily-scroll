---
layout: default
title: From Prompt to Protocol: Fast Charging Batteries with Large Language Models
---

# From Prompt to Protocol: Fast Charging Batteries with Large Language Models
**arXiv**：[2601.09626v1](https://arxiv.org/abs/2601.09626) · [PDF](https://arxiv.org/pdf/2601.09626.pdf)  
**作者**：Ge Lei, Ferran Brosa Planella, Sterling G. Baird, Samuel J. Cooper  

**一句话要点**：提出基于大语言模型的快速充电协议优化方法，以解决电池充电协议搜索空间受限问题。

**关键词**：电池充电协议优化, 大语言模型应用, 无梯度优化, 快速充电, 协议搜索空间扩展

## 3 点简述
- 核心问题：电池充电协议优化因评估慢、成本高、不可微分而受限，现有方法约束搜索空间，限制协议多样性。
- 方法要点：引入两种无梯度、大语言模型驱动的闭环方法：Prompt-to-Optimizer和Prompt-to-Protocol，扩展协议函数形式。
- 实验或效果：在快速充电场景中，两种方法相比基线提升约4.2%的健康状态，P2P在相同评估预算下实现此效果。

## 摘要（原文）

> Efficiently optimizing battery charging protocols is challenging because each evaluation is slow, costly, and non-differentiable. Many existing approaches address this difficulty by heavily constraining the protocol search space, which limits the diversity of protocols that can be explored, preventing the discovery of higher-performing solutions. We introduce two gradient-free, LLM-driven closed-loop methods: Prompt-to-Optimizer (P2O), which uses an LLM to propose the code for small neural-network-based protocols, which are then trained by an inner loop, and Prompt-to-Protocol (P2P), which simply writes an explicit function for the current and its scalar parameters. Across our case studies, LLM-guided P2O outperforms neural networks designed by Bayesian optimization, evolutionary algorithms, and random search. In a realistic fast charging scenario, both P2O and P2P yield around a 4.2 percent improvement in state of health (capacity retention based health metric under fast charging cycling) over a state-of-the-art multi-step constant current (CC) baseline, with P2P achieving this under matched evaluation budgets (same number of protocol evaluations). These results demonstrate that LLMs can expand the space of protocol functional forms, incorporate language-based constraints, and enable efficient optimization in high cost experimental settings.

