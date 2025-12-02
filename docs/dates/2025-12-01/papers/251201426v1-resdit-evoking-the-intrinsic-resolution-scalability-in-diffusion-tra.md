---
layout: default
title: ResDiT: Evoking the Intrinsic Resolution Scalability in Diffusion Transformers
---

# ResDiT: Evoking the Intrinsic Resolution Scalability in Diffusion Transformers
**arXiv**：[2512.01426v1](https://arxiv.org/abs/2512.01426) · [PDF](https://arxiv.org/pdf/2512.01426.pdf)  
**作者**：Yiyang Ma, Feng Zhou, Xuedan Yin, Pu Cao, Yonghao Dang, Jianqin Yin  

**一句话要点**：提出ResDiT以解决扩散变换器在高分辨率图像合成中的布局崩溃和纹理退化问题

**关键词**：扩散变换器, 高分辨率图像合成, 位置嵌入缩放, 局部增强机制, 训练免费方法, 空间布局校正

## 3 点简述
- 核心问题：预训练扩散变换器在高分辨率合成时因位置嵌入外推错误导致空间布局崩溃和纹理保真度下降
- 方法要点：引入训练免费的位置嵌入缩放技术校正位置编码，并基于基础分辨率局部注意力设计局部增强机制以提升细节
- 实验或效果：评估显示ResDiT能一致生成高保真高分辨率图像，并无缝集成到空间控制生成等下游任务中

## 摘要（原文）

> Leveraging pre-trained Diffusion Transformers (DiTs) for high-resolution (HR) image synthesis often leads to spatial layout collapse and degraded texture fidelity. Prior work mitigates these issues with complex pipelines that first perform a base-resolution (i.e., training-resolution) denoising process to guide HR generation. We instead explore the intrinsic generative mechanisms of DiTs and propose ResDiT, a training-free method that scales resolution efficiently. We identify the core factor governing spatial layout, position embeddings (PEs), and show that the original PEs encode incorrect positional information when extrapolated to HR, which triggers layout collapse. To address this, we introduce a PE scaling technique that rectifies positional encoding under resolution changes. To further remedy low-fidelity details, we develop a local-enhancement mechanism grounded in base-resolution local attention. We design a patch-level fusion module that aggregates global and local cues, together with a Gaussian-weighted splicing strategy that eliminates grid artifacts. Comprehensive evaluations demonstrate that ResDiT consistently delivers high-fidelity, high-resolution image synthesis and integrates seamlessly with downstream tasks, including spatially controlled generation.

