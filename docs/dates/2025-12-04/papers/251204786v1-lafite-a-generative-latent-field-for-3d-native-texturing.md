---
layout: default
title: LaFiTe: A Generative Latent Field for 3D Native Texturing
---

# LaFiTe: A Generative Latent Field for 3D Native Texturing
**arXiv**：[2512.04786v1](https://arxiv.org/abs/2512.04786) · [PDF](https://arxiv.org/pdf/2512.04786.pdf)  
**作者**：Chia-Hao Chen, Zi-Xin Zou, Yan-Pei Cao, Ze Yuan, Guan Luo, Xiaojuan Qi, Ding Liang, Song-Hai Zhang, Yuan-Chen Guo  

**一句话要点**：提出LaFiTe框架，通过生成稀疏潜在颜色场解决3D原生纹理生成中的表示瓶颈问题。

**关键词**：3D原生纹理生成, 潜在颜色场, 变分自编码器, 纹理合成, 3D内容创建

## 3 点简述
- 核心问题：现有3D原生纹理方法因缺乏强大潜在表示，限制了纹理保真度和通用性。
- 方法要点：使用变分自编码器编码表面外观为稀疏结构化潜在空间，再解码为连续颜色场。
- 实验或效果：在重建中PSNR超过现有方法>10 dB，支持多样风格纹理合成和下游应用。

## 摘要（原文）

> Generating high-fidelity, seamless textures directly on 3D surfaces, what we term 3D-native texturing, remains a fundamental open challenge, with the potential to overcome long-standing limitations of UV-based and multi-view projection methods. However, existing native approaches are constrained by the absence of a powerful and versatile latent representation, which severely limits the fidelity and generality of their generated textures. We identify this representation gap as the principal barrier to further progress. We introduce LaFiTe, a framework that addresses this challenge by learning to generate textures as a 3D generative sparse latent color field. At its core, LaFiTe employs a variational autoencoder (VAE) to encode complex surface appearance into a sparse, structured latent space, which is subsequently decoded into a continuous color field. This representation achieves unprecedented fidelity, exceeding state-of-the-art methods by >10 dB PSNR in reconstruction, by effectively disentangling texture appearance from mesh topology and UV parameterization. Building upon this strong representation, a conditional rectified-flow model synthesizes high-quality, coherent textures across diverse styles and geometries. Extensive experiments demonstrate that LaFiTe not only sets a new benchmark for 3D-native texturing but also enables flexible downstream applications such as material synthesis and texture super-resolution, paving the way for the next generation of 3D content creation workflows.

