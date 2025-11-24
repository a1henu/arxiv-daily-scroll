---
layout: default
title: PEGS: Physics-Event Enhanced Large Spatiotemporal Motion Reconstruction via 3D Gaussian Splatting
---

# PEGS: Physics-Event Enhanced Large Spatiotemporal Motion Reconstruction via 3D Gaussian Splatting
**arXiv**：[2511.17116v1](https://arxiv.org/abs/2511.17116) · [PDF](https://arxiv.org/pdf/2511.17116.pdf)  
**作者**：Yijun Xu, Jingrui Zhang, Hongyi Liu, Yuhan Chen, Yuanyang Wang, Qingyao Guo, Dingwen Wang, Lei Yu, Chu He  

**一句话要点**：提出PEGS框架，结合物理先验与事件流增强，解决大时空尺度刚体运动重建问题

**关键词**：大时空运动重建, 3D高斯泼溅, 事件流增强, 物理先验, 运动去模糊

## 3 点简述
- 核心问题：大时空尺度刚体运动重建受限于建模范式、严重运动模糊和物理一致性不足
- 方法要点：集成物理先验与事件流，采用三重监督和运动感知模拟退火策略
- 实验或效果：在多样化场景中优于主流动态方法，重建性能优越

## 摘要（原文）

> Reconstruction of rigid motion over large spatiotemporal scales remains a challenging task due to limitations in modeling paradigms, severe motion blur, and insufficient physical consistency. In this work, we propose PEGS, a framework that integrates Physical priors with Event stream enhancement within a 3D Gaussian Splatting pipeline to perform deblurred target-focused modeling and motion recovery. We introduce a cohesive triple-level supervision scheme that enforces physical plausibility via an acceleration constraint, leverages event streams for high-temporal resolution guidance, and employs a Kalman regularizer to fuse multi-source observations. Furthermore, we design a motion-aware simulated annealing strategy that adaptively schedules the training process based on real-time kinematic states. We also contribute the first RGB-Event paired dataset targeting natural, fast rigid motion across diverse scenarios. Experiments show PEGS's superior performance in reconstructing motion over large spatiotemporal scales compared to mainstream dynamic methods.

