---
layout: default
title: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation
---

# General Humanoid Whole-Body Control via Pretraining and Fast Adaptation
**arXiv**：[2602.11929v1](https://arxiv.org/abs/2602.11929) · [PDF](https://arxiv.org/pdf/2602.11929.pdf)  
**作者**：Zepeng Wang, Jiangxing Wang, Shiqing Yao, Yu Zhang, Ziluo Ding, Ming Yang, Yuxuan Wang, Haobin Jiang, Chao Ma, Xiaochuan Shi, Zongqing Lu  

**一句话要点**：提出FAST框架，通过预训练与快速适应实现通用人形机器人全身控制

**关键词**：人形机器人控制, 快速适应, 全身运动跟踪, 平衡增强, 残差策略学习

## 3 点简述
- 核心问题：人形机器人全身控制面临运动分布多样、快速适应难和高动态场景平衡挑战
- 方法要点：引入Parseval引导残差策略适应，在正交性和KL约束下学习轻量增量动作策略
- 实验或效果：仿真和真实部署实验显示，FAST在鲁棒性、适应效率和泛化性上优于基线

## 摘要（原文）

> Learning a general whole-body controller for humanoid robots remains challenging due to the diversity of motion distributions, the difficulty of fast adaptation, and the need for robust balance in high-dynamic scenarios. Existing approaches often require task-specific training or suffer from performance degradation when adapting to new motions. In this paper, we present FAST, a general humanoid whole-body control framework that enables Fast Adaptation and Stable Motion Tracking. FAST introduces Parseval-Guided Residual Policy Adaptation, which learns a lightweight delta action policy under orthogonality and KL constraints, enabling efficient adaptation to out-of-distribution motions while mitigating catastrophic forgetting. To further improve physical robustness, we propose Center-of-Mass-Aware Control, which incorporates CoM-related observations and objectives to enhance balance when tracking challenging reference motions. Extensive experiments in simulation and real-world deployment demonstrate that FAST consistently outperforms state-of-the-art baselines in robustness, adaptation efficiency, and generalization.

