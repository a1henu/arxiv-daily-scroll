---
layout: default
title: Distribution Matching Variational AutoEncoder
---

# Distribution Matching Variational AutoEncoder
**arXiv**：[2512.07778v1](https://arxiv.org/abs/2512.07778) · [PDF](https://arxiv.org/pdf/2512.07778.pdf)  
**作者**：Sen Ye, Jianning Pei, Mengde Xu, Shuyang Gu, Chunyu Wang, Liwei Wang, Han Hu  

**一句话要点**：提出分布匹配变分自编码器，通过显式对齐潜在分布与任意参考分布来优化视觉生成建模。

**关键词**：变分自编码器, 分布匹配, 潜在空间优化, 视觉生成模型, 自监督学习

## 3 点简述
- 现有视觉生成模型（如VAE）的潜在分布未显式优化，不清楚何种分布最适合建模。
- DMVAE通过分布匹配约束，使编码器潜在分布与任意参考分布（如自监督特征分布）对齐。
- 实验发现自监督特征分布能平衡重建保真度与建模效率，在ImageNet上仅用64轮训练达到gFID=3.2。

## 摘要（原文）

> Most visual generative models compress images into a latent space before applying diffusion or autoregressive modelling. Yet, existing approaches such as VAEs and foundation model aligned encoders implicitly constrain the latent space without explicitly shaping its distribution, making it unclear which types of distributions are optimal for modeling. We introduce \textbf{Distribution-Matching VAE} (\textbf{DMVAE}), which explicitly aligns the encoder's latent distribution with an arbitrary reference distribution via a distribution matching constraint. This generalizes beyond the Gaussian prior of conventional VAEs, enabling alignment with distributions derived from self-supervised features, diffusion noise, or other prior distributions. With DMVAE, we can systematically investigate which latent distributions are more conducive to modeling, and we find that SSL-derived distributions provide an excellent balance between reconstruction fidelity and modeling efficiency, reaching gFID equals 3.2 on ImageNet with only 64 training epochs. Our results suggest that choosing a suitable latent distribution structure (achieved via distribution-level alignment), rather than relying on fixed priors, is key to bridging the gap between easy-to-model latents and high-fidelity image synthesis. Code is avaliable at https://github.com/sen-ye/dmvae.

