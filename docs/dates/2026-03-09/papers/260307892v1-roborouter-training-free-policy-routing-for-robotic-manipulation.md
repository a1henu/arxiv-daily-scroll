---
layout: default
title: RoboRouter: Training-Free Policy Routing for Robotic Manipulation
---

# RoboRouter: Training-Free Policy Routing for Robotic Manipulation
**arXiv**：[2603.07892v1](https://arxiv.org/abs/2603.07892) · [PDF](https://arxiv.org/pdf/2603.07892.pdf)  
**作者**：Yiteng Chen, Zhe Cao, Hongjia Ren, Chenjie Yang, Wenbo Li, Shiyi Wang, Yemin Wang, Li Zhang, Yanming Shao, Zhenjun Zhao, Huiping Zhuang, Qingyao Wu  

**一句话要点**：提出RoboRouter框架，通过无训练策略路由提升机器人操作性能

**关键词**：机器人操作, 策略路由, 无训练框架, 异构策略, 语义任务表示, 性能提升

## 3 点简述
- 核心问题：现有机器人操作策略泛化能力有限，难以适应多样化任务
- 方法要点：基于语义任务表示和历史经验，智能选择异构策略池中的最优策略
- 实验或效果：在仿真和真实环境中平均成功率分别提升超过3%和13%

## 摘要（原文）

> Research on robotic manipulation has developed a diverse set of policy paradigms, including vision-language-action (VLA) models, vision-action (VA) policies, and code-based compositional approaches. Concrete policies typically attain high success rates on specific task distributions but lim-ited generalization beyond it. Rather than proposing an other monolithic policy, we propose to leverage the complementary strengths of existing approaches through intelligent policy routing. We introduce RoboRouter, a training-free framework that maintains a pool of heterogeneous policies and learns to select the best-performing policy for each task through accumulated execution experience. Given a new task, RoboRouter constructs a semantic task representation, retrieves historical records of similar tasks, predicts the optimal policy choice without requiring trial-and-error, and incorporates structured feedback to refine subsequent routing decisions. Integrating a new policy into the system requires only lightweight evaluation and incurs no training overhead. Across simulation benchmark and real-world evaluations, RoboRouter consistently outperforms than in-dividual policies, improving average success rate by more than 3% in simulation and over 13% in real-world settings, while preserving execution efficiency. Our results demonstrate that intelligent routing across heterogeneous, off-the-shelf policies provides a practical and scalable pathway toward building more capable robotic systems.

