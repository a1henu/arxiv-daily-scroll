---
layout: default
title: Flexible Manufacturing Systems Intralogistics: Dynamic Optimization of AGVs and Tool Sharing Using Coloured-Timed Petri Nets and Actor-Critic RL with Actions Masking
---

# Flexible Manufacturing Systems Intralogistics: Dynamic Optimization of AGVs and Tool Sharing Using Coloured-Timed Petri Nets and Actor-Critic RL with Actions Masking
**arXiv**：[2601.04887v1](https://arxiv.org/abs/2601.04887) · [PDF](https://arxiv.org/pdf/2601.04887.pdf)  
**作者**：Sofiene Lassoued, Laxmikant Shrikant Bahetic, Nathalie Weiß-Borkowskib, Stefan Lierc, Andreas Schwunga  

**一句话要点**：提出结合着色时间Petri网与演员-评论家强化学习的方法，以优化柔性制造系统中AGV和工具共享的动态调度。

**关键词**：柔性制造系统, AGV调度, 工具共享, 着色时间Petri网, 演员-评论家强化学习, 动态优化

## 3 点简述
- 核心问题：扩展传统作业车间调度，整合AGV和工具共享系统，处理柔性制造系统的复杂动态优化。
- 方法要点：使用着色时间Petri网建模和动作掩码减少搜索空间，结合演员-评论家模型强化学习提升适应性，并采用前瞻策略优化AGV定位。
- 实验或效果：在小型和大型基准测试中，匹配或超越传统方法，缩短完工时间并显著减少计算时间，提供可复现环境和消融分析。

## 摘要（原文）

> Flexible Manufacturing Systems (FMS) are pivotal in optimizing production processes in today's rapidly evolving manufacturing landscape. This paper advances the traditional job shop scheduling problem by incorporating additional complexities through the simultaneous integration of automated guided vehicles (AGVs) and tool-sharing systems. We propose a novel approach that combines Colored-Timed Petri Nets (CTPNs) with actor-critic model-based reinforcement learning (MBRL), effectively addressing the multifaceted challenges associated with FMS. CTPNs provide a formal modeling structure and dynamic action masking, significantly reducing the action search space, while MBRL ensures adaptability to changing environments through the learned policy. Leveraging the advantages of MBRL, we incorporate a lookahead strategy for optimal positioning of AGVs, improving operational efficiency. Our approach was evaluated on small-sized public benchmarks and a newly developed large-scale benchmark inspired by the Taillard benchmark. The results show that our approach matches traditional methods on smaller instances and outperforms them on larger ones in terms of makespan while achieving a tenfold reduction in computation time. To ensure reproducibility, we propose a gym-compatible environment and an instance generator. Additionally, an ablation study evaluates the contribution of each framework component to its overall performance.

