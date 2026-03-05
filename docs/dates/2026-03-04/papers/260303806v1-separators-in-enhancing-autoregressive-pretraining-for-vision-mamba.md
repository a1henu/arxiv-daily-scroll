---
layout: default
title: Separators in Enhancing Autoregressive Pretraining for Vision Mamba
---

# Separators in Enhancing Autoregressive Pretraining for Vision Mamba
**arXiv**：[2603.03806v1](https://arxiv.org/abs/2603.03806) · [PDF](https://arxiv.org/pdf/2603.03806.pdf)  
**作者**：Hanpeng Liu, Zidan Wang, Shuoxi Zhang, Kaiyuan Gao, Kun He  

**一句话要点**：提出STAR方法以增强Vision Mamba的自回归预训练，通过插入分隔符扩展输入序列长度。

**关键词**：Vision Mamba, 自回归预训练, 长序列处理, 图像分隔符, 状态空间模型

## 3 点简述
- 核心问题：当前自回归预训练方法受限于短序列，未能充分利用Mamba处理长序列的优势。
- 方法要点：引入STAR，在图像前插入相同分隔符以区分不同图像，扩展输入序列长度四倍。
- 实验或效果：STAR-B模型在ImageNet-1k上达到83.5%准确率，在Vision Mamba中表现竞争性。

## 摘要（原文）

> The state space model Mamba has recently emerged as a promising paradigm in computer vision, attracting significant attention due to its efficient processing of long sequence tasks. Mamba's inherent causal mechanism renders it particularly suitable for autoregressive pretraining. However, current autoregressive pretraining methods are constrained to short sequence tasks, failing to fully exploit Mamba's prowess in handling extended sequences. To address this limitation, we introduce an innovative autoregressive pretraining method for Vision Mamba that substantially extends the input sequence length. We introduce new \textbf{S}epara\textbf{T}ors for \textbf{A}uto\textbf{R}egressive pretraining to demarcate and differentiate between different images, known as \textbf{STAR}. Specifically, we insert identical separators before each image to demarcate its inception. This strategy enables us to quadruple the input sequence length of Vision Mamba while preserving the original dimensions of the dataset images. Employing this long sequence pretraining technique, our STAR-B model achieved an impressive accuracy of 83.5\% on ImageNet-1k, which is highly competitive in Vision Mamba. These results underscore the potential of our method in enhancing the performance of vision models through improved leveraging of long-range dependencies.

