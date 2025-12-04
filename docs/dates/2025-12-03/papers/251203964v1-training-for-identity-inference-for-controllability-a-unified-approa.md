---
layout: default
title: Training for Identity, Inference for Controllability: A Unified Approach to Tuning-Free Face Personalization
---

# Training for Identity, Inference for Controllability: A Unified Approach to Tuning-Free Face Personalization
**arXiv**：[2512.03964v1](https://arxiv.org/abs/2512.03964) · [PDF](https://arxiv.org/pdf/2512.03964.pdf)  
**作者**：Lianyu Pang, Ji Zhou, Qiping Wang, Baoquan Zhao, Zhenguo Yang, Qing Li, Xudong Mao  

**一句话要点**：提出UniID统一框架，通过训练-推理策略实现免调优人脸个性化中身份保真与文本可控性的平衡。

**关键词**：人脸个性化, 免调优方法, 身份保真, 文本可控性, 扩散模型, 统一框架

## 3 点简述
- 核心问题：现有免调优人脸个性化方法难以同时实现高身份保真和灵活文本可控性。
- 方法要点：结合文本嵌入和适配器范式，训练时专注身份特征学习，推理时引入归一化重缩放机制。
- 实验或效果：在六种先进方法对比中，UniID在身份保真和文本可控性上均表现优异。

## 摘要（原文）

> Tuning-free face personalization methods have developed along two distinct paradigms: text embedding approaches that map facial features into the text embedding space, and adapter-based methods that inject features through auxiliary cross-attention layers. While both paradigms have shown promise, existing methods struggle to simultaneously achieve high identity fidelity and flexible text controllability. We introduce UniID, a unified tuning-free framework that synergistically integrates both paradigms. Our key insight is that when merging these approaches, they should mutually reinforce only identity-relevant information while preserving the original diffusion prior for non-identity attributes. We realize this through a principled training-inference strategy: during training, we employ an identity-focused learning scheme that guides both branches to capture identity features exclusively; at inference, we introduce a normalized rescaling mechanism that recovers the text controllability of the base diffusion model while enabling complementary identity signals to enhance each other. This principled design enables UniID to achieve high-fidelity face personalization with flexible text controllability. Extensive experiments against six state-of-the-art methods demonstrate that UniID achieves superior performance in both identity preservation and text controllability. Code will be available at https://github.com/lyuPang/UniID

