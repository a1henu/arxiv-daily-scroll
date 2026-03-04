---
layout: default
title: Learning Memory-Enhanced Improvement Heuristics for Flexible Job Shop Scheduling
---

# Learning Memory-Enhanced Improvement Heuristics for Flexible Job Shop Scheduling
**arXiv**：[2603.02846v1](https://arxiv.org/abs/2603.02846) · [PDF](https://arxiv.org/pdf/2603.02846.pdf)  
**作者**：Jiaqi Wang, Zhiguang Cao, Peng Zhao, Rui Cao, Yubin Xiao, Yuan Jiang, You Zhou  

**一句话要点**：提出MIStar框架以解决柔性作业车间调度问题，通过记忆增强图表示提升改进启发式性能

**关键词**：柔性作业车间调度, 改进启发式方法, 异构图表示, 记忆增强图神经网络, 深度强化学习, 并行搜索策略

## 3 点简述
- 针对柔性作业车间调度问题，现有深度强化学习方法多为构造式，难以达到近优解；改进式方法更有效但面临状态表示和策略学习挑战
- 提出MIStar框架，采用异构析取图精确建模调度解，设计记忆增强图神经网络提取特征，结合并行贪婪搜索策略
- 在合成数据和公开基准测试中，MIStar显著优于传统启发式和先进构造式方法，实现更优解和更少迭代

## 摘要（原文）

> The rise of smart manufacturing under Industry 4.0 introduces mass customization and dynamic production, demanding more advanced and flexible scheduling techniques. The flexible job-shop scheduling problem (FJSP) has attracted significant attention due to its complex constraints and strong alignment with real-world production scenarios. Current deep reinforcement learning (DRL)-based approaches to FJSP predominantly employ constructive methods. While effective, they often fall short of reaching (near-)optimal solutions. In contrast, improvement-based methods iteratively explore the neighborhood of initial solutions and are more effective in approaching optimality. However, the flexible machine allocation in FJSP poses significant challenges to the application of this framework, including accurate state representation, effective policy learning, and efficient search strategies. To address these challenges, this paper proposes a Memory-enhanced Improvement Search framework with heterogeneous graph representation--MIStar. It employs a novel heterogeneous disjunctive graph that explicitly models the operation sequences on machines to accurately represent scheduling solutions. Moreover, a memoryenhanced heterogeneous graph neural network (MHGNN) is designed for feature extraction, leveraging historical trajectories to enhance the decision-making capability of the policy network. Finally, a parallel greedy search strategy is adopted to explore the solution space, enabling superior solutions with fewer iterations. Extensive experiments on synthetic data and public benchmarks demonstrate that MIStar significantly outperforms both traditional handcrafted improvement heuristics and state-of-the-art DRL-based constructive methods.

