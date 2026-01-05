---
layout: default
title: Memory Bank Compression for Continual Adaptation of Large Language Models
---

# Memory Bank Compression for Continual Adaptation of Large Language Models
**arXiv**：[2601.00756v1](https://arxiv.org/abs/2601.00756) · [PDF](https://arxiv.org/pdf/2601.00756.pdf)  
**作者**：Thomas Katraouras, Dimitrios Rafailidis  

**一句话要点**：提出MBC模型，通过代码本优化压缩记忆库，以解决大规模数据流中记忆库不断增长的问题。

**关键词**：持续学习, 记忆库压缩, 代码本优化, Key-Value LoRA, 在线适应学习

## 3 点简述
- 核心问题：记忆增强方法中记忆库随数据流持续增长，导致存储和计算负担增加。
- 方法要点：采用代码本优化策略压缩记忆库，结合在线重置机制防止代码本崩溃，并利用Key-Value LoRA高效利用压缩表示。
- 实验或效果：在基准问答数据集上，MBC将记忆库大小压缩至最强基线的0.3%，同时保持高保留准确率。

## 摘要（原文）

> Large Language Models (LLMs) have become a mainstay for many everyday applications. However, as data evolve their knowledge quickly becomes outdated. Continual learning aims to update LLMs with new information without erasing previously acquired knowledge. Although methods such as full fine-tuning can incorporate new data, they are computationally expensive and prone to catastrophic forgetting, where prior knowledge is overwritten. Memory-augmented approaches address this by equipping LLMs with a memory bank, that is an external memory module which stores information for future use. However, these methods face a critical limitation, in particular, the memory bank constantly grows in the real-world scenario when large-scale data streams arrive. In this paper, we propose MBC, a model that compresses the memory bank through a codebook optimization strategy during online adaptation learning. To ensure stable learning, we also introduce an online resetting mechanism that prevents codebook collapse. In addition, we employ Key-Value Low-Rank Adaptation in the attention layers of the LLM, enabling efficient utilization of the compressed memory representations. Experiments with benchmark question-answering datasets demonstrate that MBC reduces the memory bank size to 0.3% when compared against the most competitive baseline, while maintaining high retention accuracy during online adaptation learning. Our code is publicly available at https://github.com/Thomkat/MBC.

