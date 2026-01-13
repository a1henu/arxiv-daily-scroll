---
layout: default
title: DT-ICU: Towards Explainable Digital Twins for ICU Patient Monitoring via Multi-Modal and Multi-Task Iterative Inference
---

# DT-ICU: Towards Explainable Digital Twins for ICU Patient Monitoring via Multi-Modal and Multi-Task Iterative Inference
**arXiv**：[2601.07778v1](https://arxiv.org/abs/2601.07778) · [PDF](https://arxiv.org/pdf/2601.07778.pdf)  
**作者**：Wen Guo  

**一句话要点**：提出DT-ICU多模态数字孪生框架，用于ICU患者连续风险监测，实现可解释预测。

**关键词**：数字孪生, 多模态学习, ICU监测, 可解释AI, 时间序列分析, 多任务学习

## 3 点简述
- 核心问题：ICU患者风险监测需整合多模态数据并随时间更新预测，现有方法可能缺乏解释性。
- 方法要点：结合可变长临床时间序列与静态信息，通过多任务迭代推理架构支持连续预测更新。
- 实验或效果：在MIMIC-IV数据集上优于基线，提供可解释性分析，展示模型对多模态信号的合理依赖。

## 摘要（原文）

> We introduce DT-ICU, a multimodal digital twin framework for continuous risk estimation in intensive care. DT-ICU integrates variable-length clinical time series with static patient information in a unified multitask architecture, enabling predictions to be updated as new observations accumulate over the ICU stay. We evaluate DT-ICU on the large, publicly available MIMIC-IV dataset, where it consistently outperforms established baseline models under different evaluation settings. Our test-length analysis shows that meaningful discrimination is achieved shortly after admission, while longer observation windows further improve the ranking of high-risk patients in highly imbalanced cohorts. To examine how the model leverages heterogeneous data sources, we perform systematic modality ablations, revealing that the model learnt a reasonable structured reliance on interventions, physiological response observations, and contextual information. These analyses provide interpretable insights into how multimodal signals are combined and how trade-offs between sensitivity and precision emerge. Together, these results demonstrate that DT-ICU delivers accurate, temporally robust, and interpretable predictions, supporting its potential as a practical digital twin framework for continuous patient monitoring in critical care. The source code and trained model weights for DT-ICU are publicly available at https://github.com/GUO-W/DT-ICU-release.

