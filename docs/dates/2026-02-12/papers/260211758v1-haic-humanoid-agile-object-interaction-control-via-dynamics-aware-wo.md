---
layout: default
title: HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model
---

# HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model
**arXiv**：[2602.11758v1](https://arxiv.org/abs/2602.11758) · [PDF](https://arxiv.org/pdf/2602.11758.pdf)  
**作者**：Dongting Li, Xingyu Chen, Qianyang Wu, Bo Chen, Sikai Wu, Hanyu Wu, Guoyao Zhang, Liang Li, Mingliang Zhou, Diyun Xiang, Jianzhu Ma, Qiang Zhang, Renjing Xu  

**一句话要点**：提出HAIC框架，通过动态感知世界模型解决人形机器人对欠驱动物体的鲁棒交互控制问题。

**关键词**：人形机器人控制, 动态预测, 欠驱动物体交互, 世界模型, 本体感知

## 3 点简述
- 核心问题：现有方法忽略欠驱动物体的独立动力学和非完整约束，导致控制挑战。
- 方法要点：使用动态预测器从本体感知历史估计物体高阶状态，并投影到几何先验形成动态占用图。
- 实验效果：在人形机器人上实现高成功率敏捷任务，如滑板和多物体长时程搬运。

## 摘要（原文）

> Humanoid robots show promise for complex whole-body tasks in unstructured environments. Although Human-Object Interaction (HOI) has advanced, most methods focus on fully actuated objects rigidly coupled to the robot, ignoring underactuated objects with independent dynamics and non-holonomic constraints. These introduce control challenges from coupling forces and occlusions. We present HAIC, a unified framework for robust interaction across diverse object dynamics without external state estimation. Our key contribution is a dynamics predictor that estimates high-order object states (velocity, acceleration) solely from proprioceptive history. These predictions are projected onto static geometric priors to form a spatially grounded dynamic occupancy map, enabling the policy to infer collision boundaries and contact affordances in blind spots. We use asymmetric fine-tuning, where a world model continuously adapts to the student policy's exploration, ensuring robust state estimation under distribution shifts. Experiments on a humanoid robot show HAIC achieves high success rates in agile tasks (skateboarding, cart pushing/pulling under various loads) by proactively compensating for inertial perturbations, and also masters multi-object long-horizon tasks like carrying a box across varied terrain by predicting the dynamics of multiple objects.

