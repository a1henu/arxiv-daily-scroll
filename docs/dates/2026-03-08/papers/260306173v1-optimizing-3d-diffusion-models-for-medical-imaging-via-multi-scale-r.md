---
layout: default
title: Optimizing 3D Diffusion Models for Medical Imaging via Multi-Scale Reward Learning
---

# Optimizing 3D Diffusion Models for Medical Imaging via Multi-Scale Reward Learning
**arXiv**：[2603.06173v1](https://arxiv.org/abs/2603.06173) · [PDF](https://arxiv.org/pdf/2603.06173.pdf)  
**作者**：Yueying Tian, Xudong Han, Meng Zhou, Rodrigo Aviles-Espinosa, Rupert Young, Philip Birch  

**一句话要点**：提出基于多尺度奖励学习的强化学习优化方法，以提升3D扩散模型在医学影像生成中的临床相关性。

**关键词**：3D扩散模型, 强化学习优化, 医学影像生成, 多尺度奖励学习, 临床相关性提升

## 3 点简述
- 核心问题：标准训练目标与临床需求间的差距限制了3D扩散模型在医学影像生成中的应用。
- 方法要点：先预训练3D扩散模型，再通过PPO和多尺度奖励系统（结合2D切片与3D体积评估）进行微调。
- 实验或效果：在BraTS 2019和OASIS-1数据集上验证，FID显著改善，合成数据在下游分类任务中表现更优。

## 摘要（原文）

> Diffusion models have emerged as powerful tools for 3D medical image generation, yet bridging the gap between standard training objectives and clinical relevance remains a challenge. This paper presents a method to enhance 3D diffusion models using Reinforcement Learning (RL) with multi-scale feedback. We first pretrain a 3D diffusion model on MRI volumes to establish a robust generative prior. Subsequently, we fine-tune the model using Proximal Policy Optimization (PPO), guided by a novel reward system that integrates both 2D slice-wise assessments and 3D volumetric analysis. This combination allows the model to simultaneously optimize for local texture details and global structural coherence. We validate our framework on the BraTS 2019 and OASIS-1 datasets. Our results indicate that incorporating RL feedback effectively steers the generation process toward higher quality distributions. Quantitative analysis reveals significant improvements in Fréchet Inception Distance (FID) and, crucially, the synthetic data demonstrates enhanced utility in downstream tumor and disease classification tasks compared to non-optimized baselines.

