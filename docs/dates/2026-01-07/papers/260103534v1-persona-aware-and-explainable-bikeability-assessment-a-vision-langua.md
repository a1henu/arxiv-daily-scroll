---
layout: default
title: Persona-aware and Explainable Bikeability Assessment: A Vision-Language Model Approach
---

# Persona-aware and Explainable Bikeability Assessment: A Vision-Language Model Approach
**arXiv**：[2601.03534v1](https://arxiv.org/abs/2601.03534) · [PDF](https://arxiv.org/pdf/2601.03534.pdf)  
**作者**：Yilong Dai, Ziyi Wang, Chenguang Wang, Kexin Zhou, Yiheng Qian, Susu Xu, Xiang Yan  

**一句话要点**：提出基于角色感知的视觉语言模型框架，以解决自行车友好性评估中环境复杂性和用户感知异质性问题。

**关键词**：自行车友好性评估, 视觉语言模型, 角色感知, 可解释人工智能, 多粒度监督微调, 数据增强

## 3 点简述
- 核心问题：现有基于感知的自行车友好性评估方法难以捕捉道路环境复杂性和用户主观感知异质性。
- 方法要点：结合理论驱动的角色条件化、多粒度监督微调和AI数据增强，实现可解释的评估。
- 实验或效果：通过众包系统收集数据，实验显示框架在预测评分和可解释因子归因方面表现优异。

## 摘要（原文）

> Bikeability assessment is essential for advancing sustainable urban transportation and creating cyclist-friendly cities, and it requires incorporating users' perceptions of safety and comfort. Yet existing perception-based bikeability assessment approaches face key limitations in capturing the complexity of road environments and adequately accounting for heterogeneity in subjective user perceptions. This paper proposes a persona-aware Vision-Language Model framework for bikeability assessment with three novel contributions: (i) theory-grounded persona conditioning based on established cyclist typology that generates persona-specific explanations via chain-of-thought reasoning; (ii) multi-granularity supervised fine-tuning that combines scarce expert-annotated reasoning with abundant user ratings for joint prediction and explainable assessment; and (iii) AI-enabled data augmentation that creates controlled paired data to isolate infrastructure variable impacts. To test and validate this framework, we developed a panoramic image-based crowdsourcing system and collected 12,400 persona-conditioned assessments from 427 cyclists. Experiment results show that the proposed framework offers competitive bikeability rating prediction while uniquely enabling explainable factor attribution.

