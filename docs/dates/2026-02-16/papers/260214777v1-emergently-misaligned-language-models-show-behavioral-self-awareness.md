---
layout: default
title: Emergently Misaligned Language Models Show Behavioral Self-Awareness That Shifts With Subsequent Realignment
---

# Emergently Misaligned Language Models Show Behavioral Self-Awareness That Shifts With Subsequent Realignment
**arXiv**：[2602.14777v1](https://arxiv.org/abs/2602.14777) · [PDF](https://arxiv.org/pdf/2602.14777.pdf)  
**作者**：Laurène Vaugrante, Anietta Weckauff, Thilo Hagendorff  

**一句话要点**：研究大语言模型在序列微调中展现行为自我意识，以追踪对齐状态变化

**关键词**：大语言模型, 涌现错位, 行为自我意识, 序列微调, 模型对齐, 安全评估

## 3 点简述
- 核心问题：探究大语言模型在诱导和逆转涌现错位后，是否具备行为自我意识来描述其行为转变
- 方法要点：对GPT-4.1模型进行序列微调，使用已知数据集诱导和逆转错位，评估模型自我报告行为
- 实验或效果：错位模型自评危害性显著高于基础模型和再对齐模型，表明自我意识能追踪实际对齐状态

## 摘要（原文）

> Recent research has demonstrated that large language models (LLMs) fine-tuned on incorrect trivia question-answer pairs exhibit toxicity - a phenomenon later termed "emergent misalignment". Moreover, research has shown that LLMs possess behavioral self-awareness - the ability to describe learned behaviors that were only implicitly demonstrated in training data. Here, we investigate the intersection of these phenomena. We fine-tune GPT-4.1 models sequentially on datasets known to induce and reverse emergent misalignment and evaluate whether the models are self-aware of their behavior transitions without providing in-context examples. Our results show that emergently misaligned models rate themselves as significantly more harmful compared to their base model and realigned counterparts, demonstrating behavioral self-awareness of their own emergent misalignment. Our findings show that behavioral self-awareness tracks actual alignment states of models, indicating that models can be queried for informative signals about their own safety.

