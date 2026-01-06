---
layout: default
title: Output Embedding Centering for Stable LLM Pretraining
---

# Output Embedding Centering for Stable LLM Pretraining
**arXiv**：[2601.02031v1](https://arxiv.org/abs/2601.02031) · [PDF](https://arxiv.org/pdf/2601.02031.pdf)  
**作者**：Felix Stollenwerk, Anna Lokrantz, Niclas Hertzberg  

**一句话要点**：提出输出嵌入中心化以稳定大语言模型预训练

**关键词**：大语言模型预训练, 训练稳定性, 输出嵌入中心化, μ-损失, 学习率敏感度

## 3 点简述
- 核心问题：大学习率下输出对数发散导致训练不稳定
- 方法要点：基于输出嵌入几何分析，提出μ-中心化或μ-损失作为缓解策略
- 实验或效果：优于z-损失，提升训练稳定性和学习率容忍度

## 摘要（原文）

> Pretraining of large language models is not only expensive but also prone to certain training instabilities. A specific instability that often occurs for large learning rates at the end of training is output logit divergence. The most widely used mitigation strategy, z-loss, merely addresses the symptoms rather than the underlying cause of the problem. In this paper, we analyze the instability from the perspective of the output embeddings' geometry and identify its cause. Based on this, we propose output embedding centering (OEC) as a new mitigation strategy, and prove that it suppresses output logit divergence. OEC can be implemented in two different ways, as a deterministic operation called μ-centering, or a regularization method called μ-loss. Our experiments show that both variants outperform z-loss in terms of training stability and learning rate sensitivity. In particular, they ensure that training converges even for large learning rates when z-loss fails. Furthermore, we find that μ-loss is significantly less sensitive to regularization hyperparameter tuning than z-loss.

