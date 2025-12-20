---
layout: default
title: DeContext as Defense: Safe Image Editing in Diffusion Transformers
---

# DeContext as Defense: Safe Image Editing in Diffusion Transformers
**arXiv**：[2512.16625v1](https://arxiv.org/abs/2512.16625) · [PDF](https://arxiv.org/pdf/2512.16625.pdf)  
**作者**：Linghui Shen, Mingyue Cui, Xingyi Yang  

**一句话要点**：提出DeContext方法以保护图像免遭未经授权的上下文编辑

**关键词**：图像编辑防御, 上下文扩散模型, 注意力扰动, 隐私保护, 多模态注意力

## 3 点简述
- 核心问题：上下文扩散模型易被滥用，导致个人图像被恶意编辑，引发隐私和安全担忧。
- 方法要点：通过注入微小扰动，削弱多模态注意力层中的跨注意力路径，阻断输入图像到输出的上下文传播。
- 实验或效果：在Flux Kontext和Step1X-Edit上验证，DeContext能有效阻止不希望的编辑，同时保持图像视觉质量。

## 摘要（原文）

> In-context diffusion models allow users to modify images with remarkable ease and realism. However, the same power raises serious privacy concerns: personal images can be easily manipulated for identity impersonation, misinformation, or other malicious uses, all without the owner's consent. While prior work has explored input perturbations to protect against misuse in personalized text-to-image generation, the robustness of modern, large-scale in-context DiT-based models remains largely unexamined. In this paper, we propose DeContext, a new method to safeguard input images from unauthorized in-context editing. Our key insight is that contextual information from the source image propagates to the output primarily through multimodal attention layers. By injecting small, targeted perturbations that weaken these cross-attention pathways, DeContext breaks this flow, effectively decouples the link between input and output. This simple defense is both efficient and robust. We further show that early denoising steps and specific transformer blocks dominate context propagation, which allows us to concentrate perturbations where they matter most. Experiments on Flux Kontext and Step1X-Edit show that DeContext consistently blocks unwanted image edits while preserving visual quality. These results highlight the effectiveness of attention-based perturbations as a powerful defense against image manipulation.

