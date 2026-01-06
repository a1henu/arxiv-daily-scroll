---
layout: default
title: Heterogeneous Low-Bandwidth Pre-Training of LLMs
---

# Heterogeneous Low-Bandwidth Pre-Training of LLMs
**arXiv**：[2601.02360v1](https://arxiv.org/abs/2601.02360) · [PDF](https://arxiv.org/pdf/2601.02360.pdf)  
**作者**：Yazan Obeidi, Amir Sarfi, Joel Lidin, Paul Janson, Eugene Belilovsky  

**一句话要点**：提出异构低带宽预训练框架，结合稀疏同步与压缩技术以解决LLM分布式训练中的带宽限制问题。

**关键词**：大语言模型预训练, 分布式训练, 带宽优化, 模型并行, 激活压缩, 异构计算

## 3 点简述
- 核心问题：LLM预训练中带宽限制阻碍分布式扩展，尤其在模型并行导致频繁大通信时。
- 方法要点：结合SparseLoCo稀疏同步与低带宽管道模型并行，通过激活压缩和异构分组优化通信。
- 实验或效果：在178M-1B参数实验中，异构压缩在激进压缩比下提升损失-通信权衡，表明实用路径。

## 摘要（原文）

> Pre-training large language models (LLMs) increasingly requires distributed compute, yet bandwidth constraints make it difficult to scale beyond well-provisioned datacenters-especially when model parallelism forces frequent, large inter-device communications. We study whether SparseLoCo, a low-communication data parallel method based on infrequent synchronization and sparse pseudo-gradient exchange, can be combined with low-bandwidth pipeline model parallelism via activation and activation-gradient compression. We introduce a heterogeneous distributed training framework where some participants host full replicas on high-bandwidth interconnects, while resource-limited participants are grouped to jointly instantiate a replica using pipeline parallelism with subspace-projected inter-stage communication. To make the recently introduced subspace pipeline compression compatible with SparseLoCo, we study a number of adaptations. Across large-scale language modeling experiments (178M-1B parameters) on standard pretraining corpora, we find that activation compression composes with SparseLoCo at modest cost, while selective (heterogeneous) compression consistently improves the loss-communication tradeoff relative to compressing all replicas-especially at aggressive compression ratios. These results suggest a practical path to incorporating low-bandwidth model parallelism and heterogeneous participants into LLM pre-training.

