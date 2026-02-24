---
layout: default
title: ExpPortrait: Expressive Portrait Generation via Personalized Representation
---

# ExpPortrait: Expressive Portrait Generation via Personalized Representation
**arXiv**：[2602.19900v1](https://arxiv.org/abs/2602.19900) · [PDF](https://arxiv.org/pdf/2602.19900.pdf)  
**作者**：Junyi Wang, Yudong Guo, Boyang Guo, Shengming Yang, Juyong Zhang  

**一句话要点**：提出高保真个性化头部表示与表达转移模块，以生成富有表现力的肖像视频。

**关键词**：肖像生成, 扩散模型, 个性化表示, 表达转移, 视频合成

## 3 点简述
- 核心问题：现有肖像生成方法因稀疏或低秩表示，难以准确保留身份与表达细节。
- 方法要点：设计个性化头部表示，解耦身份与表达，并引入表达转移模块实现跨身份细节迁移。
- 实验或效果：在自重演和交叉重演任务中，身份保持、表达准确性和时间稳定性优于先前模型。

## 摘要（原文）

> While diffusion models have shown great potential in portrait generation, generating expressive, coherent, and controllable cinematic portrait videos remains a significant challenge. Existing intermediate signals for portrait generation, such as 2D landmarks and parametric models, have limited disentanglement capabilities and cannot express personalized details due to their sparse or low-rank representation. Therefore, existing methods based on these models struggle to accurately preserve subject identity and expressions, hindering the generation of highly expressive portrait videos. To overcome these limitations, we propose a high-fidelity personalized head representation that more effectively disentangles expression and identity. This representation captures both static, subject-specific global geometry and dynamic, expression-related details. Furthermore, we introduce an expression transfer module to achieve personalized transfer of head pose and expression details between different identities. We use this sophisticated and highly expressive head model as a conditional signal to train a diffusion transformer (DiT)-based generator to synthesize richly detailed portrait videos. Extensive experiments on self- and cross-reenactment tasks demonstrate that our method outperforms previous models in terms of identity preservation, expression accuracy, and temporal stability, particularly in capturing fine-grained details of complex motion.

