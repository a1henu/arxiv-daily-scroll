---
layout: default
title: RoboPocket: Improve Robot Policies Instantly with Your Phone
---

# RoboPocket: Improve Robot Policies Instantly with Your Phone
**arXiv**：[2603.05504v1](https://arxiv.org/abs/2603.05504) · [PDF](https://arxiv.org/pdf/2603.05504.pdf)  
**作者**：Junjie Fang, Wendi Chen, Han Xue, Fangyuan Zhou, Tian Le, Yi Wang, Yuting Zhang, Jun Lv, Chuan Wen, Cewu Lu  

**一句话要点**：提出RoboPocket系统，利用智能手机实现无机器人即时策略迭代以提升模仿学习效率

**关键词**：模仿学习, 增强现实, 远程推断, 在线微调, 数据效率, 策略迭代

## 3 点简述
- 核心问题：模仿学习数据收集效率低，手持设备采集数据为开环，无法针对策略弱点优化
- 方法要点：通过AR视觉预测远程推断策略轨迹，使收集者能主动识别失败并聚焦弱区域数据收集
- 实验或效果：实验显示RoboPocket遵循数据缩放定律，数据效率比离线策略翻倍，样本效率提升达2倍

## 摘要（原文）

> Scaling imitation learning is fundamentally constrained by the efficiency of data collection. While handheld interfaces have emerged as a scalable solution for in-the-wild data acquisition, they predominantly operate in an open-loop manner: operators blindly collect demonstrations without knowing the underlying policy's weaknesses, leading to inefficient coverage of critical state distributions. Conversely, interactive methods like DAgger effectively address covariate shift but rely on physical robot execution, which is costly and difficult to scale. To reconcile this trade-off, we introduce RoboPocket, a portable system that enables Robot-Free Instant Policy Iteration using single consumer smartphones. Its core innovation is a Remote Inference framework that visualizes the policy's predicted trajectory via Augmented Reality (AR) Visual Foresight. This immersive feedback allows collectors to proactively identify potential failures and focus data collection on the policy's weak regions without requiring a physical robot. Furthermore, we implement an asynchronous Online Finetuning pipeline that continuously updates the policy with incoming data, effectively closing the learning loop in minutes. Extensive experiments demonstrate that RoboPocket adheres to data scaling laws and doubles the data efficiency compared to offline scaling strategies, overcoming their long-standing efficiency bottleneck. Moreover, our instant iteration loop also boosts sample efficiency by up to 2$\times$ in distributed environments a small number of interactive corrections per person. Project page and videos: https://robo-pocket.github.io.

