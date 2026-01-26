---
layout: default
title: SALAD: Achieve High-Sparsity Attention via Efficient Linear Attention Tuning for Video Diffusion Transformer
---

# SALAD: Achieve High-Sparsity Attention via Efficient Linear Attention Tuning for Video Diffusion Transformer
**arXiv**：[2601.16515v1](https://arxiv.org/abs/2601.16515) · [PDF](https://arxiv.org/pdf/2601.16515.pdf)  
**作者**：Tongcheng Fang, Hanling Zhang, Ruiqi Xie, Zhuo Han, Xin Tao, Tianchen Zhao, Pengfei Wan, Wenbo Ding, Wanli Ouyang, Xuefei Ning, Yu Wang  

**一句话要点**：提出SALAD方法，通过高效线性注意力微调实现高稀疏性注意力，以加速视频扩散Transformer推理。

**关键词**：视频扩散Transformer, 稀疏注意力, 线性注意力, 高效微调, 推理加速

## 3 点简述
- 视频扩散Transformer中全注意力的二次复杂度导致高计算延迟，现有稀疏方法在稀疏度或训练成本上受限。
- SALAD引入轻量线性注意力分支与稀疏注意力并行，结合输入相关门控机制平衡分支，实现高稀疏度。
- 该方法达到90%稀疏度和1.72倍推理加速，生成质量接近全注意力基线，仅需少量数据和训练步骤。

## 摘要（原文）

> Diffusion Transformers have recently demonstrated remarkable performance in video generation. However, the long input sequences result in high computational latency due to the quadratic complexity of full attention. Various sparse attention mechanisms have been proposed. Training-free sparse attention is constrained by limited sparsity and thus offers modest acceleration, whereas training-based methods can reach much higher sparsity but demand substantial data and computation for training. In this work, we propose SALAD, introducing a lightweight linear attention branch in parallel with the sparse attention. By incorporating an input-dependent gating mechanism to finely balance the two branches, our method attains 90% sparsity and 1.72x inference speedup, while maintaining generation quality comparable to the full attention baseline. Moreover, our finetuning process is highly efficient, requiring only 2,000 video samples and 1,600 training steps with a batch size of 8.

