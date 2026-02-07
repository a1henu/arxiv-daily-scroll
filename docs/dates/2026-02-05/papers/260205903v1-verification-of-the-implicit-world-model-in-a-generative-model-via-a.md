---
layout: default
title: Verification of the Implicit World Model in a Generative Model via Adversarial Sequences
---

# Verification of the Implicit World Model in a Generative Model via Adversarial Sequences
**arXiv**：[2602.05903v1](https://arxiv.org/abs/2602.05903) · [PDF](https://arxiv.org/pdf/2602.05903.pdf)  
**作者**：András Balogh, Márk Jelasity  

**一句话要点**：提出对抗序列生成方法，以验证生成序列模型在象棋领域的正确性。

**关键词**：生成序列模型, 世界模型验证, 对抗序列生成, 象棋规则, 模型正确性, 训练技术分析

## 3 点简述
- 核心问题：基于样本训练的生成序列模型能否捕获语言或规则的真实结构（世界模型），实现正确性（仅生成有效序列）。
- 方法要点：通过对抗性生成有效序列，迫使模型预测无效下一步，以验证模型正确性并分析失败模式。
- 实验或效果：在多种象棋模型上评估，发现所有模型均非完全正确，但某些训练技术和数据集选择能显著提升正确性。

## 摘要（原文）

> Generative sequence models are typically trained on sample sequences from natural or formal languages. It is a crucial question whether -- or to what extent -- sample-based training is able to capture the true structure of these languages, often referred to as the ``world model''. Theoretical results indicate that we can hope for soundness at best, that is, generating valid sequences, but not necessarily all of them. However, it is still important to have practical tools that are able to verify whether a given sequence model is sound. In this study, we focus on chess, as it is a domain that provides enough complexity while having a simple rule-based world model. We propose adversarial sequence generation for verifying the soundness of the sequence model. Our adversaries generate valid sequences so as to force the sequence model to generate an invalid next move prediction. Apart from the falsification of soundness, this method is also suitable for a more fine-grained analysis of the failure modes and the effects of different choices during training. To demonstrate this, we propose a number of methods for adversarial sequence generation and evaluate the approach on a large set of chess models. We train models on random as well as high-quality chess games, using several training recipes. We find that none of the models are sound, but some training techniques and dataset choices are able to improve soundness remarkably. We also investigate the potential application of board state probes in both our training and attack methods. Our findings indicate that the extracted board states have no causal role in next token prediction in most of the models.

