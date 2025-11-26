---
layout: default
title: Flash-DMD: Towards High-Fidelity Few-Step Image Generation with Efficient Distillation and Joint Reinforcement Learning
---

# Flash-DMD: Towards High-Fidelity Few-Step Image Generation with Efficient Distillation and Joint Reinforcement Learning
**arXiv**：[2511.20549v1](https://arxiv.org/abs/2511.20549) · [PDF](https://arxiv.org/pdf/2511.20549.pdf)  
**作者**：Guanjie Chen, Shirui Huang, Kai Liu, Jianchen Zhu, Xiaoye Qu, Peng Chen, Yu Cheng, Yifu Sun  

**一句话要点**：提出Flash-DMD框架，通过高效蒸馏与联合强化学习实现高保真少步图像生成

**关键词**：图像生成, 扩散模型, 时间步蒸馏, 强化学习, 模型加速, 高保真生成

## 3 点简述
- 扩散模型迭代采样计算成本高，蒸馏加速易导致图像质量下降和训练不稳定
- 采用时间步感知蒸馏策略降低训练成本，联合强化学习微调以稳定优化过程
- 实验显示在少步采样中收敛更快，生成质量优于现有方法，提升视觉和文本对齐指标

## 摘要（原文）

> Diffusion Models have emerged as a leading class of generative models, yet their iterative sampling process remains computationally expensive. Timestep distillation is a promising technique to accelerate generation, but it often requires extensive training and leads to image quality degradation. Furthermore, fine-tuning these distilled models for specific objectives, such as aesthetic appeal or user preference, using Reinforcement Learning (RL) is notoriously unstable and easily falls into reward hacking. In this work, we introduce Flash-DMD, a novel framework that enables fast convergence with distillation and joint RL-based refinement. Specifically, we first propose an efficient timestep-aware distillation strategy that significantly reduces training cost with enhanced realism, outperforming DMD2 with only $2.1\%$ its training cost. Second, we introduce a joint training scheme where the model is fine-tuned with an RL objective while the timestep distillation training continues simultaneously. We demonstrate that the stable, well-defined loss from the ongoing distillation acts as a powerful regularizer, effectively stabilizing the RL training process and preventing policy collapse. Extensive experiments on score-based and flow matching models show that our proposed Flash-DMD not only converges significantly faster but also achieves state-of-the-art generation quality in the few-step sampling regime, outperforming existing methods in visual quality, human preference, and text-image alignment metrics. Our work presents an effective paradigm for training efficient, high-fidelity, and stable generative models. Codes are coming soon.

