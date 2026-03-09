---
layout: default
title: CaTok: Taming Mean Flows for One-Dimensional Causal Image Tokenization
---

# CaTok: Taming Mean Flows for One-Dimensional Causal Image Tokenization
**arXiv**：[2603.06449v1](https://arxiv.org/abs/2603.06449) · [PDF](https://arxiv.org/pdf/2603.06449.pdf)  
**作者**：Yitong Chen, Zuxuan Wu, Xipeng Qiu, Yu-Gang Jiang  

**一句话要点**：提出CaTok一维因果图像分词器，通过MeanFlow解码器解决视觉因果表示难题，支持快速生成与高保真采样。

**关键词**：因果图像分词, 一维视觉表示, MeanFlow解码器, 自回归模型, 图像重建, 视觉基础模型对齐

## 3 点简述
- 核心问题：现有视觉分词器或扩散自编码器难以实现因果对齐，导致序列预测模式不匹配。
- 方法要点：采用MeanFlow解码器，通过时间间隔选择令牌并绑定目标，学习因果一维表示，并引入REPA-A正则化加速训练。
- 实验或效果：在ImageNet重建上达到SOTA，FID 0.75，PSNR 22.53，SSIM 0.674，训练轮次更少，AR模型性能可比领先方法。

## 摘要（原文）

> Autoregressive (AR) language models rely on causal tokenization, but extending this paradigm to vision remains non-trivial. Current visual tokenizers either flatten 2D patches into non-causal sequences or enforce heuristic orderings that misalign with the "next-token prediction" pattern. Recent diffusion autoencoders similarly fall short: conditioning the decoder on all tokens lacks causality, while applying nested dropout mechanism introduces imbalance. To address these challenges, we present CaTok, a 1D causal image tokenizer with a MeanFlow decoder. By selecting tokens over time intervals and binding them to the MeanFlow objective, as illustrated in Fig. 1, CaTok learns causal 1D representations that support both fast one-step generation and high-fidelity multi-step sampling, while naturally capturing diverse visual concepts across token intervals. To further stabilize and accelerate training, we propose a straightforward regularization REPA-A, which aligns encoder features with Vision Foundation Models (VFMs). Experiments demonstrate that CaTok achieves state-of-the-art results on ImageNet reconstruction, reaching 0.75 FID, 22.53 PSNR and 0.674 SSIM with fewer training epochs, and the AR model attains performance comparable to leading approaches.

