---
layout: default
title: SC-Net: Robust Correspondence Learning via Spatial and Cross-Channel Context
---

# SC-Net: Robust Correspondence Learning via Spatial and Cross-Channel Context
**arXiv**：[2512.23473v1](https://arxiv.org/abs/2512.23473) · [PDF](https://arxiv.org/pdf/2512.23473.pdf)  
**作者**：Shuyuan Lin, Hailiang Liao, Qiang Qi, Junjie Huang, Taotao Lai, Jian Weng  

**一句话要点**：提出SC-Net，通过空间和跨通道上下文增强双视图对应学习，以解决大视差场景中的全局上下文聚合不足和运动场过平滑问题。

**关键词**：双视图对应学习, 空间上下文, 跨通道交互, 运动场优化, 相对姿态估计, 离群点去除

## 3 点简述
- 核心问题：CNN骨干网络在双视图对应学习中可能无法有效聚合全局上下文，导致大视差场景下运动场过平滑。
- 方法要点：设计自适应聚焦正则化模块增强位置感知，双边场调整模块建模长程关系并促进空间与通道交互。
- 实验或效果：在YFCC100M和SUN3D数据集上，SC-Net在相对姿态估计和离群点去除任务中优于现有方法。

## 摘要（原文）

> Recent research has focused on using convolutional neural networks (CNNs) as the backbones in two-view correspondence learning, demonstrating significant superiority over methods based on multilayer perceptrons. However, CNN backbones that are not tailored to specific tasks may fail to effectively aggregate global context and oversmooth dense motion fields in scenes with large disparity. To address these problems, we propose a novel network named SC-Net, which effectively integrates bilateral context from both spatial and channel perspectives. Specifically, we design an adaptive focused regularization module (AFR) to enhance the model's position-awareness and robustness against spurious motion samples, thereby facilitating the generation of a more accurate motion field. We then propose a bilateral field adjustment module (BFA) to refine the motion field by simultaneously modeling long-range relationships and facilitating interaction across spatial and channel dimensions. Finally, we recover the motion vectors from the refined field using a position-aware recovery module (PAR) that ensures consistency and precision. Extensive experiments demonstrate that SC-Net outperforms state-of-the-art methods in relative pose estimation and outlier removal tasks on YFCC100M and SUN3D datasets. Source code is available at http://www.linshuyuan.com.

