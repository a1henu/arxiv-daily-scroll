---
layout: default
title: Robust and Generalized Humanoid Motion Tracking
---

# Robust and Generalized Humanoid Motion Tracking
**arXiv**：[2601.23080v1](https://arxiv.org/abs/2601.23080) · [PDF](https://arxiv.org/pdf/2601.23080.pdf)  
**作者**：Yubiao Ma, Han Yu, Jiayin Xie, Changtai Lv, Qiang Luo, Chi Zhang, Yunpeng Yin, Boyang Xing, Xuemei Ren, Dongdong Zheng  

**一句话要点**：提出基于动力学条件命令聚合的框架，以解决人形机器人全身运动跟踪中的噪声和漂移问题。

**关键词**：人形机器人控制, 运动跟踪, 动力学建模, 鲁棒性训练, 仿真到现实迁移, 端到端学习

## 3 点简述
- 核心问题：参考运动在机器人域中可能包含噪声和不一致，闭环执行会放大局部缺陷，导致动态和接触丰富行为中的漂移或失败。
- 方法要点：使用因果时序编码器总结近期本体感知，并通过多头交叉注意力命令编码器基于当前动力学选择性聚合上下文窗口，集成跌倒恢复课程和退火向上辅助力。
- 实验或效果：仅需约3.5小时运动数据，支持单阶段端到端训练，在多样参考输入和挑战性运动体制下评估，展示零样本迁移和鲁棒的仿真到现实迁移。

## 摘要（原文）

> Learning a general humanoid whole-body controller is challenging because practical reference motions can exhibit noise and inconsistencies after being transferred to the robot domain, and local defects may be amplified by closed-loop execution, causing drift or failure in highly dynamic and contact-rich behaviors. We propose a dynamics-conditioned command aggregation framework that uses a causal temporal encoder to summarize recent proprioception and a multi-head cross-attention command encoder to selectively aggregate a context window based on the current dynamics. We further integrate a fall recovery curriculum with random unstable initialization and an annealed upward assistance force to improve robustness and disturbance rejection. The resulting policy requires only about 3.5 hours of motion data and supports single-stage end-to-end training without distillation. The proposed method is evaluated under diverse reference inputs and challenging motion regimes, demonstrating zero-shot transfer to unseen motions as well as robust sim-to-real transfer on a physical humanoid robot.

