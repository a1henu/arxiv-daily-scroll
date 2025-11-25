---
layout: default
title: CataractCompDetect: Intraoperative Complication Detection in Cataract Surgery
---

# CataractCompDetect: Intraoperative Complication Detection in Cataract Surgery
**arXiv**：[2511.18968v1](https://arxiv.org/abs/2511.18968) · [PDF](https://arxiv.org/pdf/2511.18968.pdf)  
**作者**：Bhuvan Sachdeva, Sneha Kumari, Rudransh Agarwal, Shalaka Kumaraswamy, Niharika Singri Prasad, Simon Mueller, Raphael Lechtenboehmer, Maximilian W. M. Wintergerst, Thomas Schultz, Kaushik Murali, Mohit Jain  

**一句话要点**：提出CataractCompDetect框架以检测白内障手术中的术中并发症

**关键词**：白内障手术, 并发症检测, 视觉语言推理, 手术视频分析, 风险评分

## 3 点简述
- 核心问题：白内障手术中虹膜脱垂、后囊破裂和玻璃体丢失等并发症导致不良后果
- 方法要点：结合阶段感知定位、SAM 2跟踪、风险评分和视觉语言推理进行分类
- 实验或效果：在CataComp数据集上平均F1得分70.63%，各并发症检测性能达60.87%-81.8%

## 摘要（原文）

> Cataract surgery is one of the most commonly performed surgeries worldwide, yet intraoperative complications such as iris prolapse, posterior capsule rupture (PCR), and vitreous loss remain major causes of adverse outcomes. Automated detection of such events could enable early warning systems and objective training feedback. In this work, we propose CataractCompDetect, a complication detection framework that combines phase-aware localization, SAM 2-based tracking, complication-specific risk scoring, and vision-language reasoning for final classification. To validate CataractCompDetect, we curate CataComp, the first cataract surgery video dataset annotated for intraoperative complications, comprising 53 surgeries, including 23 with clinical complications. On CataComp, CataractCompDetect achieves an average F1 score of 70.63%, with per-complication performance of 81.8% (Iris Prolapse), 60.87% (PCR), and 69.23% (Vitreous Loss). These results highlight the value of combining structured surgical priors with vision-language reasoning for recognizing rare but high-impact intraoperative events. Our dataset and code will be publicly released upon acceptance.

