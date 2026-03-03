---
layout: default
title: Chain-of-Context Learning: Dynamic Constraint Understanding for Multi-Task VRPs
---

# Chain-of-Context Learning: Dynamic Constraint Understanding for Multi-Task VRPs
**arXiv**：[2603.01667v1](https://arxiv.org/abs/2603.01667) · [PDF](https://arxiv.org/pdf/2603.01667.pdf)  
**作者**：Shuangchun Gui, Suyu Liu, Xuehe Wang, Zhiguang Cao  

**一句话要点**：提出链式上下文学习框架，通过动态约束理解解决多任务车辆路径问题

**关键词**：多任务车辆路径问题, 链式上下文学习, 强化学习, 动态约束理解, 节点重嵌入

## 3 点简述
- 现有求解器忽略决策过程中的约束和节点动态，导致模型无法准确响应当前上下文。
- CCL框架通过RGCR模块逐步捕获演化上下文，并利用TSNR模块指导节点更新，建模RL代理的演化偏好。
- 在48个VRP变体上评估，CCL在分布内任务全部领先，并在多数分布外任务中表现最佳。

## 摘要（原文）

> Multi-task Vehicle Routing Problems (VRPs) aim to minimize routing costs while satisfying diverse constraints. Existing solvers typically adopt a unified reinforcement learning (RL) framework to learn generalizable patterns across tasks. However, they often overlook the constraint and node dynamics during the decision process, making the model fail to accurately react to the current context. To address this limitation, we propose Chain-of-Context Learning (CCL), a novel framework that progressively captures the evolving context to guide fine-grained node adaptation. Specifically, CCL constructs step-wise contextual information via a Relevance-Guided Context Reformulation (RGCR) module, which adaptively prioritizes salient constraints. This context then guides node updates through a Trajectory-Shared Node Re-embedding (TSNR) module, which aggregates shared node features from all trajectories' contexts and uses them to update inputs for the next step. By modeling evolving preferences of the RL agent, CCL captures step-by-step dependencies in sequential decision-making. We evaluate CCL on 48 diverse VRP variants, including 16 in-distribution and 32 out-of-distribution (with unseen constraints) tasks. Experimental results show that CCL performs favorably against the state-of-the-art baselines, achieving the best performance on all in-distribution tasks and the majority of out-of-distribution tasks.

