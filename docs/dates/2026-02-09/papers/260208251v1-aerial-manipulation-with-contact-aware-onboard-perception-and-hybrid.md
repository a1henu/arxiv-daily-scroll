---
layout: default
title: Aerial Manipulation with Contact-Aware Onboard Perception and Hybrid Control
---

# Aerial Manipulation with Contact-Aware Onboard Perception and Hybrid Control
**arXiv**：[2602.08251v1](https://arxiv.org/abs/2602.08251) · [PDF](https://arxiv.org/pdf/2602.08251.pdf)  
**作者**：Yuanzhu Zhan, Yufei Jiang, Muqing Cao, Junyi Geng  

**一句话要点**：提出基于机载感知与混合控制的接触式空中操纵方法，以解决依赖外部动捕和粗粒度交互的部署限制。

**关键词**：空中操纵, 机载感知, 视觉惯性里程计, 图像视觉伺服, 混合控制, 接触力调节

## 3 点简述
- 核心问题：传统空中操纵依赖外部动捕，导致部署受限，难以实现精确接触式任务。
- 方法要点：结合增强视觉惯性里程计和图像视觉伺服，集成混合力-运动控制器，实现机载感知与接触力调节。
- 实验或效果：实验显示，接触时速度估计提升66.01%，实现稳定目标接近和力保持，提升野外部署能力。

## 摘要（原文）

> Aerial manipulation (AM) promises to move Unmanned Aerial Vehicles (UAVs) beyond passive inspection to contact-rich tasks such as grasping, assembly, and in-situ maintenance. Most prior AM demonstrations rely on external motion capture (MoCap) and emphasize position control for coarse interactions, limiting deployability. We present a fully onboard perception-control pipeline for contact-rich AM that achieves accurate motion tracking and regulated contact wrenches without MoCap. The main components are (1) an augmented visual-inertial odometry (VIO) estimator with contact-consistency factors that activate only during interaction, tightening uncertainty around the contact frame and reducing drift, and (2) image-based visual servoing (IBVS) to mitigate perception-control coupling, together with a hybrid force-motion controller that regulates contact wrenches and lateral motion for stable contact. Experiments show that our approach closes the perception-to-wrench loop using only onboard sensing, yielding an velocity estimation improvement of 66.01% at contact, reliable target approach, and stable force holding-pointing toward deployable, in-the-wild aerial manipulation.

