---
layout: default
title: AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion
---

# AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion
**arXiv**：[2511.18857v1](https://arxiv.org/abs/2511.18857) · [PDF](https://arxiv.org/pdf/2511.18857.pdf)  
**作者**：Changsheng Luo, Yushi Wang, Wenhan Cai, Mingguo Zhao  

**一句话要点**：提出AutoOdom自回归本体感知里程计，解决腿式机器人在GPS缺失和视觉退化环境中的定位问题

**关键词**：腿式机器人定位, 自回归学习, 仿真到现实迁移, 本体感知里程计, 两阶段训练, 传感器模态选择

## 3 点简述
- 核心问题：传统里程计在GPS缺失和视觉退化环境中失效，现有方法存在建模不确定性、仿真到现实差距和漂移问题
- 方法要点：采用两阶段训练，先仿真学习非线性动态和接触状态，再自回归增强以弥合仿真到现实差距
- 实验或效果：在Booster T1人形机器人上验证，绝对轨迹误差等指标显著优于基线方法，提升达57.2%

## 摘要（原文）

> Accurate proprioceptive odometry is fundamental for legged robot navigation in GPS-denied and visually degraded environments where conventional visual odometry systems fail. Current approaches face critical limitations: analytical filtering methods suffer from modeling uncertainties and cumulative drift, hybrid learning-filtering approaches remain constrained by their analytical components, while pure learning-based methods struggle with simulation-to-reality transfer and demand extensive real-world data collection. This paper introduces AutoOdom, a novel autoregressive proprioceptive odometry system that overcomes these challenges through an innovative two-stage training paradigm. Stage 1 employs large-scale simulation data to learn complex nonlinear dynamics and rapidly changing contact states inherent in legged locomotion, while Stage 2 introduces an autoregressive enhancement mechanism using limited real-world data to effectively bridge the sim-to-real gap. The key innovation lies in our autoregressive training approach, where the model learns from its own predictions to develop resilience against sensor noise and improve robustness in highly dynamic environments. Comprehensive experimental validation on the Booster T1 humanoid robot demonstrates that AutoOdom significantly outperforms state-of-the-art methods across all evaluation metrics, achieving 57.2% improvement in absolute trajectory error, 59.2% improvement in Umeyama-aligned error, and 36.2% improvement in relative pose error compared to the Legolas baseline. Extensive ablation studies provide critical insights into sensor modality selection and temporal modeling, revealing counterintuitive findings about IMU acceleration data and validating our systematic design choices for robust proprioceptive odometry in challenging locomotion scenarios.

