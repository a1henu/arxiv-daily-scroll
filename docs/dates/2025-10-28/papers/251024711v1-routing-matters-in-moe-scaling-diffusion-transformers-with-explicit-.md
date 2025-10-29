---
layout: default
title: Routing Matters in MoE: Scaling Diffusion Transformers with Explicit Routing Guidance
---

# Routing Matters in MoE: Scaling Diffusion Transformers with Explicit Routing Guidance
**arXiv**：[2510.24711v1](https://arxiv.org/abs/2510.24711) · [PDF](https://arxiv.org/pdf/2510.24711.pdf)  
**作者**：Yujie Wei, Shiwei Zhang, Hangjie Yuan, Yujin Han, Zhekai Chen, Jiayu Wang, Difan Zou, Xihui Liu, Yingya Zhang, Yu Liu, Hongming Shan  

**一句话要点**：提出ProMoE框架以解决视觉MoE中专家专业化不足的问题

**关键词**：混合专家模型, 扩散变换器, 路由指导, 视觉令牌处理, 原型路由, 对比损失

## 3 点简述
- 核心问题：视觉令牌存在空间冗余和功能异质性，阻碍MoE在扩散变换器中的专家专业化
- 方法要点：采用两步路由器，通过条件路由和原型路由提供显式路由指导
- 实验或效果：在ImageNet基准上超越现有方法，支持Rectified Flow和DDPM训练目标

## 摘要（原文）

> Mixture-of-Experts (MoE) has emerged as a powerful paradigm for scaling model
> capacity while preserving computational efficiency. Despite its notable success
> in large language models (LLMs), existing attempts to apply MoE to Diffusion
> Transformers (DiTs) have yielded limited gains. We attribute this gap to
> fundamental differences between language and visual tokens. Language tokens are
> semantically dense with pronounced inter-token variation, while visual tokens
> exhibit spatial redundancy and functional heterogeneity, hindering expert
> specialization in vision MoE. To this end, we present ProMoE, an MoE framework
> featuring a two-step router with explicit routing guidance that promotes expert
> specialization. Specifically, this guidance encourages the router to partition
> image tokens into conditional and unconditional sets via conditional routing
> according to their functional roles, and refine the assignments of conditional
> image tokens through prototypical routing with learnable prototypes based on
> semantic content. Moreover, the similarity-based expert allocation in latent
> space enabled by prototypical routing offers a natural mechanism for
> incorporating explicit semantic guidance, and we validate that such guidance is
> crucial for vision MoE. Building on this, we propose a routing contrastive loss
> that explicitly enhances the prototypical routing process, promoting
> intra-expert coherence and inter-expert diversity. Extensive experiments on
> ImageNet benchmark demonstrate that ProMoE surpasses state-of-the-art methods
> under both Rectified Flow and DDPM training objectives. Code and models will be
> made publicly available.

