---
layout: default
title: Dynamic Chunking Diffusion Transformer
---

# Dynamic Chunking Diffusion Transformer
**arXiv**：[2603.06351v1](https://arxiv.org/abs/2603.06351) · [PDF](https://arxiv.org/pdf/2603.06351.pdf)  
**作者**：Akash Haridas, Utkarsh Saxena, Parsa Ashrafi Fashi, Mehdi Rezagholizadeh, Vikram Appia, Emad Barsoum  

**一句话要点**：提出动态分块扩散变换器，通过自适应压缩改进图像生成效率与质量。

**关键词**：扩散变换器, 自适应压缩, 图像生成, 动态计算, 端到端训练

## 3 点简述
- 核心问题：传统扩散变换器使用固定分块处理图像，忽略区域细节差异和去噪过程动态性，导致计算资源浪费。
- 方法要点：引入学习型编码器-路由器-解码器框架，以数据依赖方式自适应压缩输入为更短令牌序列，实现端到端训练。
- 实验或效果：在ImageNet 256×256上，DC-DiT在参数匹配和FLOP匹配基准上提升FID和Inception Score，并支持从预训练模型高效微调。

## 摘要（原文）

> Diffusion Transformers process images as fixed-length sequences of tokens produced by a static $\textit{patchify}$ operation. While effective, this design spends uniform compute on low- and high-information regions alike, ignoring that images contain regions of varying detail and that the denoising process progresses from coarse structure at early timesteps to fine detail at late timesteps. We introduce the Dynamic Chunking Diffusion Transformer (DC-DiT), which augments the DiT backbone with a learned encoder-router-decoder scaffold that adaptively compresses the 2D input into a shorter token sequence in a data-dependent manner using a chunking mechanism learned end-to-end with diffusion training. The mechanism learns to compress uniform background regions into fewer tokens and detail-rich regions into more tokens, with meaningful visual segmentations emerging without explicit supervision. Furthermore, it also learns to adapt its compression across diffusion timesteps, using fewer tokens at noisy stages and more tokens as fine details emerge. On class-conditional ImageNet $256{\times}256$, DC-DiT consistently improves FID and Inception Score over both parameter-matched and FLOP-matched DiT baselines across $4{\times}$ and $16{\times}$ compression, showing this is a promising technique with potential further applications to pixel-space, video and 3D generation. Beyond accuracy, DC-DiT is practical: it can be upcycled from pretrained DiT checkpoints with minimal post-training compute (up to $8{\times}$ fewer training steps) and composes with other dynamic computation methods to further reduce generation FLOPs.

