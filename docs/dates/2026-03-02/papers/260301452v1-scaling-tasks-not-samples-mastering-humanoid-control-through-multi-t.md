---
layout: default
title: Scaling Tasks, Not Samples: Mastering Humanoid Control through Multi-Task Model-Based Reinforcement Learning
---

# Scaling Tasks, Not Samples: Mastering Humanoid Control through Multi-Task Model-Based Reinforcement Learning
**arXiv**：[2603.01452v1](https://arxiv.org/abs/2603.01452) · [PDF](https://arxiv.org/pdf/2603.01452.pdf)  
**作者**：Shaohuai Liu, Weirui Ye, Yilun Du, Le Xie  

**一句话要点**：提出多任务模型强化学习算法EZ-M，以任务数量而非样本数量扩展，提升人形机器人控制的样本效率。

**关键词**：多任务强化学习, 模型强化学习, 人形机器人控制, 样本效率, 在线学习, 任务扩展

## 3 点简述
- 核心问题：机器人学习需主动交互，传统参数或数据扩展方法受限，如何高效在线学习多样技能。
- 方法要点：利用模型强化学习，共享世界模型聚合多任务经验，任务多样性正则化动态学习，避免梯度干扰。
- 实验或效果：在HumanoidBench基准上，EZ-M实现最优性能，样本效率显著高于基线，无需极端参数扩展。

## 摘要（原文）

> Developing generalist robots capable of mastering diverse skills remains a central challenge in embodied AI. While recent progress emphasizes scaling model parameters and offline datasets, such approaches are limited in robotics, where learning requires active interaction. We argue that effective online learning should scale the \emph{number of tasks}, rather than the number of samples per task. This regime reveals a structural advantage of model-based reinforcement learning (MBRL). Because physical dynamics are invariant across tasks, a shared world model can aggregate multi-task experience to learn robust, task-agnostic representations. In contrast, model-free methods suffer from gradient interference when tasks demand conflicting actions in similar states. Task diversity therefore acts as a regularizer for MBRL, improving dynamics learning and sample efficiency. We instantiate this idea with \textbf{EfficientZero-Multitask (EZ-M)}, a sample-efficient multi-task MBRL algorithm for online learning. Evaluated on \textbf{HumanoidBench}, a challenging whole-body control benchmark, EZ-M achieves state-of-the-art performance with significantly higher sample efficiency than strong baselines, without extreme parameter scaling. These results establish task scaling as a critical axis for scalable robotic learning. The project website is available \href{https://yewr.github.io/ez_m/}{here}.

