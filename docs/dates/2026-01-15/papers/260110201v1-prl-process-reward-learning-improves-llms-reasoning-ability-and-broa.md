---
layout: default
title: PRL: Process Reward Learning Improves LLMs' Reasoning Ability and Broadens the Reasoning Boundary
---

# PRL: Process Reward Learning Improves LLMs' Reasoning Ability and Broadens the Reasoning Boundary
**arXiv**：[2601.10201v1](https://arxiv.org/abs/2601.10201) · [PDF](https://arxiv.org/pdf/2601.10201.pdf)  
**作者**：Jiarui Yao, Ruida Wang, Tong Zhang  

**一句话要点**：提出过程奖励学习以改进大语言模型的推理能力并拓宽推理边界

**关键词**：过程奖励学习, 大语言模型推理, 强化学习优化, 熵正则化, 过程监督

## 3 点简述
- 现有方法依赖轨迹级结果奖励，缺乏推理过程的细粒度监督
- PRL将熵正则化强化学习目标分解为中间步骤，提供理论支持的过程奖励
- 实验显示PRL提升平均性能并改善通过率，验证其有效性和泛化性

## 摘要（原文）

> Improving the reasoning abilities of Large Language Models (LLMs) has been a continuous topic recently. But most relevant works are based on outcome rewards at the trajectory level, missing fine-grained supervision during the reasoning process. Other existing training frameworks that try to combine process signals together to optimize LLMs also rely heavily on tedious additional steps like MCTS, training a separate reward model, etc., doing harm to the training efficiency. Moreover, the intuition behind the process signals design lacks rigorous theoretical support, leaving the understanding of the optimization mechanism opaque. In this paper, we propose Process Reward Learning (PRL), which decomposes the entropy regularized reinforcement learning objective into intermediate steps, with rigorous process rewards that could be assigned to models accordingly. Starting from theoretical motivation, we derive the formulation of PRL that is essentially equivalent to the objective of reward maximization plus a KL-divergence penalty term between the policy model and a reference model. However, PRL could turn the outcome reward into process supervision signals, which helps better guide the exploration during RL optimization. From our experiment results, we demonstrate that PRL not only improves the average performance for LLMs' reasoning ability measured by average @ n, but also broadens the reasoning boundary by improving the pass @ n metric. Extensive experiments show the effectiveness of PRL could be verified and generalized.

