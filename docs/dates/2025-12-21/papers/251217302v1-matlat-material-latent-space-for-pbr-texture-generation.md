---
layout: default
title: MatLat: Material Latent Space for PBR Texture Generation
---

# MatLat: Material Latent Space for PBR Texture Generation
**arXiv**：[2512.17302v1](https://arxiv.org/abs/2512.17302) · [PDF](https://arxiv.org/pdf/2512.17302.pdf)  
**作者**：Kyeongmin Yeo, Yunhong Min, Jaihoon Kim, Minhyuk Sung  

**一句话要点**：提出MatLat框架，通过微调VAE和引入局部性正则化，生成高质量PBR纹理以解决数据集稀缺和分布偏移问题。

**关键词**：PBR纹理生成, 材料潜在空间, VAE微调, 扩散模型, 局部性正则化, 3D网格纹理

## 3 点简述
- 核心问题：大规模PBR纹理数据集稀缺，现有方法冻结嵌入网络导致分布偏移，影响扩散训练。
- 方法要点：微调预训练VAE，引入材料潜在空间MatLat，通过裁剪潜在块和解码对齐来保持像素-潜在空间对应性。
- 实验或效果：消融研究和基线比较显示，框架提升PBR纹理保真度，各组件对实现先进性能至关重要。

## 摘要（原文）

> We propose a generative framework for producing high-quality PBR textures on a given 3D mesh. As large-scale PBR texture datasets are scarce, our approach focuses on effectively leveraging the embedding space and diffusion priors of pretrained latent image generative models while learning a material latent space, MatLat, through targeted fine-tuning. Unlike prior methods that freeze the embedding network and thus lead to distribution shifts when encoding additional PBR channels and hinder subsequent diffusion training, we fine-tune the pretrained VAE so that new material channels can be incorporated with minimal latent distribution deviation. We further show that correspondence-aware attention alone is insufficient for cross-view consistency unless the latent-to-image mapping preserves locality. To enforce this locality, we introduce a regularization in the VAE fine-tuning that crops latent patches, decodes them, and aligns the corresponding image regions to maintain strong pixel-latent spatial correspondence. Ablation studies and comparison with previous baselines demonstrate that our framework improves PBR texture fidelity and that each component is critical for achieving state-of-the-art performance.

