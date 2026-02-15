---
layout: default
title: AssetFormer: Modular 3D Assets Generation with Autoregressive Transformer
---

# AssetFormer: Modular 3D Assets Generation with Autoregressive Transformer
**arXiv**：[2602.12100v1](https://arxiv.org/abs/2602.12100) · [PDF](https://arxiv.org/pdf/2602.12100.pdf)  
**作者**：Lingting Zhu, Shengju Qian, Haidi Fan, Jiayu Dong, Zhenchao Jin, Siwei Zhou, Gen Dong, Xin Wang, Lequan Yu  

**一句话要点**：提出AssetFormer，基于自回归Transformer从文本生成模块化3D资产，以支持专业开发和用户生成内容。

**关键词**：模块化3D资产生成, 自回归Transformer, 文本到3D生成, 用户生成内容, 3D内容生成

## 3 点简述
- 核心问题：数字产业需高质量、多样化的模块化3D资产，但生成需满足约束设计参数。
- 方法要点：采用自回归Transformer，创新模块序列化和解码技术，提升资产生成质量。
- 实验或效果：初步结果验证AssetFormer在专业开发和UGC场景中有效简化资产创建流程。

## 摘要（原文）

> The digital industry demands high-quality, diverse modular 3D assets, especially for user-generated content~(UGC). In this work, we introduce AssetFormer, an autoregressive Transformer-based model designed to generate modular 3D assets from textual descriptions. Our pilot study leverages real-world modular assets collected from online platforms. AssetFormer tackles the challenge of creating assets composed of primitives that adhere to constrained design parameters for various applications. By innovatively adapting module sequencing and decoding techniques inspired by language models, our approach enhances asset generation quality through autoregressive modeling. Initial results indicate the effectiveness of AssetFormer in streamlining asset creation for professional development and UGC scenarios. This work presents a flexible framework extendable to various types of modular 3D assets, contributing to the broader field of 3D content generation. The code is available at https://github.com/Advocate99/AssetFormer.

