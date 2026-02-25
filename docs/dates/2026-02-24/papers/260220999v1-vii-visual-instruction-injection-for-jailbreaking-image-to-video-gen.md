---
layout: default
title: VII: Visual Instruction Injection for Jailbreaking Image-to-Video Generation Models
---

# VII: Visual Instruction Injection for Jailbreaking Image-to-Video Generation Models
**arXiv**：[2602.20999v1](https://arxiv.org/abs/2602.20999) · [PDF](https://arxiv.org/pdf/2602.20999.pdf)  
**作者**：Bowen Zheng, Yongli Xiang, Ziming Hong, Zerong Lin, Chaojian Yu, Tongliang Liu, Xinge You  

**一句话要点**：提出视觉指令注入框架以揭示图像到视频生成模型的越狱风险

**关键词**：图像到视频生成, 视觉指令注入, 越狱攻击, 恶意意图重编程, 视觉指令接地

## 3 点简述
- 核心问题：图像到视频生成模型可能通过参考图像中的视觉指令被恶意利用，注入不安全内容。
- 方法要点：通过恶意意图重编程和视觉指令接地模块，将不安全文本意图伪装为安全图像的视觉指令。
- 实验或效果：在四个商业模型上攻击成功率最高达83.5%，拒绝率降至近零，优于现有基线。

## 摘要（原文）

> Image-to-Video (I2V) generation models, which condition video generation on reference images, have shown emerging visual instruction-following capability, allowing certain visual cues in reference images to act as implicit control signals for video generation. However, this capability also introduces a previously overlooked risk: adversaries may exploit visual instructions to inject malicious intent through the image modality. In this work, we uncover this risk by proposing Visual Instruction Injection (VII), a training-free and transferable jailbreaking framework that intentionally disguises the malicious intent of unsafe text prompts as benign visual instructions in the safe reference image. Specifically, VII coordinates a Malicious Intent Reprogramming module to distill malicious intent from unsafe text prompts while minimizing their static harmfulness, and a Visual Instruction Grounding module to ground the distilled intent onto a safe input image by rendering visual instructions that preserve semantic consistency with the original unsafe text prompt, thereby inducing harmful content during I2V generation. Empirically, our extensive experiments on four state-of-the-art commercial I2V models (Kling-v2.5-turbo, Gemini Veo-3.1, Seedance-1.5-pro, and PixVerse-V5) demonstrate that VII achieves Attack Success Rates of up to 83.5% while reducing Refusal Rates to near zero, significantly outperforming existing baselines.

