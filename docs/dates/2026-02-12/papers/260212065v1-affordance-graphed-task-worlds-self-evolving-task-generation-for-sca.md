---
layout: default
title: Affordance-Graphed Task Worlds: Self-Evolving Task Generation for Scalable Embodied Learning
---

# Affordance-Graphed Task Worlds: Self-Evolving Task Generation for Scalable Embodied Learning
**arXiv**：[2602.12065v1](https://arxiv.org/abs/2602.12065) · [PDF](https://arxiv.org/pdf/2602.12065.pdf)  
**作者**：Xiang Liu, Sen Cui, Guocai Yao, Zhong Cao, Jingheng Ma, Min Zhang, Changshui Zhang  

**一句话要点**：提出Affordance-Graphed Task Worlds框架，通过结构化任务图和自进化机制解决机器人长时程任务生成与物理不确定性挑战。

**关键词**：机器人学习, 任务生成, 仿真环境, 自进化机制, 结构化图, 物理不确定性

## 3 点简述
- 核心问题：真实世界机器人训练成本高，现有仿真方法难以生成逻辑一致的长时程任务并处理动态物理不确定性。
- 方法要点：基于真实观察构建交互式仿真环境，将任务空间形式化为结构化图，结合视觉语言模型推理和几何验证实现自进化策略优化。
- 实验或效果：实验显示方法在成功率和泛化能力上显著优于基线，实现可扩展机器人学习的自改进循环。

## 摘要（原文）

> Training robotic policies directly in the real world is expensive and unscalable. Although generative simulation enables large-scale data synthesis, current approaches often fail to generate logically coherent long-horizon tasks and struggle with dynamic physical uncertainties due to open-loop execution. To address these challenges, we propose Affordance-Graphed Task Worlds (AGT-World), a unified framework that autonomously constructs interactive simulated environments and corresponding robot task policies based on real-world observations. Unlike methods relying on random proposals or static replication, AGT-World formalizes the task space as a structured graph, enabling the precise, hierarchical decomposition of complex goals into theoretically grounded atomic primitives. Furthermore, we introduce a Self-Evolution mechanism with hybrid feedback to autonomously refine policies, combining Vision-Language Model reasoning and geometric verification. Extensive experiments demonstrate that our method significantly outperforms in success rates and generalization, achieving a self-improving cycle of proposal, execution, and correction for scalable robot learning.

