---
layout: default
title: Left-right asymmetry in predicting brain activity from LLMs' representations emerges with their formal linguistic competence
---

# Left-right asymmetry in predicting brain activity from LLMs' representations emerges with their formal linguistic competence
**arXiv**：[2602.12811v1](https://arxiv.org/abs/2602.12811) · [PDF](https://arxiv.org/pdf/2602.12811.pdf)  
**作者**：Laurent Bonnasse-Gahot, Christophe Pallier  

**一句话要点**：揭示大语言模型预测脑活动左右不对称性与形式语言能力共现

**关键词**：大语言模型, 脑活动预测, 形式语言能力, 左右不对称性, fMRI数据分析

## 3 点简述
- 核心问题：大语言模型训练中预测脑活动左右不对称性源于何种能力？
- 方法要点：使用OLMo-2 7B和Pythia模型，结合fMRI数据，对比训练检查点与基准测试性能。
- 实验或效果：不对称性与形式语言能力（如语法判断）共现，与算术或世界知识任务无关。

## 摘要（原文）

> When humans and large language models (LLMs) process the same text, activations in the LLMs correlate with brain activity measured, e.g., with functional magnetic resonance imaging (fMRI). Moreover, it has been shown that, as the training of an LLM progresses, the performance in predicting brain activity from its internal activations improves more in the left hemisphere than in the right one. The aim of the present work is to understand which kind of competence acquired by the LLMs underlies the emergence of this left-right asymmetry. Using the OLMo-2 7B language model at various training checkpoints and fMRI data from English participants, we compare the evolution of the left-right asymmetry in brain scores alongside performance on several benchmarks. We observe that the asymmetry co-emerges with the formal linguistic abilities of the LLM. These abilities are demonstrated in two ways: by the model's capacity to assign a higher probability to an acceptable sentence than to a grammatically unacceptable one within a minimal contrasting pair, or its ability to produce well-formed text. On the opposite, the left-right asymmetry does not correlate with the performance on arithmetic or Dyck language tasks; nor with text-based tasks involving world knowledge and reasoning. We generalize these results to another family of LLMs (Pythia) and another language, namely French. Our observations indicate that the left-right asymmetry in brain predictivity matches the progress in formal linguistic competence (knowledge of linguistic patterns).

