---
layout: default
title: Mitty: Diffusion-based Human-to-Robot Video Generation
---

# Mitty: Diffusion-based Human-to-Robot Video Generation
**arXiv**：[2512.17253v1](https://arxiv.org/abs/2512.17253) · [PDF](https://arxiv.org/pdf/2512.17253.pdf)  
**作者**：Yiren Song, Cheng Liu, Weijia Mao, Mike Zheng Shou  

**一句话要点**：提出Mitty扩散模型，实现端到端人类演示视频到机器人执行视频的生成

**关键词**：视频生成, 扩散模型, 机器人学习, 端到端学习, 上下文学习

## 3 点简述
- 核心问题：现有方法依赖关键点等中间表示，导致信息丢失和累积误差，损害时空一致性。
- 方法要点：基于预训练视频扩散模型，通过扩散过程中的双向注意力融合人类演示和机器人去噪令牌，无需动作标签或中间抽象。
- 实验或效果：在Human2Robot和EPIC-Kitchens上实现先进性能，展示强泛化能力，为可扩展机器人学习提供新见解。

## 摘要（原文）

> Learning directly from human demonstration videos is a key milestone toward scalable and generalizable robot learning. Yet existing methods rely on intermediate representations such as keypoints or trajectories, introducing information loss and cumulative errors that harm temporal and visual consistency. We present Mitty, a Diffusion Transformer that enables video In-Context Learning for end-to-end Human2Robot video generation. Built on a pretrained video diffusion model, Mitty leverages strong visual-temporal priors to translate human demonstrations into robot-execution videos without action labels or intermediate abstractions. Demonstration videos are compressed into condition tokens and fused with robot denoising tokens through bidirectional attention during diffusion. To mitigate paired-data scarcity, we also develop an automatic synthesis pipeline that produces high-quality human-robot pairs from large egocentric datasets. Experiments on Human2Robot and EPIC-Kitchens show that Mitty delivers state-of-the-art results, strong generalization to unseen environments, and new insights for scalable robot learning from human observations.

