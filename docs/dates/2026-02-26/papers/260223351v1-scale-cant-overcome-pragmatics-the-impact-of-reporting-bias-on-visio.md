---
layout: default
title: Scale Can't Overcome Pragmatics: The Impact of Reporting Bias on Vision-Language Reasoning
---

# Scale Can't Overcome Pragmatics: The Impact of Reporting Bias on Vision-Language Reasoning
**arXiv**：[2602.23351v1](https://arxiv.org/abs/2602.23351) · [PDF](https://arxiv.org/pdf/2602.23351.pdf)  
**作者**：Amita Kamath, Jack Hessel, Khyathi Chandu, Jena D. Hwang, Kai-Wei Chang, Ranjay Krishna  

**一句话要点**：揭示报告偏差限制视觉语言模型推理能力，提出针对性数据标注提升效果

**关键词**：视觉语言模型, 报告偏差, 推理能力, 数据标注, 语用学, 模型评估

## 3 点简述
- 核心问题：视觉语言模型推理能力不足源于训练数据中的报告偏差，即默认省略隐含信息。
- 方法要点：基于语用学理论分析OpenCLIP等模型数据，发现空间、时间、否定和计数推理技能代表性不足。
- 实验或效果：实验表明，扩大数据规模无法自动提升推理能力，但针对性标注数据能有效改善性能。

## 摘要（原文）

> The lack of reasoning capabilities in Vision-Language Models (VLMs) has remained at the forefront of research discourse. We posit that this behavior stems from a reporting bias in their training data. That is, how people communicate about visual content by default omits tacit information needed to supervise some types of reasoning; e.g., "at the game today!" is a more likely caption than "a photo of 37 people standing behind a field". We investigate the data underlying the popular VLMs OpenCLIP, LLaVA-1.5 and Molmo through the lens of theories from pragmatics, and find that reporting bias results in insufficient representation of four reasoning skills (spatial, temporal, negation, and counting), despite the corpora being of web-scale, and/or synthetically generated. With a set of curated benchmarks, we demonstrate that: (i) VLMs perform poorly on the aforementioned types of reasoning suppressed in the training data by reporting bias; (ii) contrary to popular belief, scaling data size, model size, and to multiple languages does not result in emergence of these skills by default; but, promisingly, (iii) incorporating annotations specifically collected to obtain tacit information is effective. Our findings highlight the need for more intentional training data curation methods, rather than counting on scale for emergence of reasoning capabilities.

