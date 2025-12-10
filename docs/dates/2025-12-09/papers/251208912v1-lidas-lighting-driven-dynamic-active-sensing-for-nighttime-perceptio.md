---
layout: default
title: LiDAS: Lighting-driven Dynamic Active Sensing for Nighttime Perception
---

# LiDAS: Lighting-driven Dynamic Active Sensing for Nighttime Perception
**arXiv**：[2512.08912v1](https://arxiv.org/abs/2512.08912) · [PDF](https://arxiv.org/pdf/2512.08912.pdf)  
**作者**：Simon de Moreau, Andrei Bursuc, Hafid El-Idrissi, Fabien Moutarde  

**一句话要点**：提出LiDAS系统，通过动态主动照明优化夜间感知性能

**关键词**：夜间感知, 主动照明, 闭环控制, 零样本泛化, 节能优化

## 3 点简述
- 核心问题：夜间环境光照不足，现有相机感知方法被动依赖场景照明，性能受限。
- 方法要点：结合现成视觉模型与高清头灯，闭环预测最优照明场，动态重分配光线至目标区域。
- 实验或效果：在真实闭环驾驶场景中零样本部署，相比标准近光灯提升mAP50 18.7%和mIoU 5.0%，节能40%。

## 摘要（原文）

> Nighttime environments pose significant challenges for camera-based perception, as existing methods passively rely on the scene lighting. We introduce Lighting-driven Dynamic Active Sensing (LiDAS), a closed-loop active illumination system that combines off-the-shelf visual perception models with high-definition headlights. Rather than uniformly brightening the scene, LiDAS dynamically predicts an optimal illumination field that maximizes downstream perception performance, i.e., decreasing light on empty areas to reallocate it on object regions. LiDAS enables zero-shot nighttime generalization of daytime-trained models through adaptive illumination control. Trained on synthetic data and deployed zero-shot in real-world closed-loop driving scenarios, LiDAS enables +18.7% mAP50 and +5.0% mIoU over standard low-beam at equal power. It maintains performances while reducing energy use by 40%. LiDAS complements domain-generalization methods, further strengthening robustness without retraining. By turning readily available headlights into active vision actuators, LiDAS offers a cost-effective solution to robust nighttime perception.

