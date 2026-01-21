---
layout: default
title: VENI: Variational Encoder for Natural Illumination
---

# VENI: Variational Encoder for Natural Illumination
**arXiv**：[2601.14079v1](https://arxiv.org/abs/2601.14079) · [PDF](https://arxiv.org/pdf/2601.14079.pdf)  
**作者**：Paul Walker, James A. D. Gardner, Andreea Ardelean, William A. P. Smith, Bernhard Egger  

**一句话要点**：提出旋转等变变分自编码器VENI以建模球面自然光照，改进逆渲染中的光照先验。

**关键词**：逆渲染, 旋转等变模型, 变分自编码器, 光照建模, 球面表示, 潜在空间优化

## 3 点简述
- 核心问题：逆渲染中光照建模忽略球面旋转等变性或潜在空间不理想。
- 方法要点：使用VN-ViT编码器和旋转等变条件神经场解码器，保持SO(2)等变性。
- 实验或效果：潜在空间插值更平滑，SO(2)等变全连接层优于标准向量神经元。

## 摘要（原文）

> Inverse rendering is an ill-posed problem, but priors like illumination priors, can simplify it. Existing work either disregards the spherical and rotation-equivariant nature of illumination environments or does not provide a well-behaved latent space. We propose a rotation-equivariant variational autoencoder that models natural illumination on the sphere without relying on 2D projections. To preserve the SO(2)-equivariance of environment maps, we use a novel Vector Neuron Vision Transformer (VN-ViT) as encoder and a rotation-equivariant conditional neural field as decoder. In the encoder, we reduce the equivariance from SO(3) to SO(2) using a novel SO(2)-equivariant fully connected layer, an extension of Vector Neurons. We show that our SO(2)-equivariant fully connected layer outperforms standard Vector Neurons when used in our SO(2)-equivariant model. Compared to previous methods, our variational autoencoder enables smoother interpolation in latent space and offers a more well-behaved latent space.

