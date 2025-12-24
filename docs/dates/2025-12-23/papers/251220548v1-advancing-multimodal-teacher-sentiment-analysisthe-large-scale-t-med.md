---
layout: default
title: Advancing Multimodal Teacher Sentiment Analysis:The Large-Scale T-MED Dataset & The Effective AAM-TSA Model
---

# Advancing Multimodal Teacher Sentiment Analysis:The Large-Scale T-MED Dataset & The Effective AAM-TSA Model
**arXiv**：[2512.20548v1](https://arxiv.org/abs/2512.20548) · [PDF](https://arxiv.org/pdf/2512.20548.pdf)  
**作者**：Zhiyi Duan, Xiangren Wang, Hongyu Yuan, Qianli Xing  

**一句话要点**：提出AAM-TSA模型与T-MED数据集以解决教师情感分析中表演性及教学信息影响的问题

**关键词**：教师情感分析, 多模态数据集, 非对称注意力, 特征融合, 教育场景

## 3 点简述
- 核心问题：现有研究难以准确捕捉教师情感，因表演性及忽略教学信息影响。
- 方法要点：构建大规模多模态数据集T-MED，并提出基于非对称注意力的AAM-TSA模型进行特征融合。
- 实验或效果：AAM-TSA在T-MED数据集上显著优于现有方法，提升准确性和可解释性。

## 摘要（原文）

> Teachers' emotional states are critical in educational scenarios, profoundly impacting teaching efficacy, student engagement, and learning achievements. However, existing studies often fail to accurately capture teachers' emotions due to the performative nature and overlook the critical impact of instructional information on emotional expression.In this paper, we systematically investigate teacher sentiment analysis by building both the dataset and the model accordingly. We construct the first large-scale teacher multimodal sentiment analysis dataset, T-MED.To ensure labeling accuracy and efficiency, we employ a human-machine collaborative labeling process.The T-MED dataset includes 14,938 instances of teacher emotional data from 250 real classrooms across 11 subjects ranging from K-12 to higher education, integrating multimodal text, audio, video, and instructional information.Furthermore, we propose a novel asymmetric attention-based multimodal teacher sentiment analysis model, AAM-TSA.AAM-TSA introduces an asymmetric attention mechanism and hierarchical gating unit to enable differentiated cross-modal feature fusion and precise emotional classification. Experimental results demonstrate that AAM-TSA significantly outperforms existing state-of-the-art methods in terms of accuracy and interpretability on the T-MED dataset.

