---
layout: default
title: SeedPolicy: Horizon Scaling via Self-Evolving Diffusion Policy for Robot Manipulation
---

# SeedPolicy: Horizon Scaling via Self-Evolving Diffusion Policy for Robot Manipulation
**arXiv**：[2603.05117v1](https://arxiv.org/abs/2603.05117) · [PDF](https://arxiv.org/pdf/2603.05117.pdf)  
**作者**：Youqiang Gui, Yuxuan Zhou, Shen Cheng, Xinyang Yuan, Haoqiang Fan, Peng Cheng, Shuaicheng Liu  

**一句话要点**：提出SeedPolicy，通过自演化门控注意力解决扩散策略在长时程机器人操作中的性能下降问题。

**关键词**：机器人操作, 模仿学习, 扩散策略, 长时程建模, 门控注意力, 自演化机制

## 3 点简述
- 扩散策略在多模态专家行为建模中，随观察时程增加性能下降，限制长时程操作。
- 引入自演化门控注意力模块，通过门控注意力维护时变潜在状态，压缩长时程观测并过滤无关信息。
- 在RoboTwin 2.0基准测试中，SeedPolicy优于扩散策略及其他模仿学习基线，参数效率高。

## 摘要（原文）

> Imitation Learning (IL) enables robots to acquire manipulation skills from expert demonstrations. Diffusion Policy (DP) models multi-modal expert behaviors but suffers performance degradation as observation horizons increase, limiting long-horizon manipulation. We propose Self-Evolving Gated Attention (SEGA), a temporal module that maintains a time-evolving latent state via gated attention, enabling efficient recurrent updates that compress long-horizon observations into a fixed-size representation while filtering irrelevant temporal information. Integrating SEGA into DP yields Self-Evolving Diffusion Policy (SeedPolicy), which resolves the temporal modeling bottleneck and enables scalable horizon extension with moderate overhead. On the RoboTwin 2.0 benchmark with 50 manipulation tasks, SeedPolicy outperforms DP and other IL baselines. Averaged across both CNN and Transformer backbones, SeedPolicy achieves 36.8% relative improvement in clean settings and 169% relative improvement in randomized challenging settings over the DP. Compared to vision-language-action models such as RDT with 1.2B parameters, SeedPolicy achieves competitive performance with one to two orders of magnitude fewer parameters, demonstrating strong efficiency and scalability. These results establish SeedPolicy as a state-of-the-art imitation learning method for long-horizon robotic manipulation. Code is available at: https://github.com/Youqiang-Gui/SeedPolicy.

