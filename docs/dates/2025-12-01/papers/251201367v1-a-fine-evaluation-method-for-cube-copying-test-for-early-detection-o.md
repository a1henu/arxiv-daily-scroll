---
layout: default
title: A Fine Evaluation Method for Cube Copying Test for Early Detection of Alzheimer's Disease
---

# A Fine Evaluation Method for Cube Copying Test for Early Detection of Alzheimer's Disease
**arXiv**：[2512.01367v1](https://arxiv.org/abs/2512.01367) · [PDF](https://arxiv.org/pdf/2512.01367.pdf)  
**作者**：Xinyu Jiang, Cuiyun Gao, Wenda Huang, Yiyang Jiang, Binwen Luo, Yuxin Jiang, Mengting Wang, Haoran Wen, Yang Zhao, Xuemei Chen, Songqun Huang  

**一句话要点**：提出基于动态笔迹特征提取的精细评估方法，以解决阿尔茨海默病早期检测中立方体复制测试的评估偏差问题。

**关键词**：阿尔茨海默病早期检测, 立方体复制测试, 动态笔迹特征提取, BiLSTM-Attention模型, 视觉空间认知评估, 认知障碍筛查

## 3 点简述
- 核心问题：传统蒙特利尔认知评估使用二元评分法评估立方体复制测试，导致低教育水平老年人评分偏差，影响阿尔茨海默病早期检测准确性。
- 方法要点：利用Cogni-CareV3.0软件收集动态笔迹数据，提取空间和运动特征，采用BiLSTM-Attention模型进行分类，实现精细评估。
- 实验或效果：方法分类准确率达86.69%，优于同类研究，评分分布与MCI患者、年龄、教育水平显著相关，为早期筛查提供客观依据。

## 摘要（原文）

> Background: Impairment of visual spatial cognitive function is the most common early clinical manifestation of Alzheimer's Disease (AD). When the Montreal Cognitive Assessment (MoCA) uses the "0/1" binary method ("pass/fail") to evaluate the visual spatial cognitive ability represented by the Cube Copying Test(CCT), the elder with less formal education generally score 0 point, resulting in serious bias in the evaluation results. Therefore, this study proposes a fine evaluation method for CCT based on dynamic handwriting feature extraction of DH-SCSM-BLA. method : The Cogni-CareV3.0 software independently developed by our team was used to collect dynamic handwriting data of CCT. Then, the spatial and motion features of segmented dynamic handwriting were extracted, and feature matrix with unequal dimensions were normalized. Finally, a bidirectional long short-term memory network model combined with attention mechanism (BiLSTM-Attention) was adopted for classification. Result: The experimental results showed that: The proposed method has significant superiority compared to similar studies, with a classification accuracy of 86.69%. The distribution of cube drawing ability scores has significant regularity for three aspects such as MCI patients and healthy control group, age, and levels of education. It was also found that score for each cognitive task including cube drawing ability score is negatively correlated with age. Score for each cognitive task including cube drawing ability score, but positively correlated with levels of education significantly. Conclusion: This study provides a relatively objective and comprehensive evaluation method for early screening and personalized intervention of visual spatial cognitive impairment.

