---
layout: default
title: SpikingTac: A Miniaturized Neuromorphic Visuotactile Sensor for High-Precision Dynamic Tactile Imprint Tracking
---

# SpikingTac: A Miniaturized Neuromorphic Visuotactile Sensor for High-Precision Dynamic Tactile Imprint Tracking
**arXiv**：[2602.23654v1](https://arxiv.org/abs/2602.23654) · [PDF](https://arxiv.org/pdf/2602.23654.pdf)  
**作者**：Tianyu Jiang, Chaofan Zhang, Shaolin Zhang, Shaowei Cui, Shuo Wang  

**一句话要点**：提出SpikingTac微型神经形态触觉传感器，以解决事件相机体积大和硅胶迟滞问题，实现高精度动态触觉跟踪。

**关键词**：神经形态传感器, 事件相机, 触觉感知, 动态跟踪, 迟滞补偿, 微型化设计

## 3 点简述
- 问题：高速事件驱动触觉传感器集成受限，标准事件相机体积大，且硅胶弹性体存在粘弹性迟滞。
- 方法：设计微型独立事件相机模块，结合全局动态状态图和去噪网络，提出迟滞感知增量更新律与空间增益阻尼机制。
- 效果：实验显示零位稳定性高，动态任务中避障超调小，几何精度达亚毫米级，性能优于传统帧基传感器。

## 摘要（原文）

> High-speed event-driven tactile sensors are essential for achieving human-like dynamic manipulation, yet their integration is often limited by the bulkiness of standard event cameras. This paper presents SpikingTac, a miniaturized, highly integrated neuromorphic tactile sensor featuring a custom standalone event camera module, achieved with a total material cost of less than \$150. We construct a global dynamic state map coupled with an unsupervised denoising network to enable precise tracking at a 1000~Hz perception rate and 350~Hz tracking frequency. Addressing the viscoelastic hysteresis of silicone elastomers, we propose a hysteresis-aware incremental update law with a spatial gain damping mechanism. Experimental results demonstrate exceptional zero-point stability, achieving a 100\% return-to-origin success rate with a minimal mean bias of 0.8039 pixels, even under extreme torsional deformations. In dynamic tasks, SpikingTac limits the obstacle-avoidance overshoot to 6.2~mm, representing a 5-fold performance improvement over conventional frame-based sensors. Furthermore, the sensor achieves sub-millimeter geometric accuracy, with Root Mean Square Error (RMSE) of 0.0952~mm in localization and 0.0452~mm in radius measurement.

