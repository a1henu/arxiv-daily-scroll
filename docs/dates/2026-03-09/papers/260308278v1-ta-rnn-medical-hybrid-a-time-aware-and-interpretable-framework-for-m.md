---
layout: default
title: TA-RNN-Medical-Hybrid: A Time-Aware and Interpretable Framework for Mortality Risk Prediction
---

# TA-RNN-Medical-Hybrid: A Time-Aware and Interpretable Framework for Mortality Risk Prediction
**arXiv**：[2603.08278v1](https://arxiv.org/abs/2603.08278) · [PDF](https://arxiv.org/pdf/2603.08278.pdf)  
**作者**：Zahra Jafari, Azadeh Zamanifar, Amirfarhad Farhadi  

**一句话要点**：提出TA-RNN-Medical-Hybrid框架，通过时间感知和知识增强建模解决ICU死亡率预测的准确性与可解释性问题。

**关键词**：死亡率预测, 时间感知建模, 可解释性框架, 电子健康记录, 重症监护室, 深度学习

## 3 点简述
- 核心问题：ICU电子健康记录时间不规则、疾病轨迹复杂，现有模型缺乏临床可解释性。
- 方法要点：集成连续时间编码、标准化医学概念表示和分层双重注意力机制，实现时间感知和知识增强建模。
- 实验或效果：在MIMIC-III数据集上验证，AUC、准确率和F2分数提升，并提供疾病严重度和时间进展的可解释分析。

## 摘要（原文）

> Accurate and interpretable mortality risk prediction in intensive care units (ICUs) remains a critical challenge due to the irregular temporal structure of electronic health records (EHRs), the complexity of longitudinal disease trajectories, and the lack of clinically grounded explanations in many data-driven models. To address these challenges, we propose \textit{TA-RNN-Medical-Hybrid}, a time-aware and knowledge-enriched deep learning framework that jointly models longitudinal clinical sequences and irregular temporal dynamics through explicit continuous-time encoding, along with standardized medical concept representations. The proposed framework extends time-aware recurrent modeling by integrating explicit continuous-time embeddings that operate independently of visit indexing, SNOMED-based disease representations, and a hierarchical dual-level attention mechanism that captures both visit-level temporal importance and feature/concept-level clinical relevance. This design enables accurate mortality risk estimation while providing transparent and clinically meaningful explanations aligned with established medical knowledge. We evaluate the proposed approach on the MIMIC-III critical care dataset and compare it against strong time-aware and sequential baselines. Experimental results demonstrate that TA-RNN-Medical-Hybrid consistently improves predictive performance in terms of AUC, accuracy, and recall-oriented F$_2$-score. Moreover, qualitative analysis shows that the model effectively decomposes mortality risk across time and clinical concepts, yielding interpretable insights into disease severity, chronicity, and temporal progression. Overall, the proposed framework bridges the gap between predictive accuracy and clinical interpretability, offering a scalable and transparent solution for high-stakes ICU decision support systems.

