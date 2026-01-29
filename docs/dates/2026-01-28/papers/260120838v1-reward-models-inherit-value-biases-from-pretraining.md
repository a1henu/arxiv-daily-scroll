---
layout: default
title: Reward Models Inherit Value Biases from Pretraining
---

# Reward Models Inherit Value Biases from Pretraining
**arXiv**：[2601.20838v1](https://arxiv.org/abs/2601.20838) · [PDF](https://arxiv.org/pdf/2601.20838.pdf)  
**作者**：Brian Christian, Jessica A. F. Thompson, Elle Michelle Yang, Vincent Adam, Hannah Rose Kirk, Christopher Summerfield, Tsvetomira Dumbalska  

**一句话要点**：揭示奖励模型从预训练继承价值偏见，强调预训练阶段对齐的重要性

**关键词**：奖励模型, 价值偏见, 预训练对齐, 大语言模型, 心理语言学分析

## 3 点简述
- 核心问题：奖励模型基于预训练大语言模型初始化，其价值偏见影响未知
- 方法要点：使用心理语言学语料库分析10个开源奖励模型，基于'大二'心理轴测量偏见
- 实验或效果：发现Llama模型偏好'能动性'，Gemma模型偏好'共融性'，偏见持久且可重复

## 摘要（原文）

> Reward models (RMs) are central to aligning large language models (LLMs) with human values but have received less attention than pre-trained and post-trained LLMs themselves. Because RMs are initialized from LLMs, they inherit representations that shape their behavior, but the nature and extent of this influence remain understudied. In a comprehensive study of 10 leading open-weight RMs using validated psycholinguistic corpora, we show that RMs exhibit significant differences along multiple dimensions of human value as a function of their base model. Using the "Big Two" psychological axes, we show a robust preference of Llama RMs for "agency" and a corresponding robust preference of Gemma RMs for "communion." This phenomenon holds even when the preference data and finetuning process are identical, and we trace it back to the logits of the respective instruction-tuned and pre-trained models. These log-probability differences themselves can be formulated as an implicit RM; we derive usable implicit reward scores and show that they exhibit the very same agency/communion difference. We run experiments training RMs with ablations for preference data source and quantity, which demonstrate that this effect is not only repeatable but surprisingly durable. Despite RMs being designed to represent human preferences, our evidence shows that their outputs are influenced by the pretrained LLMs on which they are based. This work underscores the importance of safety and alignment efforts at the pretraining stage, and makes clear that open-source developers' choice of base model is as much a consideration of values as of performance.

