---
layout: default
title: LAMS-Edit: Latent and Attention Mixing with Schedulers for Improved Content Preservation in Diffusion-Based Image and Style Editing
---

# LAMS-Edit: Latent and Attention Mixing with Schedulers for Improved Content Preservation in Diffusion-Based Image and Style Editing
**arXiv**：[2601.02987v1](https://arxiv.org/abs/2601.02987) · [PDF](https://arxiv.org/pdf/2601.02987.pdf)  
**作者**：Wingwa Fu, Takayuki Okatani  

**一句话要点**：提出LAMS-Edit框架，通过潜在表示和注意力混合调度器，改进基于扩散模型的图像和风格编辑中的内容保持。

**关键词**：扩散模型, 图像编辑, 内容保持, 注意力机制, 风格迁移, 潜在表示

## 3 点简述
- 核心问题：扩散模型在文本到图像编辑中难以平衡内容保持与编辑应用，且处理真实图像编辑时存在挑战。
- 方法要点：利用反转过程的中间状态，通过加权插值混合潜在表示和注意力图，结合Prompt-to-Prompt形成可扩展框架。
- 实验或效果：实验表明LAMS-Edit能有效平衡内容保持和编辑应用，支持区域掩码精确编辑和LoRA风格迁移。

## 摘要（原文）

> Text-to-Image editing using diffusion models faces challenges in balancing content preservation with edit application and handling real-image editing. To address these, we propose LAMS-Edit, leveraging intermediate states from the inversion process--an essential step in real-image editing--during edited image generation. Specifically, latent representations and attention maps from both processes are combined at each step using weighted interpolation, controlled by a scheduler. This technique, Latent and Attention Mixing with Schedulers (LAMS), integrates with Prompt-to-Prompt (P2P) to form LAMS-Edit--an extensible framework that supports precise editing with region masks and enables style transfer via LoRA. Extensive experiments demonstrate that LAMS-Edit effectively balances content preservation and edit application.

