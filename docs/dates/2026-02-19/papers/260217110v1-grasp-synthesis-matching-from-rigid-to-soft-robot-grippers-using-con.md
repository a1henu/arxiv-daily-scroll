---
layout: default
title: Grasp Synthesis Matching From Rigid To Soft Robot Grippers Using Conditional Flow Matching
---

# Grasp Synthesis Matching From Rigid To Soft Robot Grippers Using Conditional Flow Matching
**arXiv**：[2602.17110v1](https://arxiv.org/abs/2602.17110) · [PDF](https://arxiv.org/pdf/2602.17110.pdf)  
**作者**：Tanisha Parulekar, Ge Shi, Josh Pinskier, David Howard, Jen Jen Chung  

**一句话要点**：提出基于条件流匹配的框架，将刚性夹爪抓取姿态映射到软体夹爪以解决表示差距问题。

**关键词**：抓取合成, 条件流匹配, 软体机器人, 姿态映射, 数据高效学习

## 3 点简述
- 核心问题：刚性夹爪抓取合成方法不适用于软体夹爪，导致数据密集且模型不准确。
- 方法要点：使用条件流匹配学习从刚性到软体夹爪的复杂姿态映射，结合U-Net自编码器处理物体几何。
- 实验或效果：在7自由度机器人上验证，CFM生成姿态相比基线显著提升抓取成功率，尤其对圆柱和球形物体。

## 摘要（原文）

> A representation gap exists between grasp synthesis for rigid and soft grippers. Anygrasp [1] and many other grasp synthesis methods are designed for rigid parallel grippers, and adapting them to soft grippers often fails to capture their unique compliant behaviors, resulting in data-intensive and inaccurate models. To bridge this gap, this paper proposes a novel framework to map grasp poses from a rigid gripper model to a soft Fin-ray gripper. We utilize Conditional Flow Matching (CFM), a generative model, to learn this complex transformation. Our methodology includes a data collection pipeline to generate paired rigid-soft grasp poses. A U-Net autoencoder conditions the CFM model on the object's geometry from a depth image, allowing it to learn a continuous mapping from an initial Anygrasp pose to a stable Fin-ray gripper pose. We validate our approach on a 7-DOF robot, demonstrating that our CFM-generated poses achieve a higher overall success rate for seen and unseen objects (34% and 46% respectively) compared to the baseline rigid poses (6% and 25% respectively) when executed by the soft gripper. The model shows significant improvements, particularly for cylindrical (50% and 100% success for seen and unseen objects) and spherical objects (25% and 31% success for seen and unseen objects), and successfully generalizes to unseen objects. This work presents CFM as a data-efficient and effective method for transferring grasp strategies, offering a scalable methodology for other soft robotic systems.

