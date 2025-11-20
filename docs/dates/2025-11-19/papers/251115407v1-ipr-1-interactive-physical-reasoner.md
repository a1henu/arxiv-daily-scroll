---
layout: default
title: IPR-1: Interactive Physical Reasoner
---

# IPR-1: Interactive Physical Reasoner
**arXiv**：[2511.15407v1](https://arxiv.org/abs/2511.15407) · [PDF](https://arxiv.org/pdf/2511.15407.pdf)  
**作者**：Mingyu Zhang, Lifeng Zhuo, Tianxi Tan, Guocan Xie, Xian Nie, Yan Li, Renjie Zhao, Zizhu He, Ziyu Wang, Jiting Cai, Yong-Lu Li  

**一句话要点**：提出IPR-1交互物理推理器，通过世界模型与VLM结合提升物理推理能力。

**关键词**：物理推理, 交互学习, 世界模型, 视觉语言模型, 零样本迁移, 游戏环境

## 3 点简述
- 核心问题：现有VLM/VLA和世界模型在交互环境中物理推理存在互补缺陷。
- 方法要点：使用世界模型推演评分强化VLM策略，引入PhysCode对齐语义与动态。
- 实验或效果：在1000+游戏中预训练，性能随经验提升，零样本迁移至未见游戏。

## 摘要（原文）

> Humans learn by observing, interacting with environments, and internalizing physics and causality. Here, we aim to ask whether an agent can similarly acquire human-like reasoning from interaction and keep improving with more experience. We study this in a Game-to-Unseen (G2U) setting, curating 1,000+ heterogeneous games with diverse physical and causal mechanisms, and evaluate at three human-like levels: Survival, Curiosity, Utility, from primitive intuition to goal-driven reasoning. Our analysis reveals complementary failures: VLM/VLA agents reason but lack look-ahead in interactive settings, while world models imagine but imitate visual patterns rather than analyze physics and causality. We therefore propose IPR (Interactive Physical Reasoner), using world-model rollouts to score and reinforce a VLM's policy, and introduce PhysCode, a physics-centric action code aligning semantic intent with dynamics to provide a shared action space for prediction and reasoning. Pretrained on 1,000+ games, our IPR performs robustly on three levels, matches GPT-5 overall, and surpasses it on Curiosity. We find that performance improves with more training games and interaction steps, and that the model also zero-shot transfers to unseen games. These results support physics-centric interaction as a path to steadily improving physical reasoning.

