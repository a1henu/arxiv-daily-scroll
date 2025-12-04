---
layout: default
title: GOMP: Grasped Object Manifold Projection for Multimodal Imitation Learning of Manipulation
---

# GOMP: Grasped Object Manifold Projection for Multimodal Imitation Learning of Manipulation
**arXiv**：[2512.03347v1](https://arxiv.org/abs/2512.03347) · [PDF](https://arxiv.org/pdf/2512.03347.pdf)  
**作者**：William van den Bogert, Gregory Linkowski, Nima Fazeli  

**一句话要点**：提出GOMP方法，通过低维流形投影解决模仿学习中轨迹精度不足的问题，应用于精确装配任务。

**关键词**：模仿学习, 精确装配, 低维流形投影, 触觉反馈, 交互式学习, 累积误差

## 3 点简述
- 模仿学习在工业装配等重复性操作任务中潜力大，但常因累积误差导致轨迹精度不足。
- GOMP通过将非刚性抓取物体约束到低维流形，减少误差，方法基于专家数据学习并采用交互式调整。
- 在四个精确装配任务中验证，使用触觉反馈，方法保持模态无关性，理论分析改进误差界限。

## 摘要（原文）

> Imitation Learning (IL) holds great potential for learning repetitive manipulation tasks, such as those in industrial assembly. However, its effectiveness is often limited by insufficient trajectory precision due to compounding errors. In this paper, we introduce Grasped Object Manifold Projection (GOMP), an interactive method that mitigates these errors by constraining a non-rigidly grasped object to a lower-dimensional manifold. GOMP assumes a precise task in which a manipulator holds an object that may shift within the grasp in an observable manner and must be mated with a grounded part. Crucially, all GOMP enhancements are learned from the same expert dataset used to train the base IL policy, and are adjusted with an n-arm bandit-based interactive component. We propose a theoretical basis for GOMP's improvement upon the well-known compounding error bound in IL literature. We demonstrate the framework on four precise assembly tasks using tactile feedback, and note that the approach remains modality-agnostic. Data and videos are available at williamvdb.github.io/GOMPsite.

