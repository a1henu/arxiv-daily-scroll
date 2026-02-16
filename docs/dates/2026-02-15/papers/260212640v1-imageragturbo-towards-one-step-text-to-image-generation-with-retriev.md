---
layout: default
title: ImageRAGTurbo: Towards One-step Text-to-Image Generation with Retrieval-Augmented Diffusion Models
---

# ImageRAGTurbo: Towards One-step Text-to-Image Generation with Retrieval-Augmented Diffusion Models
**arXiv**：[2602.12640v1](https://arxiv.org/abs/2602.12640) · [PDF](https://arxiv.org/pdf/2602.12640.pdf)  
**作者**：Peijie Qiu, Hariharan Ramshankar, Arnau Ramisa, René Vidal, Amit Kumar K C, Vamsi Salaka, Rahul Bhagat  

**一句话要点**：提出ImageRAGTurbo，通过检索增强高效微调少步扩散模型，实现一步文本到图像生成。

**关键词**：文本到图像生成, 检索增强, 扩散模型, 少步生成, H空间编辑, 交叉注意力

## 3 点简述
- 核心问题：扩散模型迭代采样导致高延迟，少步生成常牺牲图像质量和提示对齐。
- 方法要点：基于文本提示检索相关文本-图像对，通过可训练适配器在UNet去噪器的H空间融合检索内容。
- 实验或效果：在快速文本到图像生成中，相比现有方法，不增加延迟下生成高保真图像。

## 摘要（原文）

> Diffusion models have emerged as the leading approach for text-to-image generation. However, their iterative sampling process, which gradually morphs random noise into coherent images, introduces significant latency that limits their applicability. While recent few-step diffusion models reduce the number of sampling steps to as few as one to four steps, they often compromise image quality and prompt alignment, especially in one-step generation. Additionally, these models require computationally expensive training procedures. To address these limitations, we propose ImageRAGTurbo, a novel approach to efficiently finetune few-step diffusion models via retrieval augmentation. Given a text prompt, we retrieve relevant text-image pairs from a database and use them to condition the generation process. We argue that such retrieved examples provide rich contextual information to the UNet denoiser that helps reduce the number of denoising steps without compromising image quality. Indeed, our initial investigations show that using the retrieved content to edit the denoiser's latent space ($\mathcal{H}$-space) without additional finetuning already improves prompt fidelity. To further improve the quality of the generated images, we augment the UNet denoiser with a trainable adapter in the $\mathcal{H}$-space, which efficiently blends the retrieved content with the target prompt using a cross-attention mechanism. Experimental results on fast text-to-image generation demonstrate that our approach produces high-fidelity images without compromising latency compared to existing methods.

