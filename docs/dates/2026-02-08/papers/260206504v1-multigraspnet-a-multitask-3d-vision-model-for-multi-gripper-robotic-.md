---
layout: default
title: MultiGraspNet: A Multitask 3D Vision Model for Multi-gripper Robotic Grasping
---

# MultiGraspNet: A Multitask 3D Vision Model for Multi-gripper Robotic Grasping
**arXiv**：[2602.06504v1](https://arxiv.org/abs/2602.06504) · [PDF](https://arxiv.org/pdf/2602.06504.pdf)  
**作者**：Stephany Ortuno-Chanelo, Paolo Rabino, Enrico Civitelli, Tatiana Tommasi, Raffaello Camoriano  

**一句话要点**：提出MultiGraspNet，一种多任务3D视觉模型，用于统一预测平行和真空夹爪的可行抓取姿态。

**关键词**：多任务学习, 3D视觉, 机器人抓取, 深度学习, 夹爪姿态预测

## 3 点简述
- 现有方法局限于单一夹爪或定制混合夹爪，缺乏通用性。
- 模型通过共享早期特征和夹爪特定细化器，在统一框架中同时预测两种夹爪的抓取姿态。
- 实验显示在真实多夹爪机器人设置中，真空任务抓取新物体提升32%，平行任务结果具有竞争力。

## 摘要（原文）

> Vision-based models for robotic grasping automate critical, repetitive, and draining industrial tasks. Existing approaches are typically limited in two ways: they either target a single gripper and are potentially applied on costly dual-arm setups, or rely on custom hybrid grippers that require ad-hoc learning procedures with logic that cannot be transferred across tasks, restricting their general applicability. In this work, we present MultiGraspNet, a novel multitask 3D deep learning method that predicts feasible poses simultaneously for parallel and vacuum grippers within a unified framework, enabling a single robot to handle multiple end effectors. The model is trained on the richly annotated GraspNet-1Billion and SuctionNet-1Billion datasets, which have been aligned for the purpose, and generates graspability masks quantifying the suitability of each scene point for successful grasps. By sharing early-stage features while maintaining gripper-specific refiners, MultiGraspNet effectively leverages complementary information across grasping modalities, enhancing robustness and adaptability in cluttered scenes. We characterize MultiGraspNet's performance with an extensive experimental analysis, demonstrating its competitiveness with single-task models on relevant benchmarks. We run real-world experiments on a single-arm multi-gripper robotic setup showing that our approach outperforms the vacuum baseline, grasping 16% percent more seen objects and 32% more of the novel ones, while obtaining competitive results for the parallel task.

