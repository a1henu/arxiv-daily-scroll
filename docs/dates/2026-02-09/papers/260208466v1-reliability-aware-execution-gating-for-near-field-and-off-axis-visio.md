---
layout: default
title: Reliability-aware Execution Gating for Near-field and Off-axis Vision-guided Robotic Alignment
---

# Reliability-aware Execution Gating for Near-field and Off-axis Vision-guided Robotic Alignment
**arXiv**：[2602.08466v1](https://arxiv.org/abs/2602.08466) · [PDF](https://arxiv.org/pdf/2602.08466.pdf)  
**作者**：Ning Hu, Senhao Cao, Maochen Li  

**一句话要点**：提出可靠性感知执行门控机制，以提升近场和离轴视觉引导机器人对齐的鲁棒性。

**关键词**：视觉引导机器人, 姿态估计, 执行可靠性, 几何误差放大, 近场对齐, 离轴配置

## 3 点简述
- 核心问题：姿态估计精度不足以保证执行可靠性，几何误差放大导致对齐失败。
- 方法要点：在执行层面评估几何一致性和配置风险，选择性拒绝或缩放高风险姿态更新。
- 实验或效果：在UR5机器人平台上验证，显著提高任务成功率，降低执行方差，抑制尾部风险。

## 摘要（原文）

> Vision-guided robotic systems are increasingly deployed in precision alignment tasks that require reliable execution under near-field and off-axis configurations. While recent advances in pose estimation have significantly improved numerical accuracy, practical robotic systems still suffer from frequent execution failures even when pose estimates appear accurate. This gap suggests that pose accuracy alone is insufficient to guarantee execution-level reliability. In this paper, we reveal that such failures arise from a deterministic geometric error amplification mechanism, in which small pose estimation errors are magnified through system structure and motion execution, leading to unstable or failed alignment. Rather than modifying pose estimation algorithms, we propose a Reliability-aware Execution Gating mechanism that operates at the execution level. The proposed approach evaluates geometric consistency and configuration risk before execution, and selectively rejects or scales high-risk pose updates. We validate the proposed method on a real UR5 robotic platform performing single-step visual alignment tasks under varying camera-target distances and off-axis configurations. Experimental results demonstrate that the proposed execution gating significantly improves task success rates, reduces execution variance, and suppresses tail-risk behavior, while leaving average pose accuracy largely unchanged. Importantly, the proposed mechanism is estimator-agnostic and can be readily integrated with both classical geometry-based and learning-based pose estimation pipelines. These results highlight the importance of execution-level reliability modeling and provide a practical solution for improving robustness in near-field vision-guided robotic systems.

