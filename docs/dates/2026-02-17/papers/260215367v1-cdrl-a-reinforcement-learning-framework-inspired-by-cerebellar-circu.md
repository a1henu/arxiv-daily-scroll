---
layout: default
title: CDRL: A Reinforcement Learning Framework Inspired by Cerebellar Circuits and Dendritic Computational Strategies
---

# CDRL: A Reinforcement Learning Framework Inspired by Cerebellar Circuits and Dendritic Computational Strategies
**arXiv**：[2602.15367v1](https://arxiv.org/abs/2602.15367) · [PDF](https://arxiv.org/pdf/2602.15367.pdf)  
**作者**：Sibo Zhang, Rui Jing, Liangfu Lv, Jian Zhang, Yunliang Zang  

**一句话要点**：提出受小脑结构和树突计算启发的强化学习框架，以提升样本效率、鲁棒性和泛化能力。

**关键词**：强化学习, 小脑启发架构, 树突计算, 样本效率, 鲁棒性, 泛化能力

## 3 点简述
- 强化学习在样本效率低、噪声敏感和部分可观测下泛化弱的问题。
- 基于小脑结构原理，引入大规模扩展、稀疏连接、稀疏激活和树突级调制。
- 实验显示该架构在噪声高维基准上优于传统设计，参数分析表明其优化性能。

## 摘要（原文）

> Reinforcement learning (RL) has achieved notable performance in high-dimensional sequential decision-making tasks, yet remains limited by low sample efficiency, sensitivity to noise, and weak generalization under partial observability. Most existing approaches address these issues primarily through optimization strategies, while the role of architectural priors in shaping representation learning and decision dynamics is less explored. Inspired by structural principles of the cerebellum, we propose a biologically grounded RL architecture that incorporate large expansion, sparse connectivity, sparse activation, and dendritic-level modulation. Experiments on noisy, high-dimensional RL benchmarks show that both the cerebellar architecture and dendritic modulation consistently improve sample efficiency, robustness, and generalization compared to conventional designs. Sensitivity analysis of architectural parameters suggests that cerebellum-inspired structures can offer optimized performance for RL with constrained model parameters. Overall, our work underscores the value of cerebellar structural priors as effective inductive biases for RL.

