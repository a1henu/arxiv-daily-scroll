---
layout: default
title: End-to-End Test-Time Training for Long Context
---

# End-to-End Test-Time Training for Long Context
**arXiv**：[2512.23675v1](https://arxiv.org/abs/2512.23675) · [PDF](https://arxiv.org/pdf/2512.23675.pdf)  
**作者**：Arnuv Tandon, Karan Dalal, Xinhao Li, Daniel Koceja, Marcel Rød, Sam Buchanan, Xiaolong Wang, Jure Leskovec, Sanmi Koyejo, Tatsunori Hashimoto, Carlos Guestrin, Jed McCaleb, Yejin Choi, Yu Sun  

**一句话要点**：提出端到端测试时训练方法，将长上下文建模视为持续学习问题，提升模型扩展性与推理效率。

**关键词**：长上下文建模, 测试时训练, 持续学习, 元学习, Transformer架构, 推理效率

## 3 点简述
- 核心问题：将长上下文语言建模重新定义为持续学习问题，而非依赖架构设计。
- 方法要点：使用标准Transformer架构，通过测试时基于上下文的下一词预测进行持续学习，并结合训练时元学习优化初始化。
- 实验或效果：在3B模型上，方法随上下文长度扩展性类似全注意力Transformer，推理延迟恒定，比全注意力快2.7倍于128K上下文。

## 摘要（原文）

> We formulate long-context language modeling as a problem in continual learning rather than architecture design. Under this formulation, we only use a standard architecture -- a Transformer with sliding-window attention. However, our model continues learning at test time via next-token prediction on the given context, compressing the context it reads into its weights. In addition, we improve the model's initialization for learning at test time via meta-learning at training time. Overall, our method, a form of Test-Time Training (TTT), is End-to-End (E2E) both at test time (via next-token prediction) and training time (via meta-learning), in contrast to previous forms. We conduct extensive experiments with a focus on scaling properties. In particular, for 3B models trained with 164B tokens, our method (TTT-E2E) scales with context length in the same way as Transformer with full attention, while others, such as Mamba 2 and Gated DeltaNet, do not. However, similar to RNNs, TTT-E2E has constant inference latency regardless of context length, making it 2.7 times faster than full attention for 128K context. Our code is publicly available.

