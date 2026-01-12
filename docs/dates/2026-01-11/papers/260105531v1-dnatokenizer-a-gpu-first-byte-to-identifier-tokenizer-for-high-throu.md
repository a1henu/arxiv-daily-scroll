---
layout: default
title: DNATokenizer: A GPU-First Byte-to-Identifier Tokenizer for High-Throughput DNA Language Models
---

# DNATokenizer: A GPU-First Byte-to-Identifier Tokenizer for High-Throughput DNA Language Models
**arXiv**：[2601.05531v1](https://arxiv.org/abs/2601.05531) · [PDF](https://arxiv.org/pdf/2601.05531.pdf)  
**作者**：Eliatan Niktab, Hardip Patel  

**一句话要点**：提出DNATok，一种GPU优先的字节到标识符分词系统，以解决DNA语言模型高吞吐量训练和推理中的分词瓶颈问题。

**关键词**：DNA语言模型, 分词系统, GPU加速, 高吞吐量, 字节查找表, 流式处理

## 3 点简述
- 核心问题：DNA序列分词在系统层面成为瓶颈，标准分词器在数十亿碱基输入时主导运行时间，影响模型效率。
- 方法要点：采用基于字节查找表的标识符流式处理和重叠主机到设备/计算流水线，实现词汇无关的高性能GPU优先分词。
- 实验或效果：编码吞吐量比优化基线高84-95倍，端到端流式处理达1.27-1.84e8 tokens/s，有效消除分词瓶颈。

## 摘要（原文）

> Tokenization sits at the boundary between high-throughput genomic input and GPU compute, posing challenges in both algorithm design and system throughput. Overlapping k-mer tokenization can introduce information leakage under masked language modeling (MLM) and may degrade downstream accuracy. Single-nucleotide tokenization avoids leakage and preserves per-base fidelity, but it greatly increases sequence length for attention-based architectures. Non-overlapping k-mers and byte-pair encoding (BPE) provide compression and avoid leakage, at the cost of boundary sensitivity or reduced interpretability. Empirically, the choice of tokenization interacts strongly with model architecture and task requirements. At the system level, however, standard string tokenizers and host-bound vocabulary lookups dominate wall-clock time once inputs reach billions of bases, regardless of the tokenization algorithm. We present DNATok, a high-performance, GPU-first tokenization system that replaces general-purpose string processing with byte lookup table (LUT)-based identifier streaming and an overlapped host-to-device (H2D)/compute pipeline using pinned memory and architectural parallelism. DNATok is vocabulary-agnostic: it accelerates single-nucleotide, non-overlapping k-mer, and BPE tokenization, and integrates as a drop-in systems layer beneath genomic foundation models. DNATok achieves 84-95x higher encoding throughput than optimized Hugging Face baselines and up to 1.9x higher H2D throughput. End-to-end streaming reaches 1.27-1.84e8 tokens/s depending on configuration, effectively removing tokenization as a bottleneck for production-scale training and inference.

