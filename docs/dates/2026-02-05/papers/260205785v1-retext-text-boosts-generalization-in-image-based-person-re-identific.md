---
layout: default
title: ReText: Text Boosts Generalization in Image-Based Person Re-identification
---

# ReText: Text Boosts Generalization in Image-Based Person Re-identification
**arXiv**：[2602.05785v1](https://arxiv.org/abs/2602.05785) · [PDF](https://arxiv.org/pdf/2602.05785.pdf)  
**作者**：Timur Mamedov, Karina Kvanchiani, Anton Konushin, Vadim Konushin  

**一句话要点**：提出ReText方法，通过文本增强单摄像头数据以提升跨域行人重识别的泛化能力

**关键词**：行人重识别, 跨域泛化, 多模态学习, 文本增强, 图像重建, 图文匹配

## 3 点简述
- 核心问题：跨域行人重识别泛化难，单摄像头数据易收集但缺乏跨视角变化
- 方法要点：混合多摄像头与文本增强的单摄像头数据，联合优化重识别、图文匹配和文本引导图像重建任务
- 实验或效果：在跨域基准测试中显著优于现有方法，首次探索多模态混合数据学习

## 摘要（原文）

> Generalizable image-based person re-identification (Re-ID) aims to recognize individuals across cameras in unseen domains without retraining. While multiple existing approaches address the domain gap through complex architectures, recent findings indicate that better generalization can be achieved by stylistically diverse single-camera data. Although this data is easy to collect, it lacks complexity due to minimal cross-view variation. We propose ReText, a novel method trained on a mixture of multi-camera Re-ID data and single-camera data, where the latter is complemented by textual descriptions to enrich semantic cues. During training, ReText jointly optimizes three tasks: (1) Re-ID on multi-camera data, (2) image-text matching, and (3) image reconstruction guided by text on single-camera data. Experiments demonstrate that ReText achieves strong generalization and significantly outperforms state-of-the-art methods on cross-domain Re-ID benchmarks. To the best of our knowledge, this is the first work to explore multimodal joint learning on a mixture of multi-camera and single-camera data in image-based person Re-ID.

