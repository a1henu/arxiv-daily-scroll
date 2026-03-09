---
layout: default
title: Improved hopping control on slopes for small robots using spring mass modeling
---

# Improved hopping control on slopes for small robots using spring mass modeling
**arXiv**：[2603.05902v1](https://arxiv.org/abs/2603.05902) · [PDF](https://arxiv.org/pdf/2603.05902.pdf)  
**作者**：Heston Roberts, Pronoy Sarker, Sm Ashikul Islam, Min Gyu Kim  

**一句话要点**：提出基于弹簧质量模型的斜坡跳跃控制方法，以解决小型机器人在倾斜地形上的着陆失稳问题。

**关键词**：跳跃机器人, 斜坡控制, 弹簧质量模型, 着陆稳定性, 低成本平台, 自然地形导航

## 3 点简述
- 核心问题：斜坡导致着陆时产生不期望的旋转，使跳跃机器人失去平衡。
- 方法要点：使用弹簧质量模型分析斜坡效应，通过调整着陆角度和施加起飞前校正扭矩来抵消旋转。
- 实验或效果：仿真验证该方法能显著提升着陆稳定性，适用于低成本平台，增强在自然地形中的可靠跳跃能力。

## 摘要（原文）

> Hopping robots often lose balance on slopes because the tilted ground creates unwanted rotation at landing. This work analyzes that effect using a simple spring mass model and identifies how slope induced impulses destabilize the robot. To address this, we introduce two straightforward fixes, adjusting the bodys touchdown angle based on the slope and applying a small corrective torque before takeoff. Together, these steps effectively cancel the unwanted rotation caused by inclined terrain, allowing the robot to land smoothly and maintain stable hopping even on steep slopes. Moreover, the proposed method remains simple enough to implement on low cost robotic platforms without requiring complex sensing or computation. By combining this analytical model with minimal control actions, this approach provides a practical path toward reliable hopping on uneven terrain. The results from simulation confirm that even small slope aware adjustments can dramatically improve landing stability, making the technique suitable for future autonomous field robots that must navigate natural environments such as hills, rubble, and irregular outdoor landscapes.

