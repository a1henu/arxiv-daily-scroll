---
layout: default
title: Crowd-FM: Learned Optimal Selection of Conditional Flow Matching-generated Trajectories for Crowd Navigation
---

# Crowd-FM: Learned Optimal Selection of Conditional Flow Matching-generated Trajectories for Crowd Navigation
**arXiv**：[2602.06698v1](https://arxiv.org/abs/2602.06698) · [PDF](https://arxiv.org/pdf/2602.06698.pdf)  
**作者**：Antareep Singha, Laksh Nanwani, Mathai Mathew P., Samkit Jain, Phani Teja Singamaneni, Arun Kumar Singh, K. Madhava Krishna  

**一句话要点**：提出Crowd-FM方法，通过条件流匹配和评分网络优化机器人人群导航的安全性和类人性

**关键词**：人群导航, 条件流匹配, 轨迹规划, 机器人安全, 类人轨迹, 评分网络

## 3 点简述
- 核心问题：移动机器人在密集非结构化人群中的安全高效本地规划，需提升轨迹类人性以增强接受度
- 方法要点：训练条件流匹配策略学习碰撞自由轨迹基元，结合评分网络评估轨迹类人性，推理时选择最高分轨迹
- 实验或效果：CFM策略在成功率上优于现有学习基线，推理时细化可超越基于优化的方法，评分网络优于手动成本函数

## 摘要（原文）

> Safe and computationally efficient local planning for mobile robots in dense, unstructured human crowds remains a fundamental challenge. Moreover, ensuring that robot trajectories are similar to how a human moves will increase the acceptance of the robot in human environments. In this paper, we present Crowd-FM, a learning-based approach to address both safety and human-likeness challenges. Our approach has two novel components. First, we train a Conditional Flow-Matching (CFM) policy over a dataset of optimally controlled trajectories to learn a set of collision-free primitives that a robot can choose at any given scenario. The chosen optimal control solver can generate multi-modal collision-free trajectories, allowing the CFM policy to learn a diverse set of maneuvers. Secondly, we learn a score function over a dataset of human demonstration trajectories that provides a human-likeness score for the flow primitives. At inference time, computing the optimal trajectory requires selecting the one with the highest score. Our approach improves the state-of-the-art by showing that our CFM policy alone can produce collision-free navigation with a higher success rate than existing learning-based baselines. Furthermore, when augmented with inference-time refinement, our approach can outperform even expensive optimisation-based planning approaches. Finally, we validate that our scoring network can select trajectories closer to the expert data than a manually designed cost function.

