---
layout: default
title: Dense2MoE: Restructuring Diffusion Transformer to MoE for Efficient Text-to-Image Generation
---

# Dense2MoE: Restructuring Diffusion Transformer to MoE for Efficient Text-to-Image Generation
**arXiv**：[2510.09094v1](https://arxiv.org/abs/2510.09094) · [PDF](https://arxiv.org/pdf/2510.09094.pdf)  
**作者**：Youwei Zheng, Yuxi Ren, Xin Xia, Xuefeng Xiao, Xiaohua Xie  
**一句话要点**：提出Dense2MoE将扩散Transformer转换为MoE结构以高效文本到图像生成
**关键词**：文本到图像生成, 扩散Transformer, 专家混合, 结构化稀疏化, 知识蒸馏, 参数效率

## 3 点简述
- 扩散Transformer参数大导致推理开销高，现有剪枝方法易造成性能下降
- 将DiT块中前馈网络替换为MoE层，并引入块混合选择性激活以结构化稀疏化
- 实验显示激活参数减少60%，性能保持原水平，优于剪枝方法

## 摘要（原文）

> Diffusion Transformer (DiT) has demonstrated remarkable performance in
> text-to-image generation; however, its large parameter size results in
> substantial inference overhead. Existing parameter compression methods
> primarily focus on pruning, but aggressive pruning often leads to severe
> performance degradation due to reduced model capacity. To address this
> limitation, we pioneer the transformation of a dense DiT into a Mixture of
> Experts (MoE) for structured sparsification, reducing the number of activated
> parameters while preserving model capacity. Specifically, we replace the
> Feed-Forward Networks (FFNs) in DiT Blocks with MoE layers, reducing the number
> of activated parameters in the FFNs by 62.5\%. Furthermore, we propose the
> Mixture of Blocks (MoB) to selectively activate DiT blocks, thereby further
> enhancing sparsity. To ensure an effective dense-to-MoE conversion, we design a
> multi-step distillation pipeline, incorporating Taylor metric-based expert
> initialization, knowledge distillation with load balancing, and group feature
> loss for MoB optimization. We transform large diffusion transformers (e.g.,
> FLUX.1 [dev]) into an MoE structure, reducing activated parameters by 60\%
> while maintaining original performance and surpassing pruning-based approaches
> in extensive experiments. Overall, Dense2MoE establishes a new paradigm for
> efficient text-to-image generation.

