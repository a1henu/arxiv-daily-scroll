---
layout: default
title: Learning Omnidirectional Locomotion for a Salamander-Like Quadruped Robot
---

# Learning Omnidirectional Locomotion for a Salamander-Like Quadruped Robot
**arXiv**：[2511.08299v1](https://arxiv.org/abs/2511.08299) · [PDF](https://arxiv.org/pdf/2511.08299.pdf)  
**作者**：Zhiang Liu, Yang Liu, Yongchun Fang, Xian Guo  

**一句话要点**：提出学习框架使机器人获得全向步态，无需参考运动。

**关键词**：四足机器人, 全向运动, 强化学习, 相位控制, 形态对称

## 3 点简述
- 现有控制器依赖预定义步态，限制机器人灵活性和多样性。
- 使用相位变量和相位覆盖奖励，探索腿部相位空间。
- 实验获得22种全向步态，展示动态和对称运动。

## 摘要（原文）

> Salamander-like quadruped robots are designed inspired by the skeletal structure of their biological counterparts. However, existing controllers cannot fully exploit these morphological features and largely rely on predefined gait patterns or joint trajectories, which prevents the generation of diverse and flexible locomotion and limits their applicability in real-world scenarios. In this paper, we propose a learning framework that enables the robot to acquire a diverse repertoire of omnidirectional gaits without reference motions. Each body part is controlled by a phase variable capable of forward and backward evolution, with a phase coverage reward to promote the exploration of the leg phase space. Additionally, morphological symmetry of the robot is incorporated via data augmentation, improving sample efficiency and enforcing both motion-level and task-level symmetry in learned behaviors. Extensive experiments show that the robot successfully acquires 22 omnidirectional gaits exhibiting both dynamic and symmetric movements, demonstrating the effectiveness of the proposed learning framework.

