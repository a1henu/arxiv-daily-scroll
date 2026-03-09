---
layout: default
title: Learning to Generate via Understanding: Understanding-Driven Intrinsic Rewarding for Unified Multimodal Models
---

# Learning to Generate via Understanding: Understanding-Driven Intrinsic Rewarding for Unified Multimodal Models
**arXiv**：[2603.06043v1](https://arxiv.org/abs/2603.06043) · [PDF](https://arxiv.org/pdf/2603.06043.pdf)  
**作者**：Jiadong Pan, Liang Li, Yuxin Peng, Yu-Ming Tang, Shuohuan Wang, Yu Sun, Hua Wu, Qingming Huang, Haifeng Wang  

**一句话要点**：提出基于理解的内在奖励机制GvU，以缩小统一多模态模型中视觉理解与生成的能力差距。

**关键词**：统一多模态模型, 文本到图像生成, 内在奖励, 自监督学习, 强化学习, 视觉理解

## 3 点简述
- 核心问题：统一多模态模型存在视觉理解强但生成能力弱的内在解耦问题。
- 方法要点：设计令牌级文本-图像对齐内在奖励GvU，使模型通过理解分支自我评估并指导生成。
- 实验或效果：自监督强化学习框架提升生成质量，同时增强细粒度视觉理解，无需外部监督。

## 摘要（原文）

> Recently, unified multimodal models (UMMs) have made remarkable progress in integrating visual understanding and generation, demonstrating strong potential for complex text-to-image (T2I) tasks. Despite their theoretical promise, a persistent capability gap exists: UMMs typically exhibit superior visual understanding but comparatively weaker generative capabilities. This discrepancy arises largely from the intrinsic decoupling between the understanding and generation processes. While a UMM can accurately interpret fine-grained visual details, it often struggles to produce semantically coherent images from complex textual prompts. To address this challenge, we explore UMMs' internal understanding capability to enhance generation quality. We propose a token-level intrinsic text-image alignment reward mechanism, GvU, enabling the UMM to act simultaneously as teacher and student: it evaluates its own outputs using the understanding branch to guide the generations accordingly. Building upon this, we design a self-supervised reinforcement learning framework, allowing UMMs to iteratively improve their generation quality through understanding-based intrinsic reward signals--without reliance on external supervision. Experimental results show that our method substantially boosts UMMs' generation, which in turn strengthens their fine-grained visual understanding, narrowing the capability gap between UMMs' visual understanding and generation.

