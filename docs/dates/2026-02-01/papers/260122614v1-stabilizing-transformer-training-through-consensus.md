---
layout: default
title: Stabilizing Transformer Training Through Consensus
---

# Stabilizing Transformer Training Through Consensus
**arXiv**：[2601.22614v1](https://arxiv.org/abs/2601.22614) · [PDF](https://arxiv.org/pdf/2601.22614.pdf)  
**作者**：Shyam Venkatasubramanian, Sean Moushegian, Michael Lin, Mir Park, Ankit Singhal, Connor Lee  

**一句话要点**：提出共识机制作为注意力替代，以稳定Transformer在高学习率下的训练。

**关键词**：Transformer训练稳定性, 共识机制, 注意力替代, 学习率优化, 多模态实验, 图模型

## 3 点简述
- 标准Transformer在高学习率下训练不稳定，现有方法多关注优化过程而非架构创新。
- 共识机制作为注意力替代，通过图模型实现，提升训练稳定性并扩展有效学习率范围。
- 实验在文本、DNA和蛋白质模态上验证稳定性改进，并提出混合框架以保持性能。

## 摘要（原文）

> Standard attention-based transformers are known to exhibit instability under learning rate overspecification during training, particularly at high learning rates. While various methods have been proposed to improve resilience to such overspecification by modifying the optimization procedure, fundamental architectural innovations to this end remain underexplored. In this work, we illustrate that the consensus mechanism, a drop-in replacement for attention, stabilizes transformer training across a wider effective range of learning rates. We formulate consensus as a graphical model and provide extensive empirical analysis demonstrating improved stability across learning rate sweeps on text, DNA, and protein modalities. We further propose a hybrid consensus-attention framework that preserves performance while improving stability. We provide theoretical analysis characterizing the properties of consensus.

