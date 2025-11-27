---
layout: default
title: BAMAS: Structuring Budget-Aware Multi-Agent Systems
---

# BAMAS: Structuring Budget-Aware Multi-Agent Systems
**arXiv**：[2511.21572v1](https://arxiv.org/abs/2511.21572) · [PDF](https://arxiv.org/pdf/2511.21572.pdf)  
**作者**：Liming Yang, Junyu Luo, Xuanzhe Liu, Yiling Lou, Zhenpeng Chen  

**一句话要点**：提出BAMAS以在预算约束下构建多智能体系统

**关键词**：多智能体系统, 预算约束, 整数线性规划, 强化学习, 成本优化

## 3 点简述
- 核心问题：现有多智能体系统在复杂任务中缺乏对预算约束的考虑
- 方法要点：通过整数线性规划选择LLM，强化学习确定交互拓扑
- 实验或效果：在三个任务中性能相当，成本降低高达86%

## 摘要（原文）

> Large language model (LLM)-based multi-agent systems have emerged as a powerful paradigm for enabling autonomous agents to solve complex tasks. As these systems scale in complexity, cost becomes an important consideration for practical deployment. However, existing work rarely addresses how to structure multi-agent systems under explicit budget constraints. In this paper, we propose BAMAS, a novel approach for building multi-agent systems with budget awareness. BAMAS first selects an optimal set of LLMs by formulating and solving an Integer Linear Programming problem that balances performance and cost. It then determines how these LLMs should collaborate by leveraging a reinforcement learning-based method to select the interaction topology. Finally, the system is instantiated and executed based on the selected agents and their collaboration topology. We evaluate BAMAS on three representative tasks and compare it with state-of-the-art agent construction methods. Results show that BAMAS achieves comparable performance while reducing cost by up to 86%.

