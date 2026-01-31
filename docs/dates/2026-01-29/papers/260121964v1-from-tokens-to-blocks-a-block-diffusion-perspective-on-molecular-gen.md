---
layout: default
title: From Tokens to Blocks: A Block-Diffusion Perspective on Molecular Generation
---

# From Tokens to Blocks: A Block-Diffusion Perspective on Molecular Generation
**arXiv**：[2601.21964v1](https://arxiv.org/abs/2601.21964) · [PDF](https://arxiv.org/pdf/2601.21964.pdf)  
**作者**：Qianwei Yang, Dong Xu, Zhangfan Yang, Sisi Yuan, Zexuan Zhu, Jianqiang Li, Junkai Ji  

**一句话要点**：提出SoftMol框架，结合块扩散与自回归生成，用于靶向分子设计。

**关键词**：分子生成, 块扩散模型, 靶向药物设计, 软片段表示, 蒙特卡洛树搜索

## 3 点简述
- 现有分子语言模型难以捕捉图结构且缺乏靶向生成机制。
- 引入软片段表示和块扩散模型SoftBD，在结构约束下融合双向扩散与自回归生成。
- 实验显示SoftMol实现100%化学有效性，提升结合亲和力9.7%，并加速推理6.6倍。

## 摘要（原文）

> Drug discovery can be viewed as a combinatorial search over an immense chemical space, motivating the development of deep generative models for de novo molecular design. Among these, GPT-based molecular language models (MLM) have shown strong molecular design performance by learning chemical syntax and semantics from large-scale data. However, existing MLMs face two fundamental limitations: they inadequately capture the graph-structured nature of molecules when formulated as next-token prediction problems, and they typically lack explicit mechanisms for target-aware generation. Here, we propose SoftMol, a unified framework that co-designs molecular representation, model architecture, and search strategy for target-aware molecular generation. SoftMol introduces soft fragments, a rule-free block representation of SMILES that enables diffusion-native modeling, and develops SoftBD, the first block-diffusion molecular language model that combines local bidirectional diffusion with autoregressive generation under molecular structural constraints. To favor generated molecules with high drug-likeness and synthetic accessibility, SoftBD is trained on a carefully curated dataset named ZINC-Curated. SoftMol further integrates a gated Monte Carlo tree search to assemble fragments in a target-aware manner. Experimental results show that, compared with current state-of-the-art models, SoftMol achieves 100% chemical validity, improves binding affinity by 9.7%, yields a 2-3x increase in molecular diversity, and delivers a 6.6x speedup in inference efficiency. Code is available at https://github.com/szu-aicourse/softmol

