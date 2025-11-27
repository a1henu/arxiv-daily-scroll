---
layout: default
title: Harmony: Harmonizing Audio and Video Generation through Cross-Task Synergy
---

# Harmony: Harmonizing Audio and Video Generation through Cross-Task Synergy
**arXiv**：[2511.21579v1](https://arxiv.org/abs/2511.21579) · [PDF](https://arxiv.org/pdf/2511.21579.pdf)  
**作者**：Teng Hu, Zhentao Yu, Guozhen Zhang, Zihan Su, Zhengguang Zhou, Youliang Zhang, Yuan Zhou, Qinglin Lu, Ran Yi  

**一句话要点**：提出Harmony框架以解决音视频生成中的同步问题

**关键词**：音视频生成, 扩散模型, 跨模态同步, 类无关引导, 注意力机制

## 3 点简述
- 核心问题：联合扩散过程存在对应漂移、全局注意力低效和类无关引导的模态内偏差
- 方法要点：引入跨任务协同训练、全局-局部解耦交互模块和同步增强CFG
- 实验或效果：在生成保真度和音视频同步方面显著优于现有方法

## 摘要（原文）

> The synthesis of synchronized audio-visual content is a key challenge in generative AI, with open-source models facing challenges in robust audio-video alignment. Our analysis reveals that this issue is rooted in three fundamental challenges of the joint diffusion process: (1) Correspondence Drift, where concurrently evolving noisy latents impede stable learning of alignment; (2) inefficient global attention mechanisms that fail to capture fine-grained temporal cues; and (3) the intra-modal bias of conventional Classifier-Free Guidance (CFG), which enhances conditionality but not cross-modal synchronization. To overcome these challenges, we introduce Harmony, a novel framework that mechanistically enforces audio-visual synchronization. We first propose a Cross-Task Synergy training paradigm to mitigate drift by leveraging strong supervisory signals from audio-driven video and video-driven audio generation tasks. Then, we design a Global-Local Decoupled Interaction Module for efficient and precise temporal-style alignment. Finally, we present a novel Synchronization-Enhanced CFG (SyncCFG) that explicitly isolates and amplifies the alignment signal during inference. Extensive experiments demonstrate that Harmony establishes a new state-of-the-art, significantly outperforming existing methods in both generation fidelity and, critically, in achieving fine-grained audio-visual synchronization.

