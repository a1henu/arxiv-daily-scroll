---
layout: default
title: Conditional Flow Matching for Continuous Anomaly Detection in Autonomous Driving on a Manifold-Aware Spectral Space
---

# Conditional Flow Matching for Continuous Anomaly Detection in Autonomous Driving on a Manifold-Aware Spectral Space
**arXiv**：[2602.17586v1](https://arxiv.org/abs/2602.17586) · [PDF](https://arxiv.org/pdf/2602.17586.pdf)  
**作者**：Antonio Guillen-Perez  

**一句话要点**：提出Deep-Flow框架，利用条件流匹配在谱空间进行连续异常检测，以解决自动驾驶中长尾场景的安全验证瓶颈。

**关键词**：自动驾驶安全验证, 条件流匹配, 谱流形, 异常检测, 最优传输, Transformer编码器

## 3 点简述
- 核心问题：自动驾驶安全验证受限于传统规则方法难以检测罕见高风险长尾场景。
- 方法要点：采用最优传输条件流匹配在低秩谱流形上建模驾驶行为概率密度，结合Transformer编码器处理多模态歧义。
- 实验或效果：在Waymo数据集上AUC-ROC达0.766，揭示运动危险与语义违规的根本区别，识别传统方法忽略的异常行为。

## 摘要（原文）

> Safety validation for Level 4 autonomous vehicles (AVs) is currently bottlenecked by the inability to scale the detection of rare, high-risk long-tail scenarios using traditional rule-based heuristics. We present Deep-Flow, an unsupervised framework for safety-critical anomaly detection that utilizes Optimal Transport Conditional Flow Matching (OT-CFM) to characterize the continuous probability density of expert human driving behavior. Unlike standard generative approaches that operate in unstable, high-dimensional coordinate spaces, Deep-Flow constrains the generative process to a low-rank spectral manifold via a Principal Component Analysis (PCA) bottleneck. This ensures kinematic smoothness by design and enables the computation of the exact Jacobian trace for numerically stable, deterministic log-likelihood estimation. To resolve multi-modal ambiguity at complex junctions, we utilize an Early Fusion Transformer encoder with lane-aware goal conditioning, featuring a direct skip-connection to the flow head to maintain intent-integrity throughout the network. We introduce a kinematic complexity weighting scheme that prioritizes high-energy maneuvers (quantified via path tortuosity and jerk) during the simulation-free training process. Evaluated on the Waymo Open Motion Dataset (WOMD), our framework achieves an AUC-ROC of 0.766 against a heuristic golden set of safety-critical events. More significantly, our analysis reveals a fundamental distinction between kinematic danger and semantic non-compliance. Deep-Flow identifies a critical predictability gap by surfacing out-of-distribution behaviors, such as lane-boundary violations and non-normative junction maneuvers, that traditional safety filters overlook. This work provides a mathematically rigorous foundation for defining statistical safety gates, enabling objective, data-driven validation for the safe deployment of autonomous fleets.

