---
layout: default
title: CleanStyle: Plug-and-Play Style Conditioning Purification for Text-to-Image Stylization
---

# CleanStyle: Plug-and-Play Style Conditioning Purification for Text-to-Image Stylization
**arXiv**：[2602.20721v1](https://arxiv.org/abs/2602.20721) · [PDF](https://arxiv.org/pdf/2602.20721.pdf)  
**作者**：Xiaoman Feng, Mingkun Lei, Yang Wang, Dingwen Fu, Chi Zhang  

**一句话要点**：提出CleanStyle框架以解决文本到图像风格化中的内容泄漏问题

**关键词**：文本到图像生成, 风格迁移, 扩散模型, 内容泄漏, 奇异值分解, 无分类器引导

## 3 点简述
- 核心问题：基于编码器的扩散模型风格迁移存在内容泄漏，损害提示保真度和风格一致性。
- 方法要点：通过SVD隔离并动态抑制风格嵌入的尾部成分，并引入风格特定无分类器引导。
- 实验或效果：实验表明该方法显著减少内容泄漏，提升风格化质量和提示对齐，无需重训练。

## 摘要（原文）

> Style transfer in diffusion models enables controllable visual generation by injecting the style of a reference image. However, recent encoder-based methods, while efficient and tuning-free, often suffer from content leakage, where semantic elements from the style image undesirably appear in the output, impairing prompt fidelity and stylistic consistency. In this work, we introduce CleanStyle, a plug-and-play framework that filters out content-related noise from the style embedding without retraining. Motivated by empirical analysis, we observe that such leakage predominantly stems from the tail components of the style embedding, which are isolated via Singular Value Decomposition (SVD). To address this, we propose CleanStyleSVD (CS-SVD), which dynamically suppresses tail components using a time-aware exponential schedule, providing clean, style-preserving conditional embeddings throughout the denoising process. Furthermore, we present Style-Specific Classifier-Free Guidance (SS-CFG), which reuses the suppressed tail components to construct style-aware unconditional inputs. Unlike conventional methods that use generic negative embeddings (e.g., zero vectors), SS-CFG introduces targeted negative signals that reflect style-specific but prompt-irrelevant visual elements. This enables the model to effectively suppress these distracting patterns during generation, thereby improving prompt fidelity and enhancing the overall visual quality of stylized outputs. Our approach is lightweight, interpretable, and can be seamlessly integrated into existing encoder-based diffusion models without retraining. Extensive experiments demonstrate that CleanStyle substantially reduces content leakage, improves stylization quality and improves prompt alignment across a wide range of style references and prompts.

