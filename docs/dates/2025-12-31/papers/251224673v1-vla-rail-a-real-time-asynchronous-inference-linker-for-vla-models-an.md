---
layout: default
title: VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots
---

# VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots
**arXiv**：[2512.24673v1](https://arxiv.org/abs/2512.24673) · [PDF](https://arxiv.org/pdf/2512.24673.pdf)  
**作者**：Yongsheng Zhao, Lei Zhao, Baoping Cheng, Gongxin Yao, Xuanzhang Wen, Han Gao  

**一句话要点**：提出VLA-RAIL框架以解决机器人动作执行中的抖动与停顿问题

**关键词**：视觉语言动作模型, 机器人运动控制, 异步推理, 轨迹平滑, 动作块融合, 实时系统

## 3 点简述
- 核心问题：现有VLA模型在机器人动作融合时易产生抖动、停滞，影响执行速度与成功率。
- 方法要点：采用异步推理与运动控制，结合轨迹平滑器和块融合器确保动作连续性。
- 实验或效果：在动态仿真和真实任务中验证，显著减少抖动、提升速度与成功率。

## 摘要（原文）

> Vision-Language-Action (VLA) models have achieved remarkable breakthroughs in robotics, with the action chunk playing a dominant role in these advances. Given the real-time and continuous nature of robotic motion control, the strategies for fusing a queue of successive action chunks have a profound impact on the overall performance of VLA models. Existing methods suffer from jitter, stalling, or even pauses in robotic action execution, which not only limits the achievable execution speed but also reduces the overall success rate of task completion. This paper introduces VLA-RAIL (A Real-Time Asynchronous Inference Linker), a novel framework designed to address these issues by conducting model inference and robot motion control asynchronously and guaranteeing smooth, continuous, and high-speed action execution. The core contributions of the paper are two fold: a Trajectory Smoother that effectively filters out the noise and jitter in the trajectory of one action chunk using polynomial fitting and a Chunk Fuser that seamlessly align the current executing trajectory and the newly arrived chunk, ensuring position, velocity, and acceleration continuity between two successive action chunks. We validate the effectiveness of VLA-RAIL on a benchmark of dynamic simulation tasks and several real-world manipulation tasks. Experimental results demonstrate that VLA-RAIL significantly reduces motion jitter, enhances execution speed, and improves task success rates, which will become a key infrastructure for the large-scale deployment of VLA models.

