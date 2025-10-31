---
layout: default
title: Clone Deterministic 3D Worlds with Geometrically-Regularized World Models
---

# Clone Deterministic 3D Worlds with Geometrically-Regularized World Models
**arXiv**：[2510.26782v1](https://arxiv.org/abs/2510.26782) · [PDF](https://arxiv.org/pdf/2510.26782.pdf)  
**作者**：Zaishuo Xia, Yukuan Lu, Xinyi Li, Yifan Xu, Yubei Chen  

**一句话要点**：提出几何正则化世界模型以提升确定性3D世界克隆与长期预测能力

**关键词**：世界模型, 几何正则化, 表示学习, 长期预测, 3D环境克隆

## 3 点简述
- 核心问题：当前世界模型在长期预测中表现脆弱，源于表示质量差和潜在空间纠缠
- 方法要点：通过几何正则化强制潜在空间中相邻轨迹点接近，改善表示学习
- 实验或效果：在确定性3D场景中显著提高预测保真度和稳定性，支持长时程推理

## 摘要（原文）

> A world model is an internal model that simulates how the world evolves.
> Given past observations and actions, it predicts the future of both the
> embodied agent and its environment. Accurate world models are essential for
> enabling agents to think, plan, and reason effectively in complex, dynamic
> settings. Despite rapid progress, current world models remain brittle and
> degrade over long horizons. We argue that a central cause is representation
> quality: exteroceptive inputs (e.g., images) are high-dimensional, and lossy or
> entangled latents make dynamics learning unnecessarily hard. We therefore ask
> whether improving representation learning alone can substantially improve
> world-model performance. In this work, we take a step toward building a truly
> accurate world model by addressing a fundamental yet open problem: constructing
> a model that can fully clone and overfit to a deterministic 3D world. We
> propose Geometrically-Regularized World Models (GRWM), which enforces that
> consecutive points along a natural sensory trajectory remain close in latent
> representation space. This approach yields significantly improved latent
> representations that align closely with the true topology of the environment.
> GRWM is plug-and-play, requires only minimal architectural modification, scales
> with trajectory length, and is compatible with diverse latent generative
> backbones. Across deterministic 3D settings and long-horizon prediction tasks,
> GRWM significantly increases rollout fidelity and stability. Analyses show that
> its benefits stem from learning a latent manifold with superior geometric
> structure. These findings support a clear takeaway: improving representation
> learning is a direct and useful path to robust world models, delivering
> reliable long-horizon predictions without enlarging the dynamics module.

