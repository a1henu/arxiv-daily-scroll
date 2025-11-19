---
layout: default
title: Diffusion As Self-Distillation: End-to-End Latent Diffusion In One Model
---

# Diffusion As Self-Distillation: End-to-End Latent Diffusion In One Model
**arXiv**：[2511.14716v1](https://arxiv.org/abs/2511.14716) · [PDF](https://arxiv.org/pdf/2511.14716.pdf)  
**作者**：Xiyuan Wang, Muhan Zhang  

**一句话要点**：提出扩散自蒸馏框架以解决潜在扩散模型模块化训练不稳定的问题

**关键词**：潜在扩散模型, 自蒸馏, 端到端训练, 图像生成, 训练稳定性

## 3 点简述
- 标准潜在扩散模型采用编码器、解码器和扩散网络分离架构，导致训练效率低和性能不佳
- 通过类比自蒸馏方法，提出DSD框架修改训练目标，稳定潜在空间学习
- 在ImageNet 256×256条件生成任务中，以较少参数和训练轮次实现高FID分数

## 摘要（原文）

> Standard Latent Diffusion Models rely on a complex, three-part architecture consisting of a separate encoder, decoder, and diffusion network, which are trained in multiple stages. This modular design is computationally inefficient, leads to suboptimal performance, and prevents the unification of diffusion with the single-network architectures common in vision foundation models. Our goal is to unify these three components into a single, end-to-end trainable network. We first demonstrate that a naive joint training approach fails catastrophically due to ``latent collapse'', where the diffusion training objective interferes with the network's ability to learn a good latent representation. We identify the root causes of this instability by drawing a novel analogy between diffusion and self-distillation based unsupervised learning method. Based on this insight, we propose Diffusion as Self-Distillation (DSD), a new framework with key modifications to the training objective that stabilize the latent space. This approach enables, for the first time, the stable end-to-end training of a single network that simultaneously learns to encode, decode, and perform diffusion. DSD achieves outstanding performance on the ImageNet $256\times 256$ conditional generation task: FID=13.44/6.38/4.25 with only 42M/118M/205M parameters and 50 training epochs on ImageNet, without using classifier-free-guidance.

