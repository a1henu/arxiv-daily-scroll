---
layout: default
title: Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers
---

# Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers
**arXiv**：[2512.16615v1](https://arxiv.org/abs/2512.16615) · [PDF](https://arxiv.org/pdf/2512.16615.pdf)  
**作者**：Yifan Zhou, Zeqi Xiao, Tianyi Wei, Shuai Yang, Xingang Pan  

**一句话要点**：提出可训练的对数线性稀疏注意力机制，以高效处理扩散变换器中的长序列生成问题。

**关键词**：扩散变换器, 稀疏注意力, 长序列生成, 分层结构, 高效训练, 图像生成

## 3 点简述
- 扩散变换器自注意力成本二次方增长，限制长序列扩展；现有Top-K稀疏方法仍存在选择成本高和K值随序列增长而增加的问题。
- 引入分层Top-K选择和分层键值丰富机制，将选择和注意力成本从二次方降至对数线性，并保持全局上下文。
- 在256x256像素序列上，注意力推理加速28.27倍，训练加速6.09倍，同时维持生成质量，代码已开源。

## 摘要（原文）

> Diffusion Transformers (DiTs) set the state of the art in visual generation, yet their quadratic self-attention cost fundamentally limits scaling to long token sequences. Recent Top-K sparse attention approaches reduce the computation of DiTs by compressing tokens into block-wise representation and selecting a small set of relevant key blocks, but still suffer from (i) quadratic selection cost on compressed tokens and (ii) increasing K required to maintain model quality as sequences grow. We identify that their inefficiency is due to the single-level design, as a single coarse level is insufficient to represent the global structure. In this paper, we introduce Log-linear Sparse Attention (LLSA), a trainable sparse attention mechanism for extremely long token sequences that reduces both selection and attention costs from quadratic to log-linear complexity by utilizing a hierarchical structure. LLSA performs hierarchical Top-K selection, progressively adopting sparse Top-K selection with the indices found at the previous level, and introduces a Hierarchical KV Enrichment mechanism that preserves global context while using fewer tokens of different granularity during attention computation. To support efficient training, we develop a high-performance GPU implementation that uses only sparse indices for both the forward and backward passes, eliminating the need for dense attention masks. We evaluate LLSA on high-resolution pixel-space image generation without using patchification and VAE encoding. LLSA accelerates attention inference by 28.27x and DiT training by 6.09x on 256x256 pixel token sequences, while maintaining generation quality. The results demonstrate that LLSA offers a promising direction for training long-sequence DiTs efficiently. Code is available at: https://github.com/SingleZombie/LLSA

