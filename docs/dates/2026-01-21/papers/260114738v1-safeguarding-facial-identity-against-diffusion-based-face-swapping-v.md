---
layout: default
title: Safeguarding Facial Identity against Diffusion-based Face Swapping via Cascading Pathway Disruption
---

# Safeguarding Facial Identity against Diffusion-based Face Swapping via Cascading Pathway Disruption
**arXiv**：[2601.14738v1](https://arxiv.org/abs/2601.14738) · [PDF](https://arxiv.org/pdf/2601.14738.pdf)  
**作者**：Liqin Wang, Qianyue Hu, Wei Lu, Xiangyang Luo  

**一句话要点**：提出VoidFace方法，通过级联路径破坏保护面部身份免受扩散模型换脸攻击

**关键词**：面部身份保护, 扩散模型防御, 对抗攻击, 级联路径破坏, 视觉质量优化

## 3 点简述
- 核心问题：现有防御方法忽视换脸系统的结构韧性和静态条件引导机制，导致无效
- 方法要点：在关键瓶颈注入扰动，破坏物理回归、语义嵌入和生成域，实现级联干扰
- 实验或效果：在多种扩散换脸模型上优于现有防御，同时保持对抗面部的高视觉质量

## 摘要（原文）

> The rapid evolution of diffusion models has democratized face swapping but also raises concerns about privacy and identity security. Existing proactive defenses, often adapted from image editing attacks, prove ineffective in this context. We attribute this failure to an oversight of the structural resilience and the unique static conditional guidance mechanism inherent in face swapping systems. To address this, we propose VoidFace, a systemic defense method that views face swapping as a coupled identity pathway. By injecting perturbations at critical bottlenecks, VoidFace induces cascading disruption throughout the pipeline. Specifically, we first introduce localization disruption and identity erasure to degrade physical regression and semantic embeddings, thereby impairing the accurate modeling of the source face. We then intervene in the generative domain by decoupling attention mechanisms to sever identity injection, and corrupting intermediate diffusion features to prevent the reconstruction of source identity. To ensure visual imperceptibility, we perform adversarial search in the latent manifold, guided by a perceptual adaptive strategy to balance attack potency with image quality. Extensive experiments show that VoidFace outperforms existing defenses across various diffusion-based swapping models, while producing adversarial faces with superior visual quality.

