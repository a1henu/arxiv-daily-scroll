---
layout: default
title: DPAR: Dynamic Patchification for Efficient Autoregressive Visual Generation
---

# DPAR: Dynamic Patchification for Efficient Autoregressive Visual Generation
**arXiv**：[2512.21867v1](https://arxiv.org/abs/2512.21867) · [PDF](https://arxiv.org/pdf/2512.21867.pdf)  
**作者**：Divyansh Srivastava, Akshay Mehra, Pranav Maneriker, Debopam Sanyal, Vishnu Raj, Vijay Kamarshi, Fan Du, Joshua Kimball  

**一句话要点**：提出DPAR动态分块方法，以降低自回归视觉生成的计算和内存开销。

**关键词**：自回归图像生成, 动态分块, 计算效率优化, 标记聚合, 信息熵预测, 多模态兼容

## 3 点简述
- 解码器自回归图像生成中固定长度标记化导致计算成本随分辨率平方增长。
- DPAR利用轻量无监督模型预测熵动态聚合标记为可变数量分块，优化计算分配。
- 实验显示DPAR减少标记数达2.06倍，训练FLOPs降低40%，FID改进27.1%。

## 摘要（原文）

> Decoder-only autoregressive image generation typically relies on fixed-length tokenization schemes whose token counts grow quadratically with resolution, substantially increasing the computational and memory demands of attention. We present DPAR, a novel decoder-only autoregressive model that dynamically aggregates image tokens into a variable number of patches for efficient image generation. Our work is the first to demonstrate that next-token prediction entropy from a lightweight and unsupervised autoregressive model provides a reliable criterion for merging tokens into larger patches based on information content. DPAR makes minimal modifications to the standard decoder architecture, ensuring compatibility with multimodal generation frameworks and allocating more compute to generation of high-information image regions. Further, we demonstrate that training with dynamically sized patches yields representations that are robust to patch boundaries, allowing DPAR to scale to larger patch sizes at inference. DPAR reduces token count by 1.81x and 2.06x on Imagenet 256 and 384 generation resolution respectively, leading to a reduction of up to 40% FLOPs in training costs. Further, our method exhibits faster convergence and improves FID by up to 27.1% relative to baseline models.

