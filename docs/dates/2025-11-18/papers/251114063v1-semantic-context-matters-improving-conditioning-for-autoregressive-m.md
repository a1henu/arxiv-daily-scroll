---
layout: default
title: Semantic Context Matters: Improving Conditioning for Autoregressive Models
---

# Semantic Context Matters: Improving Conditioning for Autoregressive Models
**arXiv**：[2511.14063v1](https://arxiv.org/abs/2511.14063) · [PDF](https://arxiv.org/pdf/2511.14063.pdf)  
**作者**：Dongyang Jin, Ryan Xu, Jianhao Zeng, Rui Lan, Yancheng Bai, Lei Sun, Xiangxiang Chu  

**一句话要点**：提出SCAR方法以增强自回归模型的语义条件，提升图像编辑性能

**关键词**：自回归模型, 图像编辑, 语义条件, 预填充技术, 可控生成

## 3 点简述
- 自回归模型在图像生成中条件弱且效率低，导致指令遵循差和视觉伪影
- SCAR引入压缩语义预填充和语义对齐指导，强化语义编码与解码对齐
- 在指令编辑和可控生成基准上实现更高视觉保真度和语义对齐，优于现有方法

## 摘要（原文）

> Recently, autoregressive (AR) models have shown strong potential in image generation, offering better scalability and easier integration with unified multi-modal systems compared to diffusion-based methods. However, extending AR models to general image editing remains challenging due to weak and inefficient conditioning, often leading to poor instruction adherence and visual artifacts. To address this, we propose SCAR, a Semantic-Context-driven method for Autoregressive models. SCAR introduces two key components: Compressed Semantic Prefilling, which encodes high-level semantics into a compact and efficient prefix, and Semantic Alignment Guidance, which aligns the last visual hidden states with target semantics during autoregressive decoding to enhance instruction fidelity. Unlike decoding-stage injection methods, SCAR builds upon the flexibility and generality of vector-quantized-based prefilling while overcoming its semantic limitations and high cost. It generalizes across both next-token and next-set AR paradigms with minimal architectural changes. SCAR achieves superior visual fidelity and semantic alignment on both instruction editing and controllable generation benchmarks, outperforming prior AR-based methods while maintaining controllability. All code will be released.

