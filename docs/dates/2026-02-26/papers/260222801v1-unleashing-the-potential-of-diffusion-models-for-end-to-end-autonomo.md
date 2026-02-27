---
layout: default
title: Unleashing the Potential of Diffusion Models for End-to-End Autonomous Driving
---

# Unleashing the Potential of Diffusion Models for End-to-End Autonomous Driving
**arXiv**：[2602.22801v1](https://arxiv.org/abs/2602.22801) · [PDF](https://arxiv.org/pdf/2602.22801.pdf)  
**作者**：Yinan Zheng, Tianyi Tan, Bin Huang, Enguang Liu, Ruiming Liang, Jianlin Zhang, Jianwei Cui, Guang Chen, Kun Ma, Hangjun Ye, Long Chen, Ya-Qin Zhang, Xianyuan Zhan, Jingjing Liu  

**一句话要点**：提出Hyper Diffusion Planner以解决端到端自动驾驶在真实世界中的规划问题

**关键词**：扩散模型, 端到端自动驾驶, 轨迹规划, 实车测试, 强化学习后训练

## 3 点简述
- 核心问题：扩散模型在真实世界端到端自动驾驶中的应用与评估有限，潜力未充分挖掘
- 方法要点：基于大量实车数据，系统研究扩散损失空间、轨迹表示和数据缩放对规划性能的影响
- 实验或效果：部署于实车平台，在6个城市场景和200公里测试中，性能比基础模型提升10倍

## 摘要（原文）

> Diffusion models have become a popular choice for decision-making tasks in robotics, and more recently, are also being considered for solving autonomous driving tasks. However, their applications and evaluations in autonomous driving remain limited to simulation-based or laboratory settings. The full strength of diffusion models for large-scale, complex real-world settings, such as End-to-End Autonomous Driving (E2E AD), remains underexplored. In this study, we conducted a systematic and large-scale investigation to unleash the potential of the diffusion models as planners for E2E AD, based on a tremendous amount of real-vehicle data and road testing. Through comprehensive and carefully controlled studies, we identify key insights into the diffusion loss space, trajectory representation, and data scaling that significantly impact E2E planning performance. Moreover, we also provide an effective reinforcement learning post-training strategy to further enhance the safety of the learned planner. The resulting diffusion-based learning framework, Hyper Diffusion Planner} (HDP), is deployed on a real-vehicle platform and evaluated across 6 urban driving scenarios and 200 km of real-world testing, achieving a notable 10x performance improvement over the base model. Our work demonstrates that diffusion models, when properly designed and trained, can serve as effective and scalable E2E AD planners for complex, real-world autonomous driving tasks.

