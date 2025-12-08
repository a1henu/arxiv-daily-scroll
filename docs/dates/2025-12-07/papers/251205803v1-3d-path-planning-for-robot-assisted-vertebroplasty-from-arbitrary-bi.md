---
layout: default
title: 3D Path Planning for Robot-assisted Vertebroplasty from Arbitrary Bi-plane X-ray via Differentiable Rendering
---

# 3D Path Planning for Robot-assisted Vertebroplasty from Arbitrary Bi-plane X-ray via Differentiable Rendering
**arXiv**：[2512.05803v1](https://arxiv.org/abs/2512.05803) · [PDF](https://arxiv.org/pdf/2512.05803.pdf)  
**作者**：Blanca Inigo, Benjamin D. Killeen, Rebecca Choi, Michelle Song, Ali Uneri, Majid Khan, Christopher Bailey, Axel Krieger, Mathias Unberath  

**一句话要点**：提出基于可微分渲染的框架，利用双平面X射线实现机器人辅助椎体成形术的3D路径规划，无需术前CT扫描。

**关键词**：可微分渲染, 3D路径规划, 机器人辅助手术, 椎体成形术, 统计形状模型, 双平面X射线

## 3 点简述
- 核心问题：机器人辅助手术中，路径规划依赖术前CT与术中2D图像配准，但椎体成形术常无术前CT，导致负担和成本高。
- 方法要点：结合可微分渲染与统计形状模型生成的椎体图谱，通过学习相似性损失动态优化形状和姿态，适应任意成像几何。
- 实验或效果：在重建指标上优于基线（DICE: 0.75 vs. 0.65），与先进模型ReVerteR相当（DICE: 0.77），双椎弓根规划成功率在合成和尸体数据中分别达82%和75%。

## 摘要（原文）

> Robotic systems are transforming image-guided interventions by enhancing accuracy and minimizing radiation exposure. A significant challenge in robotic assistance lies in surgical path planning, which often relies on the registration of intraoperative 2D images with preoperative 3D CT scans. This requirement can be burdensome and costly, particularly in procedures like vertebroplasty, where preoperative CT scans are not routinely performed. To address this issue, we introduce a differentiable rendering-based framework for 3D transpedicular path planning utilizing bi-planar 2D X-rays. Our method integrates differentiable rendering with a vertebral atlas generated through a Statistical Shape Model (SSM) and employs a learned similarity loss to refine the SSM shape and pose dynamically, independent of fixed imaging geometries. We evaluated our framework in two stages: first, through vertebral reconstruction from orthogonal X-rays for benchmarking, and second, via clinician-in-the-loop path planning using arbitrary-view X-rays. Our results indicate that our method outperformed a normalized cross-correlation baseline in reconstruction metrics (DICE: 0.75 vs. 0.65) and achieved comparable performance to the state-of-the-art model ReVerteR (DICE: 0.77), while maintaining generalization to arbitrary views. Success rates for bipedicular planning reached 82% with synthetic data and 75% with cadaver data, exceeding the 66% and 31% rates of a 2D-to-3D baseline, respectively. In conclusion, our framework facilitates versatile, CT-free 3D path planning for robot-assisted vertebroplasty, effectively accommodating real-world imaging diversity without the need for preoperative CT scans.

