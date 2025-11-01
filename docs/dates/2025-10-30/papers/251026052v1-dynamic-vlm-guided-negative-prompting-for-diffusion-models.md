---
layout: default
title: Dynamic VLM-Guided Negative Prompting for Diffusion Models
---

# Dynamic VLM-Guided Negative Prompting for Diffusion Models
**arXiv**：[2510.26052v1](https://arxiv.org/abs/2510.26052) · [PDF](https://arxiv.org/pdf/2510.26052.pdf)  
**作者**：Hoyeon Chang, Seungjin Kim, Yoonseok Choi  

**一句话要点**：提出动态VLM引导负提示方法，以提升扩散模型在去噪过程中的文本-图像对齐。

**关键词**：扩散模型, 负提示, 视觉语言模型, 动态生成, 文本-图像对齐

## 3 点简述
- 传统负提示方法使用固定提示，缺乏上下文适应性。
- 在去噪步骤生成中间图像预测，并查询VLM动态生成负提示。
- 在基准数据集上评估，展示负引导强度与文本-图像对齐的权衡。

## 摘要（原文）

> We propose a novel approach for dynamic negative prompting in diffusion
> models that leverages Vision-Language Models (VLMs) to adaptively generate
> negative prompts during the denoising process. Unlike traditional Negative
> Prompting methods that use fixed negative prompts, our method generates
> intermediate image predictions at specific denoising steps and queries a VLM to
> produce contextually appropriate negative prompts. We evaluate our approach on
> various benchmark datasets and demonstrate the trade-offs between negative
> guidance strength and text-image alignment.

