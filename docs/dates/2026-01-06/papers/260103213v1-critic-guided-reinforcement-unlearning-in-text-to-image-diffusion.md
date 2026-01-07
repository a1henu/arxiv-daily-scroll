---
layout: default
title: Critic-Guided Reinforcement Unlearning in Text-to-Image Diffusion
---

# Critic-Guided Reinforcement Unlearning in Text-to-Image Diffusion
**arXiv**：[2601.03213v1](https://arxiv.org/abs/2601.03213) · [PDF](https://arxiv.org/pdf/2601.03213.pdf)  
**作者**：Mykola Vysotskyi, Zahar Kohut, Mariia Shpir, Taras Rumezhak, Volodymyr Karpiv  

**一句话要点**：提出基于评论家引导的强化学习框架，用于文本到图像扩散模型的概念遗忘。

**关键词**：文本到图像扩散, 强化学习, 概念遗忘, 评论家网络, 噪声潜在空间, 策略梯度优化

## 3 点简述
- 核心问题：现有扩散模型遗忘方法依赖监督权重编辑或全局惩罚，强化学习方法更新方差高、信用分配弱。
- 方法要点：将去噪视为序列决策过程，引入时间步感知评论家，基于噪声潜在空间计算每步奖励以优化策略梯度。
- 实验或效果：在多个概念上实现优于或可比基线遗忘效果，保持图像质量和良性提示保真度，代码开源促进可复现性。

## 摘要（原文）

> Machine unlearning in text-to-image diffusion models aims to remove targeted concepts while preserving overall utility. Prior diffusion unlearning methods typically rely on supervised weight edits or global penalties; reinforcement-learning (RL) approaches, while flexible, often optimize sparse end-of-trajectory rewards, yielding high-variance updates and weak credit assignment. We present a general RL framework for diffusion unlearning that treats denoising as a sequential decision process and introduces a timestep-aware critic with noisy-step rewards. Concretely, we train a CLIP-based reward predictor on noisy latents and use its per-step signal to compute advantage estimates for policy-gradient updates of the reverse diffusion kernel. Our algorithm is simple to implement, supports off-policy reuse, and plugs into standard text-to-image backbones. Across multiple concepts, the method achieves better or comparable forgetting to strong baselines while maintaining image quality and benign prompt fidelity; ablations show that (i) per-step critics and (ii) noisy-conditioned rewards are key to stability and effectiveness. We release code and evaluation scripts to facilitate reproducibility and future research on RL-based diffusion unlearning.

