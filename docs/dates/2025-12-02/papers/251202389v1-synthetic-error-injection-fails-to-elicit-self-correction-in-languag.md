---
layout: default
title: Synthetic Error Injection Fails to Elicit Self-Correction In Language Models
---

# Synthetic Error Injection Fails to Elicit Self-Correction In Language Models
**arXiv**：[2512.02389v1](https://arxiv.org/abs/2512.02389) · [PDF](https://arxiv.org/pdf/2512.02389.pdf)  
**作者**：David X. Wu, Shreyas Kapur, Anant Sahai, Stuart Russell  

**一句话要点**：提出合成错误注入方法以诱导语言模型自我纠正，但实验表明其效果有限。

**关键词**：语言模型, 自我纠正, 合成错误注入, 监督学习, 分布偏移

## 3 点简述
- 核心问题：强化学习成本高，探索合成错误注入作为替代方法以激发语言模型自我纠正能力。
- 方法要点：在推理链中插入人工错误并掩码，通过监督学习训练模型识别和纠正这些错误。
- 实验或效果：方法在简单合成任务上未能显著提升性能，且模型常重复原始错误，合成错误与策略错误分布偏移导致能力下降。

## 摘要（原文）

> Reinforcement learning has become the dominant paradigm for eliciting reasoning and self-correction capabilities in large language models, but its computational expense motivates exploration of alternatives. Inspired by techniques from autonomous driving and robotics, we investigate whether supervised learning with synthetic error injection can induce self-correction abilities in language models. Our approach inserts artificial errors into reasoning chains, masks them, and supervises the model to recognize and correct these mistakes. Despite the intuitive appeal of this method, we find that it fails to significantly improve performance even on simple synthetic tasks across multiple models. Moreover, even when the model catches its own error, it often parrots the original mistake. We find that the distribution shift of synthetic errors to on-policy errors significantly degrades the error-correction capabilities of the fine-tuned model, even with good synthetic coverage of on-policy errors. Our results help explain why on-policy reinforcement learning methods have proven uniquely effective for eliciting self-correction.

