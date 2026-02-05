---
layout: default
title: VILLAIN at AVerImaTeC: Verifying Image-Text Claims via Multi-Agent Collaboration
---

# VILLAIN at AVerImaTeC: Verifying Image-Text Claims via Multi-Agent Collaboration
**arXiv**：[2602.04587v1](https://arxiv.org/abs/2602.04587) · [PDF](https://arxiv.org/pdf/2602.04587.pdf)  
**作者**：Jaeyoon Jung, Yejun Yoon, Seunghyun Yoon, Kunwoo Park  

**一句话要点**：提出VILLAIN系统，通过多智能体协作验证图像-文本声明，在AVerImaTeC任务中表现优异。

**关键词**：多模态事实核查, 图像-文本验证, 多智能体系统, 视觉语言模型, 证据检索

## 3 点简述
- 核心问题：验证图像-文本声明的真实性，涉及多模态事实核查。
- 方法要点：采用基于提示的多智能体协作，分阶段处理视觉和文本证据。
- 实验或效果：在AVerImaTeC共享任务中，所有评估指标排名第一。

## 摘要（原文）

> This paper describes VILLAIN, a multimodal fact-checking system that verifies image-text claims through prompt-based multi-agent collaboration. For the AVerImaTeC shared task, VILLAIN employs vision-language model agents across multiple stages of fact-checking. Textual and visual evidence is retrieved from the knowledge store enriched through additional web collection. To identify key information and address inconsistencies among evidence items, modality-specific and cross-modal agents generate analysis reports. In the subsequent stage, question-answer pairs are produced based on these reports. Finally, the Verdict Prediction agent produces the verification outcome based on the image-text claim and the generated question-answer pairs. Our system ranked first on the leaderboard across all evaluation metrics. The source code is publicly available at https://github.com/ssu-humane/VILLAIN.

