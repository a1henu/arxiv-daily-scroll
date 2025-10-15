---
layout: default
title: HYPE: Hybrid Planning with Ego Proposal-Conditioned Predictions
---

# HYPE: Hybrid Planning with Ego Proposal-Conditioned Predictions
**arXiv**：[2510.12733v1](https://arxiv.org/abs/2510.12733) · [PDF](https://arxiv.org/pdf/2510.12733.pdf)  
**作者**：Hang Yu, Julian Jordan, Julian Schmidt, Silvan Lindner, Alessandro Canevaro, Wilhelm Stork  

**一句话要点**：提出HYPE混合规划器，通过自我提案条件预测解决复杂城市环境中的安全运动规划问题

**关键词**：运动规划, 多智能体交互, 蒙特卡洛树搜索, 自我条件预测, 城市驾驶, 成本函数简化

## 3 点简述
- 核心问题：复杂城市环境中双向多智能体交互的安全运动规划，需估计自我驾驶操作成本
- 方法要点：集成学习提案模型的多模态轨迹到MCTS精炼，使用自我条件占用预测建模交互
- 实验或效果：在nuPlan和DeepUrban基准上实现先进性能，尤其在安全性和适应性方面

## 摘要（原文）

> Safe and interpretable motion planning in complex urban environments needs to
> reason about bidirectional multi-agent interactions. This reasoning requires to
> estimate the costs of potential ego driving maneuvers. Many existing planners
> generate initial trajectories with sampling-based methods and refine them by
> optimizing on learned predictions of future environment states, which requires
> a cost function that encodes the desired vehicle behavior. Designing such a
> cost function can be very challenging, especially if a wide range of complex
> urban scenarios has to be considered. We propose HYPE: HYbrid Planning with Ego
> proposal-conditioned predictions, a planner that integrates multimodal
> trajectory proposals from a learned proposal model as heuristic priors into a
> Monte Carlo Tree Search (MCTS) refinement. To model bidirectional interactions,
> we introduce an ego-conditioned occupancy prediction model, enabling
> consistent, scene-aware reasoning. Our design significantly simplifies cost
> function design in refinement by considering proposal-driven guidance,
> requiring only minimalistic grid-based cost terms. Evaluations on large-scale
> real-world benchmarks nuPlan and DeepUrban show that HYPE effectively achieves
> state-of-the-art performance, especially in safety and adaptability.

