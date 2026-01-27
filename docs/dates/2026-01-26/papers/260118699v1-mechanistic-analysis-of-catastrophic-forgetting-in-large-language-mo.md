---
layout: default
title: Mechanistic Analysis of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning
---

# Mechanistic Analysis of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning
**arXiv**：[2601.18699v1](https://arxiv.org/abs/2601.18699) · [PDF](https://arxiv.org/pdf/2601.18699.pdf)  
**作者**：Olaf Yunus Laitinen Imanov  

**一句话要点**：分析大语言模型在持续微调中灾难性遗忘的机制，揭示梯度干扰、表示漂移和损失景观平坦化三大驱动因素。

**关键词**：灾难性遗忘, 持续学习, 大语言模型, Transformer, 梯度干扰, 表示漂移

## 3 点简述
- 核心问题：大语言模型在顺序任务持续微调中发生灾难性遗忘，新知识干扰旧能力，机制理解有限。
- 方法要点：对基于Transformer的LLMs进行系统性实验，识别梯度干扰、表示漂移和损失景观平坦化三大机制。
- 实验或效果：遗忘严重度与任务相似度强相关（Pearson r=0.87），约15-23%注意力头严重受损，低层更易受影响。

## 摘要（原文）

> Large language models exhibit remarkable performance across diverse tasks through pre-training and fine-tuning paradigms. However, continual fine-tuning on sequential tasks induces catastrophic forgetting, where newly acquired knowledge interferes with previously learned capabilities. Despite widespread observations of this phenomenon, the mechanistic understanding remains limited. Here, we present a comprehensive mechanistic analysis of catastrophic forgetting in transformer-based LLMs during sequential fine-tuning. Through systematic experiments across multiple model scales (109B to 400B total parameters) and task sequences, we identify three primary mechanisms driving forgetting: gradient interference in attention weights, representational drift in intermediate layers, and loss landscape flattening. We demonstrate that forgetting severity correlates strongly with task similarity (Pearson r = 0.87) and gradient alignment metrics. Our analysis reveals that approximately 15 to 23 percent of attention heads undergo severe disruption during fine-tuning, with lower layers showing greater susceptibility. These findings establish mechanistic foundations for developing targeted mitigation strategies in continual learning systems.

