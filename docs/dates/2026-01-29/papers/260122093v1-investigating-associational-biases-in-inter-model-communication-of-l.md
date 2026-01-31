---
layout: default
title: Investigating Associational Biases in Inter-Model Communication of Large Generative Models
---

# Investigating Associational Biases in Inter-Model Communication of Large Generative Models
**arXiv**：[2601.22093v1](https://arxiv.org/abs/2601.22093) · [PDF](https://arxiv.org/pdf/2601.22093.pdf)  
**作者**：Fethiye Irmak Dogan, Yuval Weiss, Kajal Patel, Jiaee Cheong, Hatice Gunes  

**一句话要点**：研究生成模型间通信中的关联偏见传播与缓解策略

**关键词**：关联偏见, 模型间通信, 人口分布漂移, 可解释性分析, 人本AI系统, 缓解策略

## 3 点简述
- 核心问题：生成AI中的关联偏见在模型间通信中可能持续、传播并放大，影响人本感知任务。
- 方法要点：通过图像生成与描述交替的管道，量化人口分布漂移，并使用可解释性分析评估系统性偏差。
- 实验或效果：发现动作和情感表示向年轻化漂移，情感表示更女性化，部分预测依赖虚假视觉线索。

## 摘要（原文）

> Social bias in generative AI can manifest not only as performance disparities but also as associational bias, whereby models learn and reproduce stereotypical associations between concepts and demographic groups, even in the absence of explicit demographic information (e.g., associating doctors with men). These associations can persist, propagate, and potentially amplify across repeated exchanges in inter-model communication pipelines, where one generative model's output becomes another's input. This is especially salient for human-centred perception tasks, such as human activity recognition and affect prediction, where inferences about behaviour and internal states can lead to errors or stereotypical associations that propagate into unequal treatment. In this work, focusing on human activity and affective expression, we study how such associations evolve within an inter-model communication pipeline that alternates between image generation and image description. Using the RAF-DB and PHASE datasets, we quantify demographic distribution drift induced by model-to-model information exchange and assess whether these drifts are systematic using an explainability pipeline. Our results reveal demographic drifts toward younger representations for both actions and emotions, as well as toward more female-presenting representations, primarily for emotions. We further find evidence that some predictions are supported by spurious visual regions (e.g., background or hair) rather than concept-relevant cues (e.g., body or face). We also examine whether these demographic drifts translate into measurable differences in downstream behaviour, i.e., while predicting activity and emotion labels. Finally, we outline mitigation strategies spanning data-centric, training and deployment interventions, and emphasise the need for careful safeguards when deploying interconnected models in human-centred AI systems.

