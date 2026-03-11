---
layout: default
title: A Guideline-Aware AI Agent for Zero-Shot Target Volume Auto-Delineation
---

# A Guideline-Aware AI Agent for Zero-Shot Target Volume Auto-Delineation
**arXiv**：[2603.09448v1](https://arxiv.org/abs/2603.09448) · [PDF](https://arxiv.org/pdf/2603.09448.pdf)  
**作者**：Yoon Jo Kim, Wonyoung Cho, Jongmin Lee, Han Joo Chae, Hyunki Park, Sang Hoon Seo, Noh Jae Myung, Kyungmi Yang, Dongryul Oh, Jin Sung Kim  

**一句话要点**：提出OncoAgent框架，通过零射方式将文本指南转换为三维靶区轮廓，解决放疗中临床指南更新需重训练模型的问题。

**关键词**：放疗靶区勾画, 零射学习, AI代理, 临床指南转换, 食管癌, 三维轮廓生成

## 3 点简述
- 核心问题：放疗中临床靶区勾画依赖专家标注数据，指南更新时需成本高昂的模型重训练。
- 方法要点：基于AI代理框架，无需训练即可将文本临床指南直接转换为三维靶区轮廓。
- 实验或效果：在食管癌案例中，零射Dice系数达0.842（CTV）和0.880（PTV），临床评估中医生更偏好其指南合规性和可接受性。

## 摘要（原文）

> Delineating the clinical target volume (CTV) in radiotherapy involves complex margins constrained by tumor location and anatomical barriers. While deep learning models automate this process, their rigid reliance on expert-annotated data requires costly retraining whenever clinical guidelines update. To overcome this limitation, we introduce OncoAgent, a novel guideline-aware AI agent framework that seamlessly converts textual clinical guidelines into three-dimensional target contours in a training-free manner. Evaluated on esophageal cancer cases, the agent achieves a zero-shot Dice similarity coefficient of 0.842 for the CTV and 0.880 for the planning target volume, demonstrating performance highly comparable to a fully supervised nnU-Net baseline. Notably, in a blinded clinical evaluation, physicians strongly preferred OncoAgent over the supervised baseline, rating it higher in guideline compliance, modification effort, and clinical acceptability. Furthermore, the framework generalizes zero-shot to alternative esophageal guidelines and other anatomical sites (e.g., prostate) without any retraining. Beyond mere volumetric overlap, our agent-based paradigm offers near-instantaneous adaptability to alternative guidelines, providing a scalable and transparent pathway toward interpretability in radiotherapy treatment planning.

