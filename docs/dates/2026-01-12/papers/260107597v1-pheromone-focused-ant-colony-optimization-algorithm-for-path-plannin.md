---
layout: default
title: Pheromone-Focused Ant Colony Optimization algorithm for path planning
---

# Pheromone-Focused Ant Colony Optimization algorithm for path planning
**arXiv**：[2601.07597v1](https://arxiv.org/abs/2601.07597) · [PDF](https://arxiv.org/pdf/2601.07597.pdf)  
**作者**：Yi Liu, Hongda Zhang, Zhongxue Gan, Yuning Chen, Ziqing Zhou, Chunlei Meng, Chun Ouyang  

**一句话要点**：提出信息素聚焦蚁群优化算法以解决路径规划中搜索盲目和收敛慢的问题

**关键词**：蚁群优化, 路径规划, 信息素聚焦, 收敛加速, 全局优化

## 3 点简述
- 传统蚁群优化在复杂环境中存在搜索盲目和收敛慢的缺点
- PFACO通过初始信息素聚焦、优质路径强化和前瞻惩罚冗余转弯来增强优化能力
- 实验表明PFACO在收敛速度和解决方案质量上优于对比算法

## 摘要（原文）

> Ant Colony Optimization (ACO) is a prominent swarm intelligence algorithm extensively applied to path planning. However, traditional ACO methods often exhibit shortcomings, such as blind search behavior and slow convergence within complex environments. To address these challenges, this paper proposes the Pheromone-Focused Ant Colony Optimization (PFACO) algorithm, which introduces three key strategies to enhance the problem-solving ability of the ant colony. First, the initial pheromone distribution is concentrated in more promising regions based on the Euclidean distances of nodes to the start and end points, balancing the trade-off between exploration and exploitation. Second, promising solutions are reinforced during colony iterations to intensify pheromone deposition along high-quality paths, accelerating convergence while maintaining solution diversity. Third, a forward-looking mechanism is implemented to penalize redundant path turns, promoting smoother and more efficient solutions. These strategies collectively produce the focused pheromones to guide the ant colony's search, which enhances the global optimization capabilities of the PFACO algorithm, significantly improving convergence speed and solution quality across diverse optimization problems. The experimental results demonstrate that PFACO consistently outperforms comparative ACO algorithms in terms of convergence speed and solution quality.

