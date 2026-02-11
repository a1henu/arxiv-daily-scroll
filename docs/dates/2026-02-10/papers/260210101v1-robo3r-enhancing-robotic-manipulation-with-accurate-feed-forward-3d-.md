---
layout: default
title: Robo3R: Enhancing Robotic Manipulation with Accurate Feed-Forward 3D Reconstruction
---

# Robo3R: Enhancing Robotic Manipulation with Accurate Feed-Forward 3D Reconstruction
**arXiv**：[2602.10101v1](https://arxiv.org/abs/2602.10101) · [PDF](https://arxiv.org/pdf/2602.10101.pdf)  
**作者**：Sizhe Yang, Linning Xu, Hao Li, Juncheng Mu, Jia Zeng, Dahua Lin, Jiangmiao Pang  

**一句话要点**：提出Robo3R模型，通过前馈3D重建增强机器人操作的精度与实时性

**关键词**：机器人操作, 3D重建, 前馈模型, 度量一致性, 合成数据集, 实时感知

## 3 点简述
- 核心问题：现有3D感知方法在机器人操作中精度不足，深度传感器噪声大，重建模型缺乏度量一致性。
- 方法要点：联合推断尺度不变局部几何与相对相机位姿，通过全局相似变换统一到机器人坐标系，使用掩码点头和基于关键点的PnP优化。
- 实验或效果：在Robo3R-4M数据集上训练，优于现有方法，在下游任务如模仿学习和抓取合成中提升性能。

## 摘要（原文）

> 3D spatial perception is fundamental to generalizable robotic manipulation, yet obtaining reliable, high-quality 3D geometry remains challenging. Depth sensors suffer from noise and material sensitivity, while existing reconstruction models lack the precision and metric consistency required for physical interaction. We introduce Robo3R, a feed-forward, manipulation-ready 3D reconstruction model that predicts accurate, metric-scale scene geometry directly from RGB images and robot states in real time. Robo3R jointly infers scale-invariant local geometry and relative camera poses, which are unified into the scene representation in the canonical robot frame via a learned global similarity transformation. To meet the precision demands of manipulation, Robo3R employs a masked point head for sharp, fine-grained point clouds, and a keypoint-based Perspective-n-Point (PnP) formulation to refine camera extrinsics and global alignment. Trained on Robo3R-4M, a curated large-scale synthetic dataset with four million high-fidelity annotated frames, Robo3R consistently outperforms state-of-the-art reconstruction methods and depth sensors. Across downstream tasks including imitation learning, sim-to-real transfer, grasp synthesis, and collision-free motion planning, we observe consistent gains in performance, suggesting the promise of this alternative 3D sensing module for robotic manipulation.

