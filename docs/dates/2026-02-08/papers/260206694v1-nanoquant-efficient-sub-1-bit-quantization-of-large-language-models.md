---
layout: default
title: NanoQuant: Efficient Sub-1-Bit Quantization of Large Language Models
---

# NanoQuant: Efficient Sub-1-Bit Quantization of Large Language Models
**arXiv**：[2602.06694v1](https://arxiv.org/abs/2602.06694) · [PDF](https://arxiv.org/pdf/2602.06694.pdf)  
**作者**：Hyochan Chong, Dongkyu Kim, Changdong Kim, Minseop Choi  

**一句话要点**：提出NanoQuant方法，通过低秩二值分解实现大语言模型的高效亚1比特量化部署。

**关键词**：大语言模型量化, 后训练量化, 低秩二值分解, 亚1比特压缩, 高效部署

## 3 点简述
- 现有方法难以高效压缩大语言模型至二值或亚1比特级别，需大量数据或额外存储。
- NanoQuant将量化建模为低秩二值分解问题，使用ADMM初始化并微调二值矩阵和尺度参数。
- 该方法在低内存后训练量化中建立新帕累托前沿，实现亚1比特压缩下的先进精度，如Llama2-70B压缩25.8倍。

## 摘要（原文）

> Weight-only quantization has become a standard approach for efficiently serving large language models (LLMs). However, existing methods fail to efficiently compress models to binary (1-bit) levels, as they either require large amounts of data and compute or incur additional storage. In this work, we propose NanoQuant, the first post-training quantization (PTQ) method to compress LLMs to both binary and sub-1-bit levels. NanoQuant formulates quantization as a low-rank binary factorization problem, and compresses full-precision weights to low-rank binary matrices and scales. Specifically, it utilizes an efficient alternating direction method of multipliers (ADMM) method to precisely initialize latent binary matrices and scales, and then tune the initialized parameters through a block and model reconstruction process. Consequently, NanoQuant establishes a new Pareto frontier in low-memory post-training quantization, achieving state-of-the-art accuracy even at sub-1-bit compression rates. NanoQuant makes large-scale deployment feasible on consumer hardware. For example, it compresses Llama2-70B by 25.8$\times$ in just 13 hours on a single H100, enabling a 70B model to operate on a consumer 8 GB GPU.

