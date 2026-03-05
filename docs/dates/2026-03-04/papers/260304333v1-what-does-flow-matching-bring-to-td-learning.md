---
layout: default
title: What Does Flow Matching Bring To TD Learning?
---

# What Does Flow Matching Bring To TD Learning?
**arXiv**：[2603.04333v1](https://arxiv.org/abs/2603.04333) · [PDF](https://arxiv.org/pdf/2603.04333.pdf)  
**作者**：Bhavya Agrawalla, Michal Nauman, Aviral Kumar  

**一句话要点**：提出流匹配方法以提升时序差分学习，通过测试时恢复和塑性特征学习解决高UTD在线强化学习中的塑性丧失问题。

**关键词**：流匹配, 时序差分学习, 强化学习, 塑性丧失, 在线学习, 值函数估计

## 3 点简述
- 核心问题：流匹配在强化学习中有效的原因不明，传统分布强化学习解释不成立。
- 方法要点：使用积分读取值并在积分步骤中密集监督速度场，实现测试时恢复和塑性特征学习。
- 实验或效果：流匹配评论家性能提升2倍，样本效率约5倍，在高UTD在线强化学习中稳定。

## 摘要（原文）

> Recent work shows that flow matching can be effective for scalar Q-value function estimation in reinforcement learning (RL), but it remains unclear why or how this approach differs from standard critics. Contrary to conventional belief, we show that their success is not explained by distributional RL, as explicitly modeling return distributions can reduce performance. Instead, we argue that the use of integration for reading out values and dense velocity supervision at each step of this integration process for training improves TD learning via two mechanisms. First, it enables robust value prediction through \emph{test-time recovery}, whereby iterative computation through integration dampens errors in early value estimates as more integration steps are performed. This recovery mechanism is absent in monolithic critics. Second, supervising the velocity field at multiple interpolant values induces more \emph{plastic} feature learning within the network, allowing critics to represent non-stationary TD targets without discarding previously learned features or overfitting to individual TD targets encountered during training. We formalize these effects and validate them empirically, showing that flow-matching critics substantially outperform monolithic critics (2$\times$ in final performance and around 5$\times$ in sample efficiency) in settings where loss of plasticity poses a challenge e.g., in high-UTD online RL problems, while remaining stable during learning.

