---
layout: default
title: GPUTOK: GPU Accelerated Byte Level BPE Tokenization
---

# GPUTOK: GPU Accelerated Byte Level BPE Tokenization
**arXiv**：[2603.02597v1](https://arxiv.org/abs/2603.02597) · [PDF](https://arxiv.org/pdf/2603.02597.pdf)  
**作者**：Venu Gopal Kadamba, Kanishkha Jaisankar  

**一句话要点**：提出GPU加速的字节级BPE分词器，以解决长上下文语言模型中CPU分词器性能瓶颈问题。

**关键词**：GPU加速, 字节级BPE分词, 长上下文处理, 性能优化, cuCollections, CUB归约

## 3 点简述
- 核心问题：CPU分词器在百万令牌上下文窗口中成为主要性能瓶颈，导致GPU闲置。
- 方法要点：基于GPU实现字节级BPE分词，采用cuCollections静态映射和CUB归约优化。
- 实验或效果：在131k令牌序列上，优化版本比tiktoken快约1.7倍，输出质量与CPU版本相近。

## 摘要（原文）

> As large language models move toward million-token context windows, CPU tokenizers become a major slowdown because they process text one step at a time while powerful GPUs sit unused. We built a GPU-based byte-level BPE tokenizer that follows GPT-2's merge rules. It includes a basic BlockBPE-style kernel and a faster, optimized version that uses cuCollections static map, CUB reductions, and a pybind11 interface for Python.
>   On WikiText103 sequences up to 131k tokens, the optimized GPU tokenizer produces the same tokens as a CPU version and, for the longest inputs, is about 1.7x faster than tiktoken and about 7.6x faster than the HuggingFace GPT-2 tokenizer. Nsight profiling shows that 70-80% of CUDA API time goes to memory allocation, so adding memory pooling should give the biggest speed boost next. Tests on generation tasks using WikiText103 prompts show that our GPU tokenizer's outputs stay within about one percentage point of tiktoken and HuggingFace GPT-2 on similarity and overlap metrics, meaning it keeps output quality while making long-context inference more practical.

