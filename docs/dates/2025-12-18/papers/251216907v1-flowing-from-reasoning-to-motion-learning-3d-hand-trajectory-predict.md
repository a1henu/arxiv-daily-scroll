---
layout: default
title: Flowing from Reasoning to Motion: Learning 3D Hand Trajectory Prediction from Egocentric Human Interaction Videos
---

# Flowing from Reasoning to Motion: Learning 3D Hand Trajectory Prediction from Egocentric Human Interaction Videos
**arXiv**：[2512.16907v1](https://arxiv.org/abs/2512.16907) · [PDF](https://arxiv.org/pdf/2512.16907.pdf)  
**作者**：Mingfei Chen, Yifan Wang, Zhengqin Li, Homanga Bharadhwaj, Yujin Chen, Chuan Qin, Ziyi Kou, Yuan Tian, Eric Whitmire, Rajinder Sodhi, Hrvoje Benko, Eli Shlizerman, Yue Liu  

**一句话要点**：提出EgoMAN数据集与模型，通过推理到运动框架解决交互感知的3D手部轨迹预测问题。

**关键词**：3D手部轨迹预测, 第一人称视频, 推理到运动框架, 视觉语言推理, 交互感知, 数据集构建

## 3 点简述
- 核心问题：现有3D手部轨迹预测数据集将运动与语义监督解耦，模型推理与动作关联弱。
- 方法要点：构建EgoMAN数据集，含219K轨迹和3M问答对；设计EgoMAN模型，通过轨迹令牌接口连接视觉语言推理与运动生成。
- 实验或效果：模型经渐进训练对齐推理与运动动态，生成准确且阶段感知的轨迹，在真实场景中具有泛化性。

## 摘要（原文）

> Prior works on 3D hand trajectory prediction are constrained by datasets that decouple motion from semantic supervision and by models that weakly link reasoning and action. To address these, we first present the EgoMAN dataset, a large-scale egocentric dataset for interaction stage-aware 3D hand trajectory prediction with 219K 6DoF trajectories and 3M structured QA pairs for semantic, spatial, and motion reasoning. We then introduce the EgoMAN model, a reasoning-to-motion framework that links vision-language reasoning and motion generation via a trajectory-token interface. Trained progressively to align reasoning with motion dynamics, our approach yields accurate and stage-aware trajectories with generalization across real-world scenes.

