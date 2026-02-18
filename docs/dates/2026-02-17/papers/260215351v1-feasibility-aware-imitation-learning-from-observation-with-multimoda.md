---
layout: default
title: Feasibility-aware Imitation Learning from Observation with Multimodal Feedback
---

# Feasibility-aware Imitation Learning from Observation with Multimodal Feedback
**arXiv**：[2602.15351v1](https://arxiv.org/abs/2602.15351) · [PDF](https://arxiv.org/pdf/2602.15351.pdf)  
**作者**：Kei Takahashi, Hikaru Sasaki, Takamitsu Matsubara  

**一句话要点**：提出FABCO方法，通过可行性估计和多模态反馈解决机器人模仿学习中演示动作不可行的问题。

**关键词**：模仿学习, 行为克隆, 可行性估计, 多模态反馈, 机器人动力学

## 3 点简述
- 核心问题：演示者与机器人物理差异导致演示动作可能不可行，且数据缺乏机器人动作。
- 方法要点：结合行为克隆与可行性估计，利用机器人动力学模型评估和反馈演示动作的可行性。
- 实验或效果：在两项任务中，FABCO相比无可行性反馈将模仿学习性能提升超过3.2倍。

## 摘要（原文）

> Imitation learning frameworks that learn robot control policies from demonstrators' motions via hand-mounted demonstration interfaces have attracted increasing attention. However, due to differences in physical characteristics between demonstrators and robots, this approach faces two limitations: i) the demonstration data do not include robot actions, and ii) the demonstrated motions may be infeasible for robots. These limitations make policy learning difficult. To address them, we propose Feasibility-Aware Behavior Cloning from Observation (FABCO). FABCO integrates behavior cloning from observation, which complements robot actions using robot dynamics models, with feasibility estimation. In feasibility estimation, the demonstrated motions are evaluated using a robot-dynamics model, learned from the robot's execution data, to assess reproducibility under the robot's dynamics. The estimated feasibility is used for multimodal feedback and feasibility-aware policy learning to improve the demonstrator's motions and learn robust policies. Multimodal feedback provides feasibility through the demonstrator's visual and haptic senses to promote feasible demonstrated motions. Feasibility-aware policy learning reduces the influence of demonstrated motions that are infeasible for robots, enabling the learning of policies that robots can execute stably. We conducted experiments with 15 participants on two tasks and confirmed that FABCO improves imitation learning performance by more than 3.2 times compared to the case without feasibility feedback.

