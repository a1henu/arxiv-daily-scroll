---
layout: default
title: Automatic Essay Scoring and Feedback Generation in Basque Language Learning
---

# Automatic Essay Scoring and Feedback Generation in Basque Language Learning
**arXiv**：[2512.08713v1](https://arxiv.org/abs/2512.08713) · [PDF](https://arxiv.org/pdf/2512.08713.pdf)  
**作者**：Ekhi Azurmendi, Xabier Arregi, Oier Lopez de Lacalle  

**一句话要点**：提出首个巴斯克语自动作文评分与反馈生成数据集及模型，提升低资源语言教育NLP研究基础。

**关键词**：自动作文评分, 反馈生成, 巴斯克语处理, 低资源语言NLP, 模型微调, 教育技术

## 3 点简述
- 核心问题：巴斯克语等低资源语言缺乏公开的自动作文评分数据集与反馈生成基准。
- 方法要点：构建包含3200篇C1水平作文的数据集，并微调RoBERTa-EusCrawl和Latxa模型进行评分与解释生成。
- 实验或效果：微调Latxa模型在评分一致性和反馈质量上超越GPT-5等闭源系统，并建立新评估方法验证反馈有效性。

## 摘要（原文）

> This paper introduces the first publicly available dataset for Automatic Essay Scoring (AES) and feedback generation in Basque, targeting the CEFR C1 proficiency level. The dataset comprises 3,200 essays from HABE, each annotated by expert evaluators with criterion specific scores covering correctness, richness, coherence, cohesion, and task alignment enriched with detailed feedback and error examples. We fine-tune open-source models, including RoBERTa-EusCrawl and Latxa 8B/70B, for both scoring and explanation generation. Our experiments show that encoder models remain highly reliable for AES, while supervised fine-tuning (SFT) of Latxa significantly enhances performance, surpassing state-of-the-art (SoTA) closed-source systems such as GPT-5 and Claude Sonnet 4.5 in scoring consistency and feedback quality. We also propose a novel evaluation methodology for assessing feedback generation, combining automatic consistency metrics with expert-based validation of extracted learner errors. Results demonstrate that the fine-tuned Latxa model produces criterion-aligned, pedagogically meaningful feedback and identifies a wider range of error types than proprietary models. This resource and benchmark establish a foundation for transparent, reproducible, and educationally grounded NLP research in low-resource languages such as Basque.

