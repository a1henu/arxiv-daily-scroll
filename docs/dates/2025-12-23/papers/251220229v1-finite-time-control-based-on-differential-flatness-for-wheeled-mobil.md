---
layout: default
title: Finite-Time Control Based on Differential Flatness for Wheeled Mobile Robots with Experimental Validation
---

# Finite-Time Control Based on Differential Flatness for Wheeled Mobile Robots with Experimental Validation
**arXiv**：[2512.20229v1](https://arxiv.org/abs/2512.20229) · [PDF](https://arxiv.org/pdf/2512.20229.pdf)  
**作者**：Imtiaz Ur Rehman, Moussa Labbadi, Amine Abadi, Lew Lew Yan Voon  

**一句话要点**：提出基于微分平坦度的积分非线性超平面滑模控制，用于轮式移动机器人在扰动下的鲁棒跟踪。

**关键词**：轮式移动机器人, 微分平坦度, 滑模控制, 鲁棒跟踪, 实验验证

## 3 点简述
- 核心问题：轮式移动机器人在强风或不平等路径等扰动下跟踪预定路线的性能下降。
- 方法要点：利用运动学模型的微分平坦度将模型线性化，设计积分非线性超平面滑模控制以增强鲁棒性。
- 实验或效果：通过TurtleBot3室内实验验证了方法的可行性和有效性，并与现有方法进行了比较。

## 摘要（原文）

> A robust tracking control strategy is designed to empower wheeled mobile robots (WMRs) to track predetermined routes while operating in diverse fields and encountering disturbances like strong winds or uneven path conditions, which affect tracking performance. Ensuring the applicability of this tracking method in real-world scenarios is essential. To accomplish this, the WMR model is initially transformed into a linear canonical form by leveraging the differential flatness of its kinematic model, facilitating controller design. Subsequently, a novel integral nonlinear hyperplane-based sliding mode control (INH-SMC) technique is proposed for WMR under disturbances. The stability of the technique is analyzed and verified. Finally, its practical viability is demonstrated through a comparative real-world indoor experiment on a TurtleBot3 WMR subjected to disturbances, confirming the feasibility and efficacy of the proposed approach.

