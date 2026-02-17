---
layout: default
title: Real-time Monocular 2D and 3D Perception of Endoluminal Scenes for Controlling Flexible Robotic Endoscopic Instruments
---

# Real-time Monocular 2D and 3D Perception of Endoluminal Scenes for Controlling Flexible Robotic Endoscopic Instruments
**arXiv**：[2602.14666v1](https://arxiv.org/abs/2602.14666) · [PDF](https://arxiv.org/pdf/2602.14666.pdf)  
**作者**：Ruofeng Wei, Kai Chen, Yui Lun Ng, Yiyao Ma, Justin Di-Lang Ho, Hon Sing Tong, Xiaomei Wang, Jing Dai, Ka-Wai Kwok, Qi Dou  

**一句话要点**：提出基于单目内窥镜的2D和3D感知平台，以提升柔性机器人内镜手术中的器械控制精度

**关键词**：单目内窥镜感知, 柔性机器人控制, 物理模拟器, 内镜手术, 学习型算法, 实时感知

## 3 点简述
- 核心问题：内镜手术中柔性器械定位和距离测量困难，影响手术效果和学习曲线
- 方法要点：开发学习型感知算法和物理真实模拟器，生成数据并优化控制
- 实验或效果：在原型系统上验证，减少轨迹跟踪任务操作时间超70%，增强手术场景理解

## 摘要（原文）

> Endoluminal surgery offers a minimally invasive option for early-stage gastrointestinal and urinary tract cancers but is limited by surgical tools and a steep learning curve. Robotic systems, particularly continuum robots, provide flexible instruments that enable precise tissue resection, potentially improving outcomes. This paper presents a visual perception platform for a continuum robotic system in endoluminal surgery. Our goal is to utilize monocular endoscopic image-based perception algorithms to identify position and orientation of flexible instruments and measure their distances from tissues. We introduce 2D and 3D learning-based perception algorithms and develop a physically-realistic simulator that models flexible instruments dynamics. This simulator generates realistic endoluminal scenes, enabling control of flexible robots and substantial data collection. Using a continuum robot prototype, we conducted module and system-level evaluations. Results show that our algorithms improve control of flexible instruments, reducing manipulation time by over 70% for trajectory-following tasks and enhancing understanding of surgical scenarios, leading to robust endoluminal surgeries.

