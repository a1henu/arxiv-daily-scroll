---
layout: default
title: Can Local Vision-Language Models improve Activity Recognition over Vision Transformers? -- Case Study on Newborn Resuscitation
---

# Can Local Vision-Language Models improve Activity Recognition over Vision Transformers? -- Case Study on Newborn Resuscitation
**arXiv**：[2602.12002v1](https://arxiv.org/abs/2602.12002) · [PDF](https://arxiv.org/pdf/2602.12002.pdf)  
**作者**：Enrico Guerriero, Kjersti Engan, Øyvind Meinich-Bache  

**一句话要点**：提出基于本地视觉语言模型与LoRA微调的方法，以提升新生儿复苏视频中细粒度活动识别的准确性。

**关键词**：新生儿复苏视频, 细粒度活动识别, 视觉语言模型, LoRA微调, 零样本学习

## 3 点简述
- 核心问题：新生儿复苏视频的细粒度活动识别存在挑战，现有方法如Vision Transformers效果有限。
- 方法要点：探索生成式AI，结合本地视觉语言模型与大型语言模型，并采用LoRA微调策略。
- 实验或效果：在模拟数据集上，微调后模型F1分数达0.91，超越TimeSformer的0.70。

## 摘要（原文）

> Accurate documentation of newborn resuscitation is essential for quality improvement and adherence to clinical guidelines, yet remains underutilized in practice. Previous work using 3D-CNNs and Vision Transformers (ViT) has shown promising results in detecting key activities from newborn resuscitation videos, but also highlighted the challenges in recognizing such fine-grained activities. This work investigates the potential of generative AI (GenAI) methods to improve activity recognition from such videos. Specifically, we explore the use of local vision-language models (VLMs), combined with large language models (LLMs), and compare them to a supervised TimeSFormer baseline. Using a simulated dataset comprising 13.26 hours of newborn resuscitation videos, we evaluate several zero-shot VLM-based strategies and fine-tuned VLMs with classification heads, including Low-Rank Adaptation (LoRA). Our results suggest that small (local) VLMs struggle with hallucinations, but when fine-tuned with LoRA, the results reach F1 score at 0.91, surpassing the TimeSformer results of 0.70.

