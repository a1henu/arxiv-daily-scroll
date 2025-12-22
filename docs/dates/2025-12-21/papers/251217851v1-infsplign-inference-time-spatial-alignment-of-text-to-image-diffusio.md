---
layout: default
title: InfSplign: Inference-Time Spatial Alignment of Text-to-Image Diffusion Models
---

# InfSplign: Inference-Time Spatial Alignment of Text-to-Image Diffusion Models
**arXiv**：[2512.17851v1](https://arxiv.org/abs/2512.17851) · [PDF](https://arxiv.org/pdf/2512.17851.pdf)  
**作者**：Sarah Rastegar, Violeta Chatalbasheva, Sieger Falkena, Anuj Singh, Yanbo Wang, Tejas Gokhale, Hamid Palangi, Hadi Jamali-Rad  

**一句话要点**：提出InfSplign以在推理时提升文本到图像扩散模型的空间对齐能力

**关键词**：文本到图像生成, 空间对齐, 推理时优化, 扩散模型, 交叉注意力

## 3 点简述
- 核心问题：T2I扩散模型常因训练数据缺乏细粒度空间监督和文本嵌入无法编码空间语义而难以准确捕捉文本提示中的空间关系。
- 方法要点：通过在每个去噪步骤中调整噪声，利用从骨干解码器提取的多层次交叉注意力图，以复合损失强制对象放置准确和存在平衡。
- 实验或效果：在VISOR和T2I-CompBench上评估，InfSplign优于现有推理时基线，甚至超越基于微调的方法，实现新SOTA。

## 摘要（原文）

> Text-to-image (T2I) diffusion models generate high-quality images but often fail to capture the spatial relations specified in text prompts. This limitation can be traced to two factors: lack of fine-grained spatial supervision in training data and inability of text embeddings to encode spatial semantics. We introduce InfSplign, a training-free inference-time method that improves spatial alignment by adjusting the noise through a compound loss in every denoising step. Proposed loss leverages different levels of cross-attention maps extracted from the backbone decoder to enforce accurate object placement and a balanced object presence during sampling. The method is lightweight, plug-and-play, and compatible with any diffusion backbone. Our comprehensive evaluations on VISOR and T2I-CompBench show that InfSplign establishes a new state-of-the-art (to the best of our knowledge), achieving substantial performance gains over the strongest existing inference-time baselines and even outperforming the fine-tuning-based methods. Codebase is available at GitHub.

