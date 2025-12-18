---
layout: default
title: HD-Prot: A Protein Language Model for Joint Sequence-Structure Modeling with Continuous Structure Tokens
---

# HD-Prot: A Protein Language Model for Joint Sequence-Structure Modeling with Continuous Structure Tokens
**arXiv**：[2512.15133v1](https://arxiv.org/abs/2512.15133) · [PDF](https://arxiv.org/pdf/2512.15133.pdf)  
**作者**：Yi Zhou, Haohao Qu, Yunqing Liu, Shanru Lin, Le Song, Wenqi Fan  

**一句话要点**：提出HD-Prot蛋白质语言模型，通过连续结构标记实现序列-结构联合建模

**关键词**：蛋白质语言模型, 序列-结构联合建模, 连续结构标记, 混合扩散模型, 多模态学习

## 3 点简述
- 核心问题：现有方法离散化蛋白质结构导致细粒度信息丢失，限制多模态pLMs性能
- 方法要点：在离散pLM上添加连续扩散头，使用统一吸收扩散过程捕获跨模态依赖
- 实验或效果：在无条件共生成、motif-scaffolding、结构预测和逆折叠任务中表现竞争性

## 摘要（原文）

> Proteins inherently possess a consistent sequence-structure duality. The abundance of protein sequence data, which can be readily represented as discrete tokens, has driven fruitful developments in protein language models (pLMs). A key remaining challenge, however, is how to effectively integrate continuous structural knowledge into pLMs. Current methods often discretize protein structures to accommodate the language modeling framework, which inevitably results in the loss of fine-grained information and limits the performance potential of multimodal pLMs. In this paper, we argue that such concerns can be circumvented: a sequence-based pLM can be extended to incorporate the structure modality through continuous tokens, i.e., high-fidelity protein structure latents that avoid vector quantization. Specifically, we propose a hybrid diffusion protein language model, HD-Prot, which embeds a continuous-valued diffusion head atop a discrete pLM, enabling seamless operation with both discrete and continuous tokens for joint sequence-structure modeling. It captures inter-token dependencies across modalities through a unified absorbing diffusion process, and estimates per-token distributions via categorical prediction for sequences and continuous diffusion for structures. Extensive empirical results show that HD-Prot achieves competitive performance in unconditional sequence-structure co-generation, motif-scaffolding, protein structure prediction, and inverse folding tasks, performing on par with state-of-the-art multimodal pLMs despite being developed under limited computational resources. It highlights the viability of simultaneously estimating categorical and continuous distributions within a unified language model architecture, offering a promising alternative direction for multimodal pLMs.

