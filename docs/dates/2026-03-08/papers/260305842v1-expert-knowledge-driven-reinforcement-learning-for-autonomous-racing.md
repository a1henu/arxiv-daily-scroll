---
layout: default
title: Expert Knowledge-driven Reinforcement Learning for Autonomous Racing via Trajectory Guidance and Dynamics Constraints
---

# Expert Knowledge-driven Reinforcement Learning for Autonomous Racing via Trajectory Guidance and Dynamics Constraints
**arXiv**：[2603.05842v1](https://arxiv.org/abs/2603.05842) · [PDF](https://arxiv.org/pdf/2603.05842.pdf)  
**作者**：Bo Leng, Weiqi Zhang, Zhuoren Li, Lu Xiong, Guizhe Jin, Ran Yu, Chen Lv  

**一句话要点**：提出轨迹引导与动力学约束强化学习方法以提升自动驾驶赛车性能与安全

**关键词**：自动驾驶赛车, 强化学习, 轨迹引导, 动力学约束, 课程学习, 控制屏障函数

## 3 点简述
- 针对高动态非线性赛车环境，强化学习存在训练不稳定与不安全动作问题
- 方法整合专家轨迹引导、动力学约束与多阶段课程学习，实现性能与安全协同优化
- 在Tempelhof机场赛道仿真中验证，有效提高圈速与驾驶稳定性

## 摘要（原文）

> Reinforcement learning has demonstrated significant potential in the field of autonomous driving. However, it suffers from defects such as training instability and unsafe action outputs when faced with autonomous racing environments characterized by high dynamics and strong nonlinearities. To this end, this paper proposes a trajectory guidance and dynamics constraints Reinforcement Learning (TraD-RL) method for autonomous racing. The key features of this method are as follows: 1) leveraging the prior expert racing line to construct an augmented state representation and facilitate reward shaping, thereby integrating domain knowledge to stabilize early-stage policy learning; 2) embedding explicit vehicle dynamic priors into a safe operating envelope formulated via control barrier functions to enable safety-constrained learning; and 3) adopting a multi-stage curriculum learning strategy that shifts from expert-guided learning to autonomous exploration, allowing the learned policy to surpass expert-level performance. The proposed method is evaluated in a high-fidelity simulation environment modeled after the Tempelhof Airport Street Circuit. Experimental results demonstrate that TraD-RL effectively improves both lap speed and driving stability of the autonomous racing vehicle, achieving a synergistic optimization of racing performance and safety.

