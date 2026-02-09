---
layout: default
title: Pairwise is Not Enough: Hypergraph Neural Networks for Multi-Agent Pathfinding
---

# Pairwise is Not Enough: Hypergraph Neural Networks for Multi-Agent Pathfinding
**arXiv**：[2602.06733v1](https://arxiv.org/abs/2602.06733) · [PDF](https://arxiv.org/pdf/2602.06733.pdf)  
**作者**：Rishabh Jain, Keisuke Okumura, Michael Amir, Pietro Lio, Amanda Prorok  

**一句话要点**：提出HMAGAT超图神经网络以解决多智能体路径规划中的高阶交互问题

**关键词**：多智能体路径规划, 超图神经网络, 注意力机制, 高阶交互, 学习型求解器

## 3 点简述
- 多智能体路径规划中，传统图神经网络受限于成对消息传递，导致注意力稀释和次优行为
- HMAGAT利用有向超图的注意力机制，显式捕获群体动态，提升协调能力
- 实验显示，HMAGAT以更少参数和数据超越现有方法，验证超图表示的有效性

## 摘要（原文）

> Multi-Agent Path Finding (MAPF) is a representative multi-agent coordination problem, where multiple agents are required to navigate to their respective goals without collisions. Solving MAPF optimally is known to be NP-hard, leading to the adoption of learning-based approaches to alleviate the online computational burden. Prevailing approaches, such as Graph Neural Networks (GNNs), are typically constrained to pairwise message passing between agents. However, this limitation leads to suboptimal behaviours and critical issues, such as attention dilution, particularly in dense environments where group (i.e. beyond just two agents) coordination is most critical. Despite the importance of such higher-order interactions, existing approaches have not been able to fully explore them. To address this representational bottleneck, we introduce HMAGAT (Hypergraph Multi-Agent Attention Network), a novel architecture that leverages attentional mechanisms over directed hypergraphs to explicitly capture group dynamics. Empirically, HMAGAT establishes a new state-of-the-art among learning-based MAPF solvers: e.g., despite having just 1M parameters and being trained on 100$\times$ less data, it outperforms the current SoTA 85M parameter model. Through detailed analysis of HMAGAT's attention values, we demonstrate how hypergraph representations mitigate the attention dilution inherent in GNNs and capture complex interactions where pairwise methods fail. Our results illustrate that appropriate inductive biases are often more critical than the training data size or sheer parameter count for multi-agent problems.

