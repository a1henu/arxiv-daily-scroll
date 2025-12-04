---
layout: default
title: ConvRot: Rotation-Based Plug-and-Play 4-bit Quantization for Diffusion Transformers
---

# ConvRot: Rotation-Based Plug-and-Play 4-bit Quantization for Diffusion Transformers
**arXiv**：[2512.03673v1](https://arxiv.org/abs/2512.03673) · [PDF](https://arxiv.org/pdf/2512.03673.pdf)  
**作者**：Feice Huang, Zuliang Han, Xing Zhou, Yihuang Chen, Lifei Zhu, Haoqian Wang  

**一句话要点**：提出ConvRot，一种基于旋转的4位量化方法，用于扩散变换器的即插即用部署。

**关键词**：扩散变换器, 4位量化, 旋转技术, 即插即用模块, 内存优化, 推理加速

## 3 点简述
- 扩散变换器模型增大导致内存和延迟问题，现有旋转方法处理行向异常值困难且开销大。
- ConvRot利用正则Hadamard变换进行分组旋转，抑制行列异常值，复杂度从二次降至线性。
- 实验在FLUX.1-dev上实现2.26倍加速和4.05倍内存减少，保持图像质量，支持W4A4推理无需重训练。

## 摘要（原文）

> Diffusion transformers have demonstrated strong capabilities in generating high-quality images. However, as model size increases, the growing memory footprint and inference latency pose significant challenges for practical deployment. Recent studies in large language models (LLMs) show that rotation-based techniques can smooth outliers and enable 4-bit quantization, but these approaches often incur substantial overhead and struggle with row-wise outliers in diffusion transformers. To address these challenges, we propose ConvRot, a group-wise rotation-based quantization method that leverages regular Hadamard transform (RHT) to suppress both row-wise and column-wise outliers while reducing complexity from quadratic to linear. Building on this, we design ConvLinear4bit, a plug-and-play module that integrates rotation, quantization, GEMM, and dequantization, enabling W4A4 inference without retraining and preserving visual quality. Experiments on FLUX.1-dev demonstrate a 2.26$\times$ speedup and 4.05$\times$ memory reduction while maintaining image fidelity. To our knowledge, this is the first application of rotation-based quantization for plug-and-play W4A4 inference in diffusion transformers.

