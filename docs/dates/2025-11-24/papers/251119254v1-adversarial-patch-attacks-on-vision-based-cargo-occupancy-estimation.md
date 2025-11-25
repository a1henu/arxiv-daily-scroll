---
layout: default
title: Adversarial Patch Attacks on Vision-Based Cargo Occupancy Estimation via Differentiable 3D Simulation
---

# Adversarial Patch Attacks on Vision-Based Cargo Occupancy Estimation via Differentiable 3D Simulation
**arXiv**：[2511.19254v1](https://arxiv.org/abs/2511.19254) · [PDF](https://arxiv.org/pdf/2511.19254.pdf)  
**作者**：Mohamed Rissal Hedna, Sesugh Samuel Nder  

**一句话要点**：提出基于可微分3D模拟的对抗补丁攻击方法，评估物流视觉系统安全性

**关键词**：对抗补丁攻击, 可微分渲染, 3D模拟, 物流视觉系统, 物理对抗攻击

## 3 点简述
- 核心问题：物流视觉系统易受物理对抗攻击，如补丁导致分类错误
- 方法要点：使用Mitsuba 3进行可微分渲染，优化补丁纹理适应3D环境变化
- 实验或效果：3D优化补丁在拒绝服务攻击中成功率84.94%，隐蔽攻击为30.32%

## 摘要（原文）

> Computer vision systems are increasingly adopted in modern logistics operations, including the estimation of trailer occupancy for planning, routing, and billing. Although effective, such systems may be vulnerable to physical adversarial attacks, particularly adversarial patches that can be printed and placed on interior surfaces. In this work, we study the feasibility of such attacks on a convolutional cargo-occupancy classifier using fully simulated 3D environments. Using Mitsuba 3 for differentiable rendering, we optimize patch textures across variations in geometry, lighting, and viewpoint, and compare their effectiveness to a 2D compositing baseline. Our experiments demonstrate that 3D-optimized patches achieve high attack success rates, especially in a denial-of-service scenario (empty to full), where success reaches 84.94 percent. Concealment attacks (full to empty) prove more challenging but still reach 30.32 percent. We analyze the factors influencing attack success, discuss implications for the security of automated logistics pipelines, and highlight directions for strengthening physical robustness. To our knowledge, this is the first study to investigate adversarial patch attacks for cargo-occupancy estimation in physically realistic, fully simulated 3D scenes.

