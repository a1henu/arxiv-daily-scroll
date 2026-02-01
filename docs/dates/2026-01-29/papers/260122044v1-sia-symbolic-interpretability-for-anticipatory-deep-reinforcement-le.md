---
layout: default
title: SIA: Symbolic Interpretability for Anticipatory Deep Reinforcement Learning in Network Control
---

# SIA: Symbolic Interpretability for Anticipatory Deep Reinforcement Learning in Network Control
**arXiv**：[2601.22044v1](https://arxiv.org/abs/2601.22044) · [PDF](https://arxiv.org/pdf/2601.22044.pdf)  
**作者**：MohammadErfan Jabbari, Abhishek Duttagupta, Claudio Fiandrino, Leonardo Bonati, Salvatore D'Oro, Michele Polese, Marco Fiore, Tommaso Melodia  

**一句话要点**：提出SIA解释器以解决预测增强深度强化学习在网络控制中的黑盒问题

**关键词**：深度强化学习, 网络控制, 可解释人工智能, 预测增强, 符号AI, 知识图谱

## 3 点简述
- 核心问题：预测增强DRL在网络控制中因黑盒特性难以验证预测是否指导决策，阻碍应用。
- 方法要点：SIA融合符号AI抽象和知识图谱实时解释代理操作，引入影响分数指标，速度超现有方法200倍。
- 实验或效果：在三个网络用例中揭示隐藏问题，通过针对性修复提升视频流平均比特率9%和RAN切片奖励25%。

## 摘要（原文）

> Deep reinforcement learning (DRL) promises adaptive control for future mobile networks but conventional agents remain reactive: they act on past and current measurements and cannot leverage short-term forecasts of exogenous KPIs such as bandwidth. Augmenting agents with predictions can overcome this temporal myopia, yet uptake in networking is scarce because forecast-aware agents act as closed-boxes; operators cannot tell whether predictions guide decisions or justify the added complexity. We propose SIA, the first interpreter that exposes in real time how forecast-augmented DRL agents operate. SIA fuses Symbolic AI abstractions with per-KPI Knowledge Graphs to produce explanations, and includes a new Influence Score metric. SIA achieves sub-millisecond speed, over 200x faster than existing XAI methods. We evaluate SIA on three diverse networking use cases, uncovering hidden issues, including temporal misalignment in forecast integration and reward-design biases that trigger counter-productive policies. These insights enable targeted fixes: a redesigned agent achieves a 9% higher average bitrate in video streaming, and SIA's online Action-Refinement module improves RAN-slicing reward by 25% without retraining. By making anticipatory DRL transparent and tunable, SIA lowers the barrier to proactive control in next-generation mobile networks.

