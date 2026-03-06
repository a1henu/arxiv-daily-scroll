---
layout: default
title: Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes
---

# Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes
**arXiv**：[2603.05454v1](https://arxiv.org/abs/2603.05454) · [PDF](https://arxiv.org/pdf/2603.05454.pdf)  
**作者**：Pengxiang Li, Joey Tsai, Hongwei Xue, Kunyu Shi, Shilin Yan  

**一句话要点**：提出最长稳定前缀调度器以解决扩散语言模型推理中的缓存碎片化问题

**关键词**：扩散语言模型, 推理加速, 解码调度, KV缓存优化, 训练无关方法

## 3 点简述
- 核心问题：标准解码调度器导致KV缓存碎片化，降低推理效率
- 方法要点：基于单次前向传播动态识别并原子提交连续稳定前缀
- 实验或效果：在多项任务上加速推理达3.4倍，保持或提升输出质量

## 摘要（原文）

> Diffusion Language Models (DLMs) promise highly parallel text generation, yet their practical inference speed is often bottlenecked by suboptimal decoding schedulers. Standard approaches rely on 'scattered acceptance'-committing high confidence tokens at disjoint positions throughout the sequence. This approach inadvertently fractures the Key-Value (KV) cache, destroys memory locality, and forces the model into costly, repeated repairs across unstable token boundaries. To resolve this, we present the Longest Stable Prefix (LSP) scheduler, a training-free and model-agnostic inference paradigm based on monolithic prefix absorption. In each denoising step, LSP evaluates token stability via a single forward pass, dynamically identifies a contiguous left-aligned block of stable predictions, and snaps its boundary to natural linguistic or structural delimiters before an atomic commitment. This prefix-first topology yields dual benefits: systemically, it converts fragmented KV cache updates into efficient, contiguous appends; algorithmically, it preserves bidirectional lookahead over a geometrically shrinking active suffix, drastically reducing token flip rates and denoiser calls. Extensive evaluations on LLaDA-8B and Dream-7B demonstrate that LSP accelerates inference by up to 3.4x across rigorous benchmarks including mathematical reasoning, code generation, multilingual (CJK) tasks, and creative writing while matching or slightly improving output quality. By fundamentally restructuring the commitment topology, LSP bridges the gap between the theoretical parallelism of DLMs and practical hardware efficiency.

