---
layout: default
title: RAIGen: Rare Attribute Identification in Text-to-Image Generative Models
---

# RAIGen: Rare Attribute Identification in Text-to-Image Generative Models
**arXiv**：[2602.06806v1](https://arxiv.org/abs/2602.06806) · [PDF](https://arxiv.org/pdf/2602.06806.pdf)  
**作者**：Silpa Vadakkeeveetil Sreelatha, Dan Wang, Serge Belongie, Muhammad Awais, Anjan Dutta  

**一句话要点**：提出RAIGen框架以无监督发现文本到图像生成模型中的稀有属性

**关键词**：文本到图像生成, 稀有属性发现, 无监督学习, 稀疏自编码器, 模型审计, 偏差缓解

## 3 点简述
- 核心问题：现有方法忽视从模型表示中识别数据分布中代表性不足的稀有属性
- 方法要点：利用Matryoshka稀疏自编码器和结合激活频率与语义区分度的新度量来发现可解释神经元
- 实验或效果：在Stable Diffusion和SDXL中验证，支持跨架构系统审计和生成时稀有属性定向增强

## 摘要（原文）

> Text-to-image diffusion models achieve impressive generation quality but inherit and amplify training-data biases, skewing coverage of semantic attributes. Prior work addresses this in two ways. Closed-set approaches mitigate biases in predefined fairness categories (e.g., gender, race), assuming socially salient minority attributes are known a priori. Open-set approaches frame the task as bias identification, highlighting majority attributes that dominate outputs. Both overlook a complementary task: uncovering rare or minority features underrepresented in the data distribution (social, cultural, or stylistic) yet still encoded in model representations. We introduce RAIGen, the first framework, to our knowledge, for un-supervised rare-attribute discovery in diffusion models. RAIGen leverages Matryoshka Sparse Autoencoders and a novel minority metric combining neuron activation frequency with semantic distinctiveness to identify interpretable neurons whose top-activating images reveal underrepresented attributes. Experiments show RAIGen discovers attributes beyond fixed fairness categories in Stable Diffusion, scales to larger models such as SDXL, supports systematic auditing across architectures, and enables targeted amplification of rare attributes during generation.

