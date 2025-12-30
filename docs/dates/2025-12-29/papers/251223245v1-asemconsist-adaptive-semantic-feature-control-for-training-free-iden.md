---
layout: default
title: ASemConsist: Adaptive Semantic Feature Control for Training-Free Identity-Consistent Generation
---

# ASemConsist: Adaptive Semantic Feature Control for Training-Free Identity-Consistent Generation
**arXiv**：[2512.23245v1](https://arxiv.org/abs/2512.23245) · [PDF](https://arxiv.org/pdf/2512.23245.pdf)  
**作者**：Shin seong Kim, Minjung Shin, Hyunin Cho, Youngjung Uh  

**一句话要点**：提出ASemConsist框架，通过自适应语义特征控制解决文本到图像生成中角色身份一致性问题。

**关键词**：文本到图像生成, 身份一致性, 语义特征控制, 自适应策略, 扩散模型, 评估协议

## 3 点简述
- 核心问题：文本到图像扩散模型在生成序列图像时难以平衡角色身份一致性与每张图像的提示对齐。
- 方法要点：采用选择性文本嵌入修改和自适应特征共享策略，利用填充嵌入作为语义容器进行显式控制。
- 实验或效果：提出一致性质量分数（CQS）统一评估协议，在保持提示对齐的同时实现最先进的性能。

## 摘要（原文）

> Recent text-to-image diffusion models have significantly improved visual quality and text alignment. However, generating a sequence of images while preserving consistent character identity across diverse scene descriptions remains a challenging task. Existing methods often struggle with a trade-off between maintaining identity consistency and ensuring per-image prompt alignment. In this paper, we introduce a novel framework, ASemconsist, that addresses this challenge through selective text embedding modification, enabling explicit semantic control over character identity without sacrificing prompt alignment. Furthermore, based on our analysis of padding embeddings in FLUX, we propose a semantic control strategy that repurposes padding embeddings as semantic containers. Additionally, we introduce an adaptive feature-sharing strategy that automatically evaluates textual ambiguity and applies constraints only to the ambiguous identity prompt. Finally, we propose a unified evaluation protocol, the Consistency Quality Score (CQS), which integrates identity preservation and per-image text alignment into a single comprehensive metric, explicitly capturing performance imbalances between the two metrics. Our framework achieves state-of-the-art performance, effectively overcoming prior trade-offs. Project page: https://minjung-s.github.io/asemconsist

