---
layout: default
title: Gaussian Mixture-Based Inverse Perception Contract for Uncertainty-Aware Robot Navigation
---

# Gaussian Mixture-Based Inverse Perception Contract for Uncertainty-Aware Robot Navigation
**arXiv**：[2603.04329v1](https://arxiv.org/abs/2603.04329) · [PDF](https://arxiv.org/pdf/2603.04329.pdf)  
**作者**：Bingyao Du, Joonkyung Kim, Yiwei Lyu  

**一句话要点**：提出高斯混合逆感知契约以解决机器人导航中感知不确定性建模不足的问题

**关键词**：机器人导航, 感知不确定性, 高斯混合模型, 逆感知契约, 安全控制, 多模态误差

## 3 点简述
- 现有逆感知契约使用单椭球集表示不确定性，无法捕捉多模态误差结构，导致保守导航
- GM-IPC基于高斯混合模型，用椭球集并集表示不确定性，支持细粒度、多模态和非凸误差建模
- 学习框架确保集合有效性和紧凑性，实验表明能实现实时安全导航，减少保守性

## 摘要（原文）

> Reliable navigation in cluttered environments requires perception outputs that are not only accurate but also equipped with uncertainty sets suitable for safe control. An inverse perception contract (IPC) provides such a connection by mapping perceptual estimates to sets that contain the ground truth with high confidence. Existing IPC formulations, however, instantiate uncertainty as a single ellipsoidal set and rely on deterministic trust scores to guide robot motion. Such a representation cannot capture the multi-modal and irregular structure of fine-grained perception errors, often resulting in over-conservative sets and degraded navigation performance. In this work, we introduce Gaussian Mixture-based Inverse Perception Contract (GM-IPC), which extends IPC to represent uncertainty with unions of ellipsoidal confidence sets derived from Gaussian mixture models. This design moves beyond deterministic single-set abstractions, enabling fine-grained, multi-modal, and non-convex error structures to be captured with formal guarantees. A learning framework is presented that trains GM-IPC to account for probabilistic inclusion, distribution matching, and empty-space penalties, ensuring both validity and compactness of the predicted sets. We further show that the resulting uncertainty characterizations can be leveraged in downstream planning frameworks for real-time safe navigation, enabling less conservative and more adaptive robot motion while preserving safety in a probabilistic manner.

