---
layout: default
title: SG-DOR: Learning Scene Graphs with Direction-Conditioned Occlusion Reasoning for Pepper Plants
---

# SG-DOR: Learning Scene Graphs with Direction-Conditioned Occlusion Reasoning for Pepper Plants
**arXiv**：[2603.06512v1](https://arxiv.org/abs/2603.06512) · [PDF](https://arxiv.org/pdf/2603.06512.pdf)  
**作者**：Rohit Menon, Niklas Mueller-Goldingen, Sicong Pan, Gokul Krishna Chenchani, Maren Bennewitz  

**一句话要点**：提出SG-DOR框架，通过方向条件遮挡推理学习场景图，用于辣椒植株的机器人采摘规划。

**关键词**：场景图学习, 方向条件遮挡推理, 机器人采摘, 图神经网络, 辣椒植株, 实例分割

## 3 点简述
- 核心问题：密集作物冠层中机器人采摘需处理器官间几何与方向条件遮挡关系。
- 方法要点：基于实例分割点云，构建场景图编码物理附着和方向条件遮挡，采用方向感知图神经网络。
- 实验或效果：在合成辣椒数据集上，遮挡预测和附着推理性能优于强消融实验，支持下游干预规划。

## 摘要（原文）

> Robotic harvesting in dense crop canopies requires effective interventions that depend not only on geometry, but also on explicit, direction-conditioned relations identifying which organs obstruct a target fruit. We present SG-DOR (Scene Graphs with Direction-Conditioned Occlusion Reasoning), a relational framework that, given instance-segmented organ point clouds, infers a scene graph encoding physical attachments and direction-conditioned occlusion. We introduce an occlusion ranking task for retrieving and ranking candidate leaves for a target fruit and approach direction, and propose a direction-aware graph neural architecture with per-fruit leaf-set attention and union-level aggregation. Experiments on a multi-plant synthetic pepper dataset show improved occlusion prediction (F1=0.73, NDCG@3=0.85) and attachment inference (edge F1=0.83) over strong ablations, yielding a structured relational signal for downstream intervention planning.

