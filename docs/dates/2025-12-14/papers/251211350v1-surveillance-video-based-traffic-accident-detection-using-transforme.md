---
layout: default
title: Surveillance Video-Based Traffic Accident Detection Using Transformer Architecture
---

# Surveillance Video-Based Traffic Accident Detection Using Transformer Architecture
**arXiv**：[2512.11350v1](https://arxiv.org/abs/2512.11350) · [PDF](https://arxiv.org/pdf/2512.11350.pdf)  
**作者**：Tanu Singh, Pranamesh Chakraborty, Long T. Truong  

**一句话要点**：提出基于Transformer的监控视频交通事故检测方法，结合运动线索提升准确性。

**关键词**：交通事故检测, Transformer架构, 监控视频分析, 运动线索融合, 时空依赖建模

## 3 点简述
- 核心问题：传统方法在时空理解和跨域泛化方面不足，且数据集小、多样性差。
- 方法要点：使用Transformer架构捕获时空依赖，并评估多种运动线索融合策略。
- 实验或效果：结合RGB与光流特征达到88.3%最高准确率，并与VLM模型对比验证。

## 摘要（原文）

> Road traffic accidents represent a leading cause of mortality globally, with incidence rates rising due to increasing population, urbanization, and motorization. Rising accident rates raise concerns about traffic surveillance effectiveness. Traditional computer vision methods for accident detection struggle with limited spatiotemporal understanding and poor cross-domain generalization. Recent advances in transformer architectures excel at modeling global spatial-temporal dependencies and parallel computation. However, applying these models to automated traffic accident detection is limited by small, non-diverse datasets, hindering the development of robust, generalizable systems. To address this gap, we curated a comprehensive and balanced dataset that captures a wide spectrum of traffic environments, accident types, and contextual variations. Utilizing the curated dataset, we propose an accident detection model based on a transformer architecture using pre-extracted spatial video features. The architecture employs convolutional layers to extract local correlations across diverse patterns within a frame, while leveraging transformers to capture sequential-temporal dependencies among the retrieved features. Moreover, most existing studies neglect the integration of motion cues, which are essential for understanding dynamic scenes, especially during accidents. These approaches typically rely on static features or coarse temporal information. In this study, multiple methods for incorporating motion cues were evaluated to identify the most effective strategy. Among the tested input approaches, concatenating RGB features with optical flow achieved the highest accuracy at 88.3%. The results were further compared with vision language models (VLM) such as GPT, Gemini, and LLaVA-NeXT-Video to assess the effectiveness of the proposed method.

