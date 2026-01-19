---
layout: default
title: Steering Language Models Before They Speak: Logit-Level Interventions
---

# Steering Language Models Before They Speak: Logit-Level Interventions
**arXiv**：[2601.10960v1](https://arxiv.org/abs/2601.10960) · [PDF](https://arxiv.org/pdf/2601.10960.pdf)  
**作者**：Hyeseon An, Shinwoo Park, Hyundong Jin, Yo-Sub Han  

**一句话要点**：提出基于统计的logit干预方法，以在推理时无训练地控制语言模型生成

**关键词**：语言模型引导, logit干预, 无训练控制, 推理时干预, 统计token分数

## 3 点简述
- 核心问题：现有基于提示或激活的引导方法在一致性和细粒度控制上存在不足
- 方法要点：利用标注语料的z归一化对数几率构建统计token分数表，调整解码分布
- 实验或效果：在写作复杂度、正式度和毒性三个数据集上验证，实现高达+47%p准确率和50倍F1提升

## 摘要（原文）

> Steering LLMs is essential for specialized applications such as style-sensitive text rewriting, user-adaptive communication, and toxicity mitigation. Current steering methods, such as prompting-based and activation-based approaches, are widely used to guide model behavior. However, activation-based techniques require deep access to internal layers, while prompting-based steering often fails to provide consistent or fine-grained control. In order to address these limitations, we propose a training-free inference-time logit intervention for controllable generation. Our approach utilizes a statistical token score table derived from z-normalized log-odds of labeled corpora to shift the decoding distribution. Empirical evaluations across three diverse datasets focusing on writing complexity, formality, and toxicity demonstrate that our method effectively steers output characteristics, confirming its broad applicability and task-agnostic nature. Our results show that statistically grounded logit steering can achieve large, consistent, and multi-task control gains: up to +47%p accuracy and 50x f1 improvement.

