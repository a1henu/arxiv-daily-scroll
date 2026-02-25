---
layout: default
title: Efficient and Explainable End-to-End Autonomous Driving via Masked Vision-Language-Action Diffusion
---

# Efficient and Explainable End-to-End Autonomous Driving via Masked Vision-Language-Action Diffusion
**arXiv**：[2602.20577v1](https://arxiv.org/abs/2602.20577) · [PDF](https://arxiv.org/pdf/2602.20577.pdf)  
**作者**：Jiaru Zhang, Manav Gagvani, Can Cui, Juntong Peng, Ruqi Zhang, Ziran Wang  

**一句话要点**：提出掩码视觉-语言-动作扩散模型以提升端到端自动驾驶的效率和可解释性

**关键词**：自动驾驶规划, 扩散模型, 动作标记化, 几何感知嵌入, 可解释AI

## 3 点简述
- 核心问题：现有LLM/VLM方法在推理延迟、动作精度和可解释性方面存在挑战
- 方法要点：引入离散动作标记化和几何感知嵌入学习，结合动作优先解码策略
- 实验或效果：在nuScenes基准上实现高效规划，超越现有自回归和扩散基线

## 摘要（原文）

> Large Language Models (LLMs) and Vision-Language Models (VLMs) have emerged as promising candidates for end-to-end autonomous driving. However, these models typically face challenges in inference latency, action precision, and explainability. Existing autoregressive approaches struggle with slow token-by-token generation, while prior diffusion-based planners often rely on verbose, general-purpose language tokens that lack explicit geometric structure. In this work, we propose Masked Vision-Language-Action Diffusion for Autonomous Driving (MVLAD-AD), a novel framework designed to bridge the gap between efficient planning and semantic explainability via a masked vision-language-action diffusion model. Unlike methods that force actions into the language space, we introduce a discrete action tokenization strategy that constructs a compact codebook of kinematically feasible waypoints from real-world driving distributions. Moreover, we propose geometry-aware embedding learning to ensure that embeddings in the latent space approximate physical geometric metrics. Finally, an action-priority decoding strategy is introduced to prioritize trajectory generation. Extensive experiments on nuScenes and derived benchmarks demonstrate that MVLAD-AD achieves superior efficiency and outperforms state-of-the-art autoregressive and diffusion baselines in planning precision, while providing high-fidelity and explainable reasoning.

