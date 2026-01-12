---
layout: default
title: AGDC: Autoregressive Generation of Variable-Length Sequences with Joint Discrete and Continuous Spaces
---

# AGDC: Autoregressive Generation of Variable-Length Sequences with Joint Discrete and Continuous Spaces
**arXiv**：[2601.05680v1](https://arxiv.org/abs/2601.05680) · [PDF](https://arxiv.org/pdf/2601.05680.pdf)  
**作者**：Yeonsang Shin, Insoo Kim, Bongkeun Kim, Keonwoo Bae, Bohyung Han  

**一句话要点**：提出AGDC框架以解决高精度混合序列生成中的精度损失问题

**关键词**：自回归生成, 混合序列建模, 扩散模型, 高精度生成, 半导体布局

## 3 点简述
- 核心问题：Transformer自回归模型依赖离散化表示，在高精度连续值生成中易导致精度损失和功能失效
- 方法要点：结合分类预测和扩散建模，引入EOS对数调整机制和长度正则化损失
- 实验或效果：在半导体布局等数据集上优于基线，实现高保真混合向量生成

## 摘要（原文）

> Transformer-based autoregressive models excel in data generation but are inherently constrained by their reliance on discretized tokens, which limits their ability to represent continuous values with high precision. We analyze the scalability limitations of existing discretization-based approaches for generating hybrid discrete-continuous sequences, particularly in high-precision domains such as semiconductor circuit designs, where precision loss can lead to functional failure. To address the challenge, we propose AGDC, a novel unified framework that jointly models discrete and continuous values for variable-length sequences. AGDC employs a hybrid approach that combines categorical prediction for discrete values with diffusion-based modeling for continuous values, incorporating two key technical components: an end-of-sequence (EOS) logit adjustment mechanism that uses an MLP to dynamically adjust EOS token logits based on sequence context, and a length regularization term integrated into the loss function. Additionally, we present ContLayNet, a large-scale benchmark comprising 334K high-precision semiconductor layout samples with specialized evaluation metrics that capture functional correctness where precision errors significantly impact performance. Experiments on semiconductor layouts (ContLayNet), graphic layouts, and SVGs demonstrate AGDC's superior performance in generating high-fidelity hybrid vector representations compared to discretization-based and fixed-schema baselines, achieving scalable high-precision generation across diverse domains.

