---
layout: default
title: LookAroundNet: Extending Temporal Context with Transformers for Clinically Viable EEG Seizure Detection
---

# LookAroundNet: Extending Temporal Context with Transformers for Clinically Viable EEG Seizure Detection
**arXiv**：[2601.06016v1](https://arxiv.org/abs/2601.06016) · [PDF](https://arxiv.org/pdf/2601.06016.pdf)  
**作者**：Þór Sverrisson, Steinn Guðmundsson  

**一句话要点**：提出LookAroundNet，利用扩展时间上下文Transformer实现临床可行EEG癫痫检测

**关键词**：癫痫检测, 脑电图分析, Transformer模型, 时间上下文建模, 临床部署

## 3 点简述
- 核心问题：EEG癫痫检测因患者、记录条件和临床环境差异大而困难
- 方法要点：基于Transformer，使用更宽时间窗口建模癫痫活动，模拟临床上下文分析
- 实验或效果：在多个数据集上评估，表现强、泛化好、计算成本适合临床部署

## 摘要（原文）

> Automated seizure detection from electroencephalography (EEG) remains difficult due to the large variability of seizure dynamics across patients, recording conditions, and clinical settings. We introduce LookAroundNet, a transformer-based seizure detector that uses a wider temporal window of EEG data to model seizure activity. The seizure detector incorporates EEG signals before and after the segment of interest, reflecting how clinicians use surrounding context when interpreting EEG recordings. We evaluate the proposed method on multiple EEG datasets spanning diverse clinical environments, patient populations, and recording modalities, including routine clinical EEG and long-term ambulatory recordings, in order to study performance across varying data distributions. The evaluation includes publicly available datasets as well as a large proprietary collection of home EEG recordings, providing complementary views of controlled clinical data and unconstrained home-monitoring conditions. Our results show that LookAroundNet achieves strong performance across datasets, generalizes well to previously unseen recording conditions, and operates with computational costs compatible with real-world clinical deployment. The results indicate that extended temporal context, increased training data diversity, and model ensembling are key factors for improving performance. This work contributes to moving automatic seizure detection models toward clinically viable solutions.

