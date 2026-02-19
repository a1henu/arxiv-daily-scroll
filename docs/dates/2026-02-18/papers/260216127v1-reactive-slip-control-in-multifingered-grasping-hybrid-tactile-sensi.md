---
layout: default
title: Reactive Slip Control in Multifingered Grasping: Hybrid Tactile Sensing and Internal-Force Optimization
---

# Reactive Slip Control in Multifingered Grasping: Hybrid Tactile Sensing and Internal-Force Optimization
**arXiv**：[2602.16127v1](https://arxiv.org/abs/2602.16127) · [PDF](https://arxiv.org/pdf/2602.16127.pdf)  
**作者**：Théo Ayral, Saifeddine Aloui, Mathieu Grossard  

**一句话要点**：提出混合学习与模型方法，通过优化内力以阻止多指抓取中的滑动

**关键词**：多指抓取, 触觉传感, 内力优化, 二次规划, 闭环控制, 滑动检测

## 3 点简述
- 核心问题：多指机器人抓取中，外部扰动导致物体滑动，需快速检测并调整内力以稳定抓取。
- 方法要点：结合压电和压阻触觉传感，在线构建抓取矩阵，通过二次规划在抓取零空间更新内力。
- 实验或效果：实现35-40毫秒理论延迟，在受控试验中20毫秒检测滑动，展示闭环稳定抓取。

## 摘要（原文）

> We present a hybrid learning and model-based approach that adapts internal grasp forces to halt in-hand slip on a multifingered robotic gripper. A multimodal tactile stack combines piezoelectric (PzE) sensing for fast slip cues with piezoresistive (PzR) arrays for contact localization, enabling online construction of the grasp matrix. Upon slip, we update internal forces computed in the null space of the grasp via a quadratic program that preserves the object wrench while enforcing actuation limits. The pipeline yields a theoretical sensing-to-command latency of 35-40 ms, with 5 ms for PzR-based contact and geometry updates and about 4 ms for the quadratic program solve. In controlled trials, slip onset is detected at 20ms. We demonstrate closed-loop stabilization on multifingered grasps under external perturbations. Augmenting efficient analytic force control with learned tactile cues yields both robustness and rapid reactions, as confirmed in our end-to-end evaluation. Measured delays are dominated by the experimental data path rather than actual computation. The analysis outlines a clear route to sub-50 ms closed-loop stabilization.

