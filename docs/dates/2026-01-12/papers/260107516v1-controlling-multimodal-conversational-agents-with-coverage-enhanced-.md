---
layout: default
title: Controlling Multimodal Conversational Agents with Coverage-Enhanced Latent Actions
---

# Controlling Multimodal Conversational Agents with Coverage-Enhanced Latent Actions
**arXiv**：[2601.07516v1](https://arxiv.org/abs/2601.07516) · [PDF](https://arxiv.org/pdf/2601.07516.pdf)  
**作者**：Yongqi Li, Hao Lang, Tieyun Qian, Yongbin Li  

**一句话要点**：提出覆盖增强的潜在动作空间方法，以解决多模态对话代理在强化学习微调中处理大文本令牌空间的挑战。

**关键词**：多模态对话代理, 强化学习微调, 潜在动作空间, 跨模态投影, 循环一致性损失, 文本令牌空间压缩

## 3 点简述
- 核心问题：强化学习微调多模态对话代理时，大文本令牌空间导致效率低下和泛化困难。
- 方法要点：通过从观察学习构建潜在动作空间，利用配对和纯文本数据增强覆盖，引入跨模态投影器和循环一致性损失。
- 实验或效果：在两种对话任务上优于基线，验证了潜在动作方法在多种强化学习算法中的有效性。

## 摘要（原文）

> Vision-language models are increasingly employed as multimodal conversational agents (MCAs) for diverse conversational tasks. Recently, reinforcement learning (RL) has been widely explored for adapting MCAs to various human-AI interaction scenarios. Despite showing great enhancement in generalization performance, fine-tuning MCAs via RL still faces challenges in handling the extremely large text token space. To address this, we learn a compact latent action space for RL fine-tuning instead. Specifically, we adopt the learning from observation mechanism to construct the codebook for the latent action space, where future observations are leveraged to estimate current latent actions that could further be used to reconstruct future observations. However, the scarcity of paired image-text data hinders learning a codebook with sufficient coverage. Thus, we leverage both paired image-text data and text-only data to construct the latent action space, using a cross-modal projector for transforming text embeddings into image-text embeddings. We initialize the cross-modal projector on paired image-text data, and further train it on massive text-only data with a novel cycle consistency loss to enhance its robustness. We show that our latent action based method outperforms competitive baselines on two conversation tasks across various RL algorithms.

