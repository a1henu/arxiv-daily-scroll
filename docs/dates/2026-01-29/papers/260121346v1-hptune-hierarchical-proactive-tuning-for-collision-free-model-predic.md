---
layout: default
title: HPTune: Hierarchical Proactive Tuning for Collision-Free Model Predictive Control
---

# HPTune: Hierarchical Proactive Tuning for Collision-Free Model Predictive Control
**arXiv**：[2601.21346v1](https://arxiv.org/abs/2601.21346) · [PDF](https://arxiv.org/pdf/2601.21346.pdf)  
**作者**：Wei Zuo, Chengyang Li, Yikun Wang, Bingyang Cheng, Zeyi Ren, Shuai Wang, Derrick Wing Kwan Ng, Yik-Chung Wu  

**一句话要点**：提出分层主动调优框架HPTune，以解决模型预测控制中参数调优因失败事件稀疏而低效的问题。

**关键词**：模型预测控制, 参数调优, 避障规划, 分层优化, 主动学习, 多普勒激光雷达

## 3 点简述
- 现有MPC参数调优方法仅评估已执行动作，导致因碰撞等失败事件稀疏而更新效率低下。
- HPTune通过评估未执行动作，结合快速级（基于预测接近指标）和慢速级（基于闭环反向传播损失）调优。
- 高保真模拟实验显示HPTune在复杂环境中实现高效调优，优于基线方案，支持安全敏捷的避障规划。

## 摘要（原文）

> Parameter tuning is a powerful approach to enhance adaptability in model predictive control (MPC) motion planners. However, existing methods typically operate in a myopic fashion that only evaluates executed actions, leading to inefficient parameter updates due to the sparsity of failure events (e.g., obstacle nearness or collision). To cope with this issue, we propose to extend evaluation from executed to non-executed actions, yielding a hierarchical proactive tuning (HPTune) framework that combines both a fast-level tuning and a slow-level tuning. The fast one adopts risk indicators of predictive closing speed and predictive proximity distance, and the slow one leverages an extended evaluation loss for closed-loop backpropagation. Additionally, we integrate HPTune with the Doppler LiDAR that provides obstacle velocities apart from position-only measurements for enhanced motion predictions, thus facilitating the implementation of HPTune. Extensive experiments on high-fidelity simulator demonstrate that HPTune achieves efficient MPC tuning and outperforms various baseline schemes in complex environments. It is found that HPTune enables situation-tailored motion planning by formulating a safe, agile collision avoidance strategy.

