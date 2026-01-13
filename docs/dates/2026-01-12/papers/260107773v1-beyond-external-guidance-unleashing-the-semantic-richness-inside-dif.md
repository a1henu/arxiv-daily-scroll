---
layout: default
title: Beyond External Guidance: Unleashing the Semantic Richness Inside Diffusion Transformers for Improved Training
---

# Beyond External Guidance: Unleashing the Semantic Richness Inside Diffusion Transformers for Improved Training
**arXiv**：[2601.07773v1](https://arxiv.org/abs/2601.07773) · [PDF](https://arxiv.org/pdf/2601.07773.pdf)  
**作者**：Lingchen Sun, Rongyuan Wu, Zhengqiang Zhang, Ruibin Li, Yujing Sun, Shuaizheng Liu, Lei Zhang  

**一句话要点**：提出Self-Transcendence方法，利用内部特征监督加速扩散变换器训练

**关键词**：扩散变换器, 内部特征监督, 训练加速, 自监督学习, 生成模型

## 3 点简述
- 核心问题：扩散变换器训练收敛慢源于浅层表示学习困难
- 方法要点：先对齐浅层特征与VAE潜在表示，再增强中间特征以指导新训练
- 实验或效果：无需外部模型，在生成质量和收敛速度上超越现有方法

## 摘要（原文）

> Recent works such as REPA have shown that guiding diffusion models with external semantic features (e.g., DINO) can significantly accelerate the training of diffusion transformers (DiTs). However, this requires the use of pretrained external networks, introducing additional dependencies and reducing flexibility. In this work, we argue that DiTs actually have the power to guide the training of themselves, and propose \textbf{Self-Transcendence}, a simple yet effective method that achieves fast convergence using internal feature supervision only. It is found that the slow convergence in DiT training primarily stems from the difficulty of representation learning in shallow layers. To address this, we initially train the DiT model by aligning its shallow features with the latent representations from the pretrained VAE for a short phase (e.g., 40 epochs), then apply classifier-free guidance to the intermediate features, enhancing their discriminative capability and semantic expressiveness. These enriched internal features, learned entirely within the model, are used as supervision signals to guide a new DiT training. Compared to existing self-contained methods, our approach brings a significant performance boost. It can even surpass REPA in terms of generation quality and convergence speed, but without the need for any external pretrained models. Our method is not only more flexible for different backbones but also has the potential to be adopted for a wider range of diffusion-based generative tasks. The source code of our method can be found at https://github.com/csslc/Self-Transcendence.

