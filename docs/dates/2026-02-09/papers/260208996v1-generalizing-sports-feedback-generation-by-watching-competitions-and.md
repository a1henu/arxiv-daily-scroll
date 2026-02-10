---
layout: default
title: Generalizing Sports Feedback Generation by Watching Competitions and Reading Books: A Rock Climbing Case Study
---

# Generalizing Sports Feedback Generation by Watching Competitions and Reading Books: A Rock Climbing Case Study
**arXiv**：[2602.08996v1](https://arxiv.org/abs/2602.08996) · [PDF](https://arxiv.org/pdf/2602.08996.pdf)  
**作者**：Arushi Rai, Adriana Kovashka  

**一句话要点**：提出利用竞赛视频和教练手册等辅助数据，以提升攀岩运动反馈生成的泛化性能。

**关键词**：运动反馈生成, 视频-LLMs, 泛化性能, 评估指标, 辅助数据, 攀岩案例

## 3 点简述
- 问题：视频-LLMs在运动反馈生成上泛化差，且传统评估指标不适用。
- 方法：结合目标域辅助数据（如竞赛视频和教练手册）与源域反馈数据。
- 效果：提出特异性与可操作性评估指标，提升反馈生成质量。

## 摘要（原文）

> While there is rapid progress in video-LLMs with advanced reasoning capabilities, prior work shows that these models struggle on the challenging task of sports feedback generation and require expensive and difficult-to-collect finetuning feedback data for each sport. This limitation is evident from the poor generalization to sports unseen during finetuning. Furthermore, traditional text generation evaluation metrics (e.g., BLEU-4, METEOR, ROUGE-L, BERTScore), originally developed for machine translation and summarization, fail to capture the unique aspects of sports feedback quality. To address the first problem, using rock climbing as our case study, we propose using auxiliary freely-available web data from the target domain, such as competition videos and coaching manuals, in addition to existing sports feedback from a disjoint, source domain to improve sports feedback generation performance on the target domain. To improve evaluation, we propose two evaluation metrics: (1) specificity and (2) actionability. Together, our approach enables more meaningful and practical generation of sports feedback under limited annotations.

