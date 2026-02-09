---
layout: default
title: Quantum Attention by Overlap Interference: Predicting Sequences from Classical and Many-Body Quantum Data
---

# Quantum Attention by Overlap Interference: Predicting Sequences from Classical and Many-Body Quantum Data
**arXiv**：[2602.06699v1](https://arxiv.org/abs/2602.06699) · [PDF](https://arxiv.org/pdf/2602.06699.pdf)  
**作者**：Alessio Pecilli, Matteo Rosati  

**一句话要点**：提出量子自注意力机制，通过重叠干涉实现序列预测，适用于经典和量子数据建模。

**关键词**：量子自注意力, 序列预测, 量子变换器, 重叠干涉, 量子机器学习

## 3 点简述
- 核心问题：实现量子自注意力以替代经典变换器中的非线性操作，提升序列预测效率。
- 方法要点：利用量子态重叠干涉产生非线性，直接输出Renyi-1/2交叉熵损失，避免解码步骤。
- 实验或效果：在经典数据和量子多体轨迹上验证序列预测能力，展示量子优势潜力。

## 摘要（原文）

> We propose a variational quantum implementation of self-attention (QSA), the core operation in transformers and large language models, which predicts future elements of a sequence by forming overlap-weighted combinations of past data. At variance with previous approaches, our QSA realizes the required nonlinearity through interference of state overlaps and returns a Renyi-1/2 cross-entropy loss directly as the expectation value of an observable, avoiding the need to decode amplitude-encoded predictions into classical logits. Furthermore, QSA naturally accommodates a constrained, trainable data-embedding that ties quantum state overlaps to data-level similarities. We find a gate complexity dominant scaling O(T d^2) for QSA, versus O(T^2 d) classically, suggesting an advantage in the practical regime where the sequence length T dominates the embedding size d. In simulations, we show that our QSA-based quantum transformer learns sequence prediction on classical data and on many-body transverse-field Ising quantum trajectories, establishing trainable attention as a practical primitive for quantum dynamical modeling.

