---
layout: default
title: Attentive Convolution: Unifying the Expressivity of Self-Attention with Convolutional Efficiency
---

# Attentive Convolution: Unifying the Expressivity of Self-Attention with Convolutional Efficiency
**arXiv**：[2510.20092v1](https://arxiv.org/abs/2510.20092) · [PDF](https://arxiv.org/pdf/2510.20092.pdf)  
**作者**：Hao Yu, Haoyu Chen, Yan Jiang, Wei Peng, Zhaodong Sun, Samuel Kaski, Guoying Zhao  

**一句话要点**：提出Attentive Convolution以统一自注意力的表达力与卷积的效率

**关键词**：自注意力机制, 卷积神经网络, 图像分类, 图像生成, 模型效率, 自适应路由

## 3 点简述
- 自注意力表达力强但复杂度高，卷积效率高但性能存在差距
- 引入自适应路由和侧向抑制原则，设计ATConv卷积算子
- 在ImageNet分类和扩散生成任务中，ATConv超越自注意力机制

## 摘要（原文）

> Self-attention (SA) has become the cornerstone of modern vision backbones for
> its powerful expressivity over traditional Convolutions (Conv). However, its
> quadratic complexity remains a critical bottleneck for practical applications.
> Given that Conv offers linear complexity and strong visual priors, continuing
> efforts have been made to promote the renaissance of Conv. However, a
> persistent performance chasm remains, highlighting that these modernizations
> have not yet captured the intrinsic expressivity that defines SA. In this
> paper, we re-examine the design of the CNNs, directed by a key question: what
> principles give SA its edge over Conv? As a result, we reveal two fundamental
> insights that challenge the long-standing design intuitions in prior research
> (e.g., Receptive field). The two findings are: (1) \textit{Adaptive routing}:
> SA dynamically regulates positional information flow according to semantic
> content, whereas Conv employs static kernels uniformly across all positions.
> (2) \textit{Lateral inhibition}: SA induces score competition among token
> weighting, effectively suppressing redundancy and sharpening representations,
> whereas Conv filters lack such inhibitory dynamics and exhibit considerable
> redundancy. Based on this, we propose \textit{Attentive Convolution} (ATConv),
> a principled reformulation of the convolutional operator that intrinsically
> injects these principles. Interestingly, with only $3\times3$ kernels, ATConv
> consistently outperforms various SA mechanisms in fundamental vision tasks.
> Building on ATConv, we introduce AttNet, a CNN family that can attain
> \textbf{84.4\%} ImageNet-1K Top-1 accuracy with only 27M parameters. In
> diffusion-based image generation, replacing all SA with the proposed $3\times
> 3$ ATConv in SiT-XL/2 reduces ImageNet FID by 0.15 in 400k steps with faster
> sampling. Code is available at: github.com/price112/Attentive-Convolution.

