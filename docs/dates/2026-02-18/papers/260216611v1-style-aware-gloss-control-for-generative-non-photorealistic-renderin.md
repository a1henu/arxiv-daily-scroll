---
layout: default
title: Style-Aware Gloss Control for Generative Non-Photorealistic Rendering
---

# Style-Aware Gloss Control for Generative Non-Photorealistic Rendering
**arXiv**：[2602.16611v1](https://arxiv.org/abs/2602.16611) · [PDF](https://arxiv.org/pdf/2602.16611.pdf)  
**作者**：Santiago Jimenez-Navarro, Belen Masia, Ana Serrano  

**一句话要点**：提出风格感知光泽控制方法，用于生成非真实感渲染图像

**关键词**：非真实感渲染, 光泽控制, 风格解耦, 生成模型, 潜在空间, 扩散模型

## 3 点简述
- 核心问题：研究光泽与艺术风格在生成模型中的表示与解耦关系
- 方法要点：基于新数据集训练无监督生成模型，构建层次化潜在空间，并引入轻量适配器连接扩散模型
- 实验或效果：相比先前模型，在解耦性和可控性方面表现更优

## 摘要（原文）

> Humans can infer material characteristics of objects from their visual appearance, and this ability extends to artistic depictions, where similar perceptual strategies guide the interpretation of paintings or drawings. Among the factors that define material appearance, gloss, along with color, is widely regarded as one of the most important, and recent studies indicate that humans can perceive gloss independently of the artistic style used to depict an object. To investigate how gloss and artistic style are represented in learned models, we train an unsupervised generative model on a newly curated dataset of painterly objects designed to systematically vary such factors. Our analysis reveals a hierarchical latent space in which gloss is disentangled from other appearance factors, allowing for a detailed study of how gloss is represented and varies across artistic styles. Building on this representation, we introduce a lightweight adapter that connects our style- and gloss-aware latent space to a latent-diffusion model, enabling the synthesis of non-photorealistic images with fine-grained control of these factors. We compare our approach with previous models and observe improved disentanglement and controllability of the learned factors.

