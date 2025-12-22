---
layout: default
title: On Using Neural Networks to Learn Safety Speed Reduction in Human-Robot Collaboration: A Comparative Analysis
---

# On Using Neural Networks to Learn Safety Speed Reduction in Human-Robot Collaboration: A Comparative Analysis
**arXiv**：[2512.17579v1](https://arxiv.org/abs/2512.17579) · [PDF](https://arxiv.org/pdf/2512.17579.pdf)  
**作者**：Marco Faroni, Alessio Spanò, Andrea M. Zanchettin, Paolo Rocco  

**一句话要点**：提出基于深度学习的机器人安全减速预测方法，以优化人机协作中的周期时间估计与调度效率

**关键词**：人机协作, 安全减速预测, 深度学习, 周期时间估计, 调度优化, 神经网络

## 3 点简述
- 核心问题：人机协作中安全机制导致机器人减速，使周期时间估计困难并影响调度效率。
- 方法要点：使用神经网络直接从过程执行数据预测机器人安全缩放因子，分析多种架构。
- 实验或效果：证明简单前馈网络能有效估计减速，提升周期时间预测和调度算法设计。

## 摘要（原文）

> In Human-Robot Collaboration, safety mechanisms such as Speed and Separation Monitoring and Power and Force Limitation dynamically adjust the robot's speed based on human proximity. While essential for risk reduction, these mechanisms introduce slowdowns that makes cycle time estimation a hard task and impact job scheduling efficiency. Existing methods for estimating cycle times or designing schedulers often rely on predefined safety models, which may not accurately reflect real-world safety implementations, as these depend on case-specific risk assessments. In this paper, we propose a deep learning approach to predict the robot's safety scaling factor directly from process execution data. We analyze multiple neural network architectures and demonstrate that a simple feed-forward network effectively estimates the robot's slowdown. This capability is crucial for improving cycle time predictions and designing more effective scheduling algorithms in collaborative robotic environments.

