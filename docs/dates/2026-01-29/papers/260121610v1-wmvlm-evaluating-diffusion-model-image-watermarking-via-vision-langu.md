---
layout: default
title: WMVLM: Evaluating Diffusion Model Image Watermarking via Vision-Language Models
---

# WMVLM: Evaluating Diffusion Model Image Watermarking via Vision-Language Models
**arXiv**：[2601.21610v1](https://arxiv.org/abs/2601.21610) · [PDF](https://arxiv.org/pdf/2601.21610.pdf)  
**作者**：Zijin Yang, Yu Sun, Kejiang Chen, Jiawei Zhao, Jun Jiang, Weiming Zhang, Nenghai Yu  

**一句话要点**：提出WMVLM框架，通过视觉语言模型统一评估扩散模型图像水印的质量与安全性。

**关键词**：扩散模型水印评估, 视觉语言模型, 残差水印, 语义水印, 可解释性框架, 三阶段训练

## 3 点简述
- 核心问题：现有水印评估方法缺乏统一框架，忽视可解释性和全面安全考量。
- 方法要点：重新定义残差和语义水印的评估指标，引入三阶段训练策略实现分类、评分和文本生成。
- 实验或效果：WMVLM在多个数据集、扩散模型和水印方法上表现优于现有视觉语言模型，具有强泛化能力。

## 摘要（原文）

> Digital watermarking is essential for securing generated images from diffusion models. Accurate watermark evaluation is critical for algorithm development, yet existing methods have significant limitations: they lack a unified framework for both residual and semantic watermarks, provide results without interpretability, neglect comprehensive security considerations, and often use inappropriate metrics for semantic watermarks. To address these gaps, we propose WMVLM, the first unified and interpretable evaluation framework for diffusion model image watermarking via vision-language models (VLMs). We redefine quality and security metrics for each watermark type: residual watermarks are evaluated by artifact strength and erasure resistance, while semantic watermarks are assessed through latent distribution shifts. Moreover, we introduce a three-stage training strategy to progressively enable the model to achieve classification, scoring, and interpretable text generation. Experiments show WMVLM outperforms state-of-the-art VLMs with strong generalization across datasets, diffusion models, and watermarking methods.

