---
layout: default
title: Yuan-TecSwin: A text conditioned Diffusion model with Swin-transformer blocks
---

# Yuan-TecSwin: A text conditioned Diffusion model with Swin-transformer blocks
**arXiv**：[2512.16586v1](https://arxiv.org/abs/2512.16586) · [PDF](https://arxiv.org/pdf/2512.16586.pdf)  
**作者**：Shaohua Wu, Tong Yu, Shenling Wang, Xudong Zhao  

**一句话要点**：提出Yuan-TecSwin，一种基于Swin-transformer的文本条件扩散模型，以提升图像生成中的长程语义理解能力。

**关键词**：文本条件扩散模型, Swin-transformer, 长程语义建模, 图像生成, FID分数, 非局部建模

## 3 点简述
- 核心问题：CNN的局部性限制了扩散模型在图像生成中对长程语义信息的理解能力。
- 方法要点：用Swin-transformer块替换U形架构中的CNN块，增强特征提取和图像恢复的非局部建模能力。
- 实验或效果：在ImageNet生成基准上达到1.37的FID分数，推理性能提升10%，生成图像难以与人类绘画区分。

## 摘要（原文）

> Diffusion models have shown remarkable capacity in image synthesis based on their U-shaped architecture and convolutional neural networks (CNN) as basic blocks. The locality of the convolution operation in CNN may limit the model's ability to understand long-range semantic information. To address this issue, we propose Yuan-TecSwin, a text-conditioned diffusion model with Swin-transformer in this work. The Swin-transformer blocks take the place of CNN blocks in the encoder and decoder, to improve the non-local modeling ability in feature extraction and image restoration. The text-image alignment is improved with a well-chosen text encoder, effective utilization of text embedding, and careful design in the incorporation of text condition. Using an adapted time step to search in different diffusion stages, inference performance is further improved by 10%. Yuan-TecSwin achieves the state-of-the-art FID score of 1.37 on ImageNet generation benchmark, without any additional models at different denoising stages. In a side-by-side comparison, we find it difficult for human interviewees to tell the model-generated images from the human-painted ones.

