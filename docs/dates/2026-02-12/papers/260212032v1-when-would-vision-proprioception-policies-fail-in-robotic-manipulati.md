---
layout: default
title: When would Vision-Proprioception Policies Fail in Robotic Manipulation?
---

# When would Vision-Proprioception Policies Fail in Robotic Manipulation?
**arXiv**：[2602.12032v1](https://arxiv.org/abs/2602.12032) · [PDF](https://arxiv.org/pdf/2602.12032.pdf)  
**作者**：Jingxian Lu, Wenke Xia, Yuxuan Wu, Zhiwu Lu, Di Hu  

**一句话要点**：提出GAP算法以解决视觉-本体感知策略在机器人操作中运动过渡阶段的泛化失败问题

**关键词**：机器人操作, 视觉-本体感知策略, 梯度调整, 运动过渡阶段, 泛化性能

## 3 点简述
- 核心问题：视觉-本体感知策略在机器人运动过渡阶段泛化不一致，视觉模态作用受限
- 方法要点：基于相位引导的梯度调整算法，动态调制本体感知优化以促进视觉模态学习
- 实验或效果：在仿真和真实环境、单臂和双臂设置及多种模型中验证了GAP的有效性

## 摘要（原文）

> Proprioceptive information is critical for precise servo control by providing real-time robotic states. Its collaboration with vision is highly expected to enhance performances of the manipulation policy in complex tasks. However, recent studies have reported inconsistent observations on the generalization of vision-proprioception policies. In this work, we investigate this by conducting temporally controlled experiments. We found that during task sub-phases that robot's motion transitions, which require target localization, the vision modality of the vision-proprioception policy plays a limited role. Further analysis reveals that the policy naturally gravitates toward concise proprioceptive signals that offer faster loss reduction when training, thereby dominating the optimization and suppressing the learning of the visual modality during motion-transition phases. To alleviate this, we propose the Gradient Adjustment with Phase-guidance (GAP) algorithm that adaptively modulates the optimization of proprioception, enabling dynamic collaboration within the vision-proprioception policy. Specifically, we leverage proprioception to capture robotic states and estimate the probability of each timestep in the trajectory belonging to motion-transition phases. During policy learning, we apply fine-grained adjustment that reduces the magnitude of proprioception's gradient based on estimated probabilities, leading to robust and generalizable vision-proprioception policies. The comprehensive experiments demonstrate GAP is applicable in both simulated and real-world environments, across one-arm and dual-arm setups, and compatible with both conventional and Vision-Language-Action models. We believe this work can offer valuable insights into the development of vision-proprioception policies in robotic manipulation.

