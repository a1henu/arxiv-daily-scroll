---
layout: default
title: Efficient Self-Evaluation for Diffusion Language Models via Sequence Regeneration
---

# Efficient Self-Evaluation for Diffusion Language Models via Sequence Regeneration
**arXiv**：[2603.02760v1](https://arxiv.org/abs/2603.02760) · [PDF](https://arxiv.org/pdf/2603.02760.pdf)  
**作者**：Linhao Zhong, Linyu Wu, Wen Wang, Yuling Xi, Chenchen Jing, Jiaheng Zhang, Hao Chen, Chunhua Shen  

**一句话要点**：提出DiSE方法以解决扩散语言模型的自评估难题，通过序列再生概率量化置信度。

**关键词**：扩散语言模型, 自评估, 序列再生, 置信度量化, 灵活长度生成

## 3 点简述
- 扩散语言模型因非顺序生成导致质量评估困难，需有效自评估方法。
- DiSE基于全上下文计算序列再生概率，量化置信度，支持似然估计和不确定性量化。
- 实验验证DiSE与语义连贯性和答案准确性正相关，并在灵活长度生成中有效应用。

## 摘要（原文）

> Diffusion large language models (dLLMs) have recently attracted significant attention for their ability to enhance diversity, controllability, and parallelism. However, their non-sequential, bidirectionally masked generation makes quality assessment difficult, underscoring the need for effective self-evaluation. In this work, we propose DiSE, a simple yet effective self-evaluation confidence quantification method for dLLMs. DiSE quantifies confidence by computing the probability of regenerating the tokens in the entire generated sequence, given the full context. This method enables more efficient and reliable quality assessment by leveraging token regeneration probabilities, facilitating both likelihood estimation and robust uncertainty quantification. Building upon DiSE, we further introduce a flexible-length generation framework, which adaptively controls the sequence length based on the model's self-assessment of its own output. We analyze and validate the feasibility of DiSE from the perspective of dLLM generalization, and empirically demonstrate that DiSE is positively correlated with both semantic coherence and answer accuracy. Extensive experiments on likelihood evaluation, uncertainty quantification, and flexible-length generation further confirm the effectiveness of the proposed DiSE.

