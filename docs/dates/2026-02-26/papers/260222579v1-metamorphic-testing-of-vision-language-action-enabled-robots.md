---
layout: default
title: Metamorphic Testing of Vision-Language Action-Enabled Robots
---

# Metamorphic Testing of Vision-Language Action-Enabled Robots
**arXiv**：[2602.22579v1](https://arxiv.org/abs/2602.22579) · [PDF](https://arxiv.org/pdf/2602.22579.pdf)  
**作者**：Pablo Valle, Sergio Segura, Shaukat Ali, Aitor Arrieta  

**一句话要点**：提出基于蜕变测试的关系模式以缓解视觉-语言-动作机器人的测试预言问题

**关键词**：蜕变测试, 视觉-语言-动作模型, 机器人测试, 测试预言问题, 通用性评估

## 3 点简述
- 核心问题：VLA模型面临测试预言问题，包括指令特定预言复杂性和状态评估局限性。
- 方法要点：设计两种蜕变关系模式和五种蜕变关系，通过输入变化评估机器人轨迹影响。
- 实验或效果：在五个VLA模型、两个模拟机器人和四个任务中验证，能自动检测多种失败类型，具有通用性。

## 摘要（原文）

> Vision-Language-Action (VLA) models are multimodal robotic task controllers that, given an instruction and visual inputs, produce a sequence of low-level control actions (or motor commands) enabling a robot to execute the requested task in the physical environment. These systems face the test oracle problem from multiple perspectives. On the one hand, a test oracle must be defined for each instruction prompt, which is a complex and non-generalizable approach. On the other hand, current state-of-the-art oracles typically capture symbolic representations of the world (e.g., robot and object states), enabling the correctness evaluation of a task, but fail to assess other critical aspects, such as the quality with which VLA-enabled robots perform a task. In this paper, we explore whether Metamorphic Testing (MT) can alleviate the test oracle problem in this context. To do so, we propose two metamorphic relation patterns and five metamorphic relations to assess whether changes to the test inputs impact the original trajectory of the VLA-enabled robots. An empirical study involving five VLA models, two simulated robots, and four robotic tasks shows that MT can effectively alleviate the test oracle problem by automatically detecting diverse types of failures, including, but not limited to, uncompleted tasks. More importantly, the proposed MRs are generalizable, making the proposed approach applicable across different VLA models, robots, and tasks, even in the absence of test oracles.

