---
layout: default
title: RevFFN: Memory-Efficient Full-Parameter Fine-Tuning of Mixture-of-Experts LLMs with Reversible Blocks
---

# RevFFN: Memory-Efficient Full-Parameter Fine-Tuning of Mixture-of-Experts LLMs with Reversible Blocks
**arXiv**：[2512.20920v1](https://arxiv.org/abs/2512.20920) · [PDF](https://arxiv.org/pdf/2512.20920.pdf)  
**作者**：Ningyuan Liu, Jing Yang, Kaitong Cai, Keze Wang  

**一句话要点**：提出RevFFN以解决MoE大语言模型全参数微调的内存瓶颈问题

**关键词**：可逆Transformer, 全参数微调, 内存优化, MoE大语言模型, 单GPU训练

## 3 点简述
- 全参数微调大语言模型时，缓存中间激活导致内存开销巨大
- 采用可逆Transformer块，通过反向传播重构输入，减少内存占用
- 在单GPU上实现高效全参数微调，保持MoE架构表达能力

## 摘要（原文）

> Full parameter fine tuning is a key technique for adapting large language models (LLMs) to downstream tasks, but it incurs substantial memory overhead due to the need to cache extensive intermediate activations for backpropagation. This bottleneck makes full fine tuning of contemporary large scale LLMs challenging in practice. Existing distributed training frameworks such as DeepSpeed alleviate this issue using techniques like ZeRO and FSDP, which rely on multi GPU memory or CPU offloading, but often require additional hardware resources and reduce training speed. We introduce RevFFN, a memory efficient fine tuning paradigm for mixture of experts (MoE) LLMs. RevFFN employs carefully designed reversible Transformer blocks that allow reconstruction of layer input activations from outputs during backpropagation, eliminating the need to store most intermediate activations in memory. While preserving the expressive capacity of MoE architectures, this approach significantly reduces peak memory consumption for full parameter fine tuning. As a result, RevFFN enables efficient full fine tuning on a single consumer grade or server grade GPU.

