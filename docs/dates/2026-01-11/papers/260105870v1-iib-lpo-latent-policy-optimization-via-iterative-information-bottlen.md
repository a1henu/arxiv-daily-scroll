---
layout: default
title: IIB-LPO: Latent Policy Optimization via Iterative Information Bottleneck
---

# IIB-LPO: Latent Policy Optimization via Iterative Information Bottleneck
**arXiv**：[2601.05870v1](https://arxiv.org/abs/2601.05870) · [PDF](https://arxiv.org/pdf/2601.05870.pdf)  
**作者**：Huilin Deng, Hongchen Luo, Yue Zhu, Long Li, Zhuoyue Chen, Xinghao Zhao, Ming Li, Jihai Zhang, Mengchang Wang, Yang Cao, Yu Kang  

**一句话要点**：提出IIB-LPO方法以解决强化学习中探索崩溃问题，通过迭代信息瓶颈优化潜在策略。

**关键词**：强化学习, 信息瓶颈, 探索策略, 推理轨迹, 数学推理, 潜在策略优化

## 3 点简述
- 核心问题：强化学习在可验证奖励场景中面临探索崩溃，随机rollout语义同质化导致行为过优化。
- 方法要点：利用迭代信息瓶颈，从统计扰动转向推理轨迹拓扑分支，触发高熵状态潜在分支以多样化路径。
- 实验或效果：在四个数学推理基准测试中实现最优性能，准确率提升达5.3%，多样性指标提升达7.4%。

## 摘要（原文）

> Recent advances in Reinforcement Learning with Verifiable Rewards (RLVR) for Large Language Model (LLM) reasoning have been hindered by a persistent challenge: exploration collapse. The semantic homogeneity of random rollouts often traps models in narrow, over-optimized behaviors. While existing methods leverage policy entropy to encourage exploration, they face inherent limitations. Global entropy regularization is susceptible to reward hacking, which can induce meaningless verbosity, whereas local token-selective updates struggle with the strong inductive bias of pre-trained models. To address this, we propose Latent Policy Optimization via Iterative Information Bottleneck (IIB-LPO), a novel approach that shifts exploration from statistical perturbation of token distributions to topological branching of reasoning trajectories. IIB-LPO triggers latent branching at high-entropy states to diversify reasoning paths and employs the Information Bottleneck principle both as a trajectory filter and a self-reward mechanism, ensuring concise and informative exploration. Empirical results across four mathematical reasoning benchmarks demonstrate that IIB-LPO achieves state-of-the-art performance, surpassing prior methods by margins of up to 5.3% in accuracy and 7.4% in diversity metrics.

