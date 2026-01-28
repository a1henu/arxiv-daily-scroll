---
layout: default
title: Structure-based RNA Design by Step-wise Optimization of Latent Diffusion Model
---

# Structure-based RNA Design by Step-wise Optimization of Latent Diffusion Model
**arXiv**：[2601.19232v1](https://arxiv.org/abs/2601.19232) · [PDF](https://arxiv.org/pdf/2601.19232.pdf)  
**作者**：Qi Si, Xuyang Liu, Penglei Wang, Xin Guo, Yuan Qi, Yuan Cheng  

**一句话要点**：提出SOLD框架，通过强化学习优化潜在扩散模型，以解决RNA逆折叠中结构目标优化难题。

**关键词**：RNA逆折叠, 潜在扩散模型, 强化学习, 结构优化, 序列设计

## 3 点简述
- 核心问题：现有RNA逆折叠方法难以优化非可微结构目标，如二级结构一致性和局部距离差异。
- 方法要点：结合潜在扩散模型与强化学习，单步优化噪声，高效处理多结构目标。
- 实验或效果：SOLD在各项指标上超越基线方法和先进方法，提升结构准确性。

## 摘要（原文）

> RNA inverse folding, designing sequences to form specific 3D structures, is critical for therapeutics, gene regulation, and synthetic biology. Current methods, focused on sequence recovery, struggle to address structural objectives like secondary structure consistency (SS), minimum free energy (MFE), and local distance difference test (LDDT), leading to suboptimal structural accuracy. To tackle this, we propose a reinforcement learning (RL) framework integrated with a latent diffusion model (LDM). Drawing inspiration from the success of diffusion models in RNA inverse folding, which adeptly model complex sequence-structure interactions, we develop an LDM incorporating pre-trained RNA-FM embeddings from a large-scale RNA model. These embeddings capture co-evolutionary patterns, markedly improving sequence recovery accuracy. However, existing approaches, including diffusion-based methods, cannot effectively handle non-differentiable structural objectives. By contrast, RL excels in this task by using policy-driven reward optimization to navigate complex, non-gradient-based objectives, offering a significant advantage over traditional methods. In summary, we propose the Step-wise Optimization of Latent Diffusion Model (SOLD), a novel RL framework that optimizes single-step noise without sampling the full diffusion trajectory, achieving efficient refinement of multiple structural objectives. Experimental results demonstrate SOLD surpasses its LDM baseline and state-of-the-art methods across all metrics, establishing a robust framework for RNA inverse folding with profound implications for biotechnological and therapeutic applications.

