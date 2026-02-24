---
layout: default
title: ConceptPrism: Concept Disentanglement in Personalized Diffusion Models via Residual Token Optimization
---

# ConceptPrism: Concept Disentanglement in Personalized Diffusion Models via Residual Token Optimization
**arXiv**：[2602.19575v1](https://arxiv.org/abs/2602.19575) · [PDF](https://arxiv.org/pdf/2602.19575.pdf)  
**作者**：Minseo Kim, Minchan Kwon, Dongyeun Lee, Yunho Jeon, Junmo Kim  

**一句话要点**：提出ConceptPrism框架，通过残差令牌优化解决个性化扩散模型中的概念纠缠问题。

**关键词**：概念解耦, 个性化扩散模型, 残差令牌优化, 文本到图像生成, 概念纠缠

## 3 点简述
- 核心问题：个性化文本到图像生成存在概念纠缠，导致概念保真度与文本对齐间的权衡。
- 方法要点：自动比较图像集，联合优化目标令牌和残差令牌，使用重建损失和排除损失实现概念解耦。
- 实验或效果：广泛实验显示，ConceptPrism有效解决纠缠，显著改善保真度与对齐的权衡。

## 摘要（原文）

> Personalized text-to-image generation suffers from concept entanglement, where irrelevant residual information from reference images is captured, leading to a trade-off between concept fidelity and text alignment. Recent disentanglement approaches attempt to solve this utilizing manual guidance, such as linguistic cues or segmentation masks, which limits their applicability and fails to fully articulate the target concept. In this paper, we propose ConceptPrism, a novel framework that automatically disentangles the shared visual concept from image-specific residuals by comparing images within a set. Our method jointly optimizes a target token and image-wise residual tokens using two complementary objectives: a reconstruction loss to ensure fidelity, and a novel exclusion loss that compels residual tokens to discard the shared concept. This process allows the target token to capture the pure concept without direct supervision. Extensive experiments demonstrate that ConceptPrism effectively resolves concept entanglement, achieving a significantly improved trade-off between fidelity and alignment.

