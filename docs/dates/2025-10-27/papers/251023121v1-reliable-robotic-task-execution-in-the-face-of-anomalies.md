---
layout: default
title: Reliable Robotic Task Execution in the Face of Anomalies
---

# Reliable Robotic Task Execution in the Face of Anomalies
**arXiv**：[2510.23121v1](https://arxiv.org/abs/2510.23121) · [PDF](https://arxiv.org/pdf/2510.23121.pdf)  
**作者**：Bharath Santhanam, Alex Mitrevski, Santosh Thoduka, Sebastian Houben, Teena Hassan  

**一句话要点**：提出结合异常检测与恢复的框架，提升学习策略在开放环境中的任务执行可靠性。

**关键词**：机器人策略执行, 视觉异常检测, 恢复行为, 任务可靠性, 仿真到真实迁移

## 3 点简述
- 学习策略在开放环境中易因异常导致执行失败，缺乏内置处理机制。
- 训练异常检测模型，集成在线策略执行，触发三级顺序恢复过程。
- 在门把手到达和物体放置任务中验证，提高异常环境下的执行成功率。

## 摘要（原文）

> Learned robot policies have consistently been shown to be versatile, but they
> typically have no built-in mechanism for handling the complexity of open
> environments, making them prone to execution failures; this implies that
> deploying policies without the ability to recognise and react to failures may
> lead to unreliable and unsafe robot behaviour. In this paper, we present a
> framework that couples a learned policy with a method to detect visual
> anomalies during policy deployment and to perform recovery behaviours when
> necessary, thereby aiming to prevent failures. Specifically, we train an
> anomaly detection model using data collected during nominal executions of a
> trained policy. This model is then integrated into the online policy execution
> process, so that deviations from the nominal execution can trigger a
> three-level sequential recovery process that consists of (i) pausing the
> execution temporarily, (ii) performing a local perturbation of the robot's
> state, and (iii) resetting the robot to a safe state by sampling from a learned
> execution success model. We verify our proposed method in two different
> scenarios: (i) a door handle reaching task with a Kinova Gen3 arm using a
> policy trained in simulation and transferred to the real robot, and (ii) an
> object placing task with a UFactory xArm 6 using a general-purpose policy
> model. Our results show that integrating policy execution with anomaly
> detection and recovery increases the execution success rate in environments
> with various anomalies, such as trajectory deviations and adversarial human
> interventions.

