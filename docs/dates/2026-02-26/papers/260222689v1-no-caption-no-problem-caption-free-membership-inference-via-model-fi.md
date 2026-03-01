---
layout: default
title: No Caption, No Problem: Caption-Free Membership Inference via Model-Fitted Embeddings
---

# No Caption, No Problem: Caption-Free Membership Inference via Model-Fitted Embeddings
**arXiv**：[2602.22689v1](https://arxiv.org/abs/2602.22689) · [PDF](https://arxiv.org/pdf/2602.22689.pdf)  
**作者**：Joonsung Jeon, Woo Jae Kim, Suhyeon Ha, Sooel Son, Sung-Eui Yoon  

**一句话要点**：提出MoFit框架，通过模型拟合嵌入实现无字幕的成员推断攻击，以解决潜在扩散模型训练数据隐私泄露问题。

**关键词**：成员推断攻击, 潜在扩散模型, 模型拟合嵌入, 隐私审计, 无字幕条件, 图像生成安全

## 3 点简述
- 核心问题：潜在扩散模型在文本到图像生成中可能记忆训练数据，现有成员推断攻击依赖真实字幕，在仅图像可用时失效。
- 方法要点：MoFit分两阶段，先优化图像扰动构建代理，再提取模型拟合嵌入作为条件，放大成员样本的损失响应以增强可分离性。
- 实验或效果：在多个数据集和扩散模型上，MoFit优于基于视觉语言模型字幕的基线，性能接近依赖字幕的方法。

## 摘要（原文）

> Latent diffusion models have achieved remarkable success in high-fidelity text-to-image generation, but their tendency to memorize training data raises critical privacy and intellectual property concerns. Membership inference attacks (MIAs) provide a principled way to audit such memorization by determining whether a given sample was included in training. However, existing approaches assume access to ground-truth captions. This assumption fails in realistic scenarios where only images are available and their textual annotations remain undisclosed, rendering prior methods ineffective when substituted with vision-language model (VLM) captions. In this work, we propose MoFit, a caption-free MIA framework that constructs synthetic conditioning inputs that are explicitly overfitted to the target model's generative manifold. Given a query image, MoFit proceeds in two stages: (i) model-fitted surrogate optimization, where a perturbation applied to the image is optimized to construct a surrogate in regions of the model's unconditional prior learned from member samples, and (ii) surrogate-driven embedding extraction, where a model-fitted embedding is derived from the surrogate and then used as a mismatched condition for the query image. This embedding amplifies conditional loss responses for member samples while leaving hold-outs relatively less affected, thereby enhancing separability in the absence of ground-truth captions. Our comprehensive experiments across multiple datasets and diffusion models demonstrate that MoFit consistently outperforms prior VLM-conditioned baselines and achieves performance competitive with caption-dependent methods.

