---
layout: default
title: RESBev: Making BEV Perception More Robust
---

# RESBev: Making BEV Perception More Robust
**arXiv**：[2603.09529v1](https://arxiv.org/abs/2603.09529) · [PDF](https://arxiv.org/pdf/2603.09529.pdf)  
**作者**：Lifeng Zhuo, Kefan Jin, Zhe Liu, Hesheng Wang  

**一句话要点**：提出RESBev方法以增强BEV感知在传感器退化和对抗攻击下的鲁棒性

**关键词**：BEV感知, 鲁棒性增强, 潜在世界模型, 传感器退化, 对抗攻击, 自动驾驶

## 3 点简述
- 核心问题：BEV感知在真实部署中面临传感器退化和对抗攻击，导致感知异常和安全风险
- 方法要点：将感知鲁棒性重构为潜在语义预测问题，构建潜在世界模型学习BEV状态转移以恢复特征
- 实验或效果：在nuScenes数据集上，RESBev通过少样本微调显著提升现有BEV模型对多种干扰的鲁棒性

## 摘要（原文）

> Bird's-eye-view (BEV) perception has emerged as a cornerstone of autonomous driving systems, providing a structured, ego-centric representation critical for downstream planning and control. However, real-world deployment faces challenges from sensor degradation and adversarial attacks, which can cause severe perceptual anomalies and ultimately compromise the safety of autonomous driving systems. To address this, we propose a resilient and plug-and-play BEV perception method, RESBev, which can be easily applied to existing BEV perception methods to enhance their robustness to diverse disturbances. Specifically, we reframe perception robustness as a latent semantic prediction problem. A latent world model is constructed to extract spatiotemporal correlations across sequential BEV observations, thereby learning the underlying BEV state transitions to predict clean BEV features for reconstructing corrupted observations. The proposed framework operates at the semantic feature level of the Lift-Splat-Shoot pipeline, enabling recovery that generalizes across both natural disturbances and adversarial attacks without modifying the underlying backbone. Extensive experiments on the nuScenes dataset demonstrate that, with few-shot fine-tuning, RESBev significantly improves the robustness of existing BEV perception models against various external disturbances and adversarial attacks.

