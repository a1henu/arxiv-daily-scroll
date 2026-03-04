---
layout: default
title: Bias and Fairness in Self-Supervised Acoustic Representations for Cognitive Impairment Detection
---

# Bias and Fairness in Self-Supervised Acoustic Representations for Cognitive Impairment Detection
**arXiv**：[2603.02937v1](https://arxiv.org/abs/2603.02937) · [PDF](https://arxiv.org/pdf/2603.02937.pdf)  
**作者**：Kashaf Gulzar, Korbinian Riedhammer, Elmar Nöth, Andreas K. Maier, Paula Andrea Pérez-Toro  

**一句话要点**：分析自监督声学表征在认知障碍检测中的偏见与公平性，揭示性能差异并提出公平评估需求。

**关键词**：认知障碍检测, 自监督学习, 公平性分析, 声学表征, 语音处理, 临床应用

## 3 点简述
- 核心问题：语音检测认知障碍存在性能差异，影响公平性和泛化能力。
- 方法要点：比较传统声学特征与Wav2Vec 2.0嵌入，评估性别、年龄和抑郁状态子组。
- 实验或效果：Wav2Vec 2.0高层嵌入性能更优但存在显著差异，女性与年轻参与者分类风险更高。

## 摘要（原文）

> Speech-based detection of cognitive impairment (CI) offers a promising non-invasive approach for early diagnosis, yet performance disparities across demographic and clinical subgroups remain underexplored, raising concerns around fairness and generalizability. This study presents a systematic bias analysis of acoustic-based CI and depression classification using the DementiaBank Pitt Corpus. We compare traditional acoustic features (MFCCs, eGeMAPS) with contextualized speech embeddings from Wav2Vec 2.0 (W2V2), and evaluate classification performance across gender, age, and depression-status subgroups. For CI detection, higher-layer W2V2 embeddings outperform baseline features (UAR up to 80.6\%), but exhibit performance disparities; specifically, females and younger participants demonstrate lower discriminative power (\(AUC\): 0.769 and 0.746, respectively) and substantial specificity disparities (\(Δ_{spec}\) up to 18\% and 15\%, respectively), leading to a higher risk of misclassifications than their counterparts. These disparities reflect representational biases, defined as systematic differences in model performance across demographic or clinical subgroups. Depression detection within CI subjects yields lower overall performance, with mild improvements from low and mid-level W2V2 layers. Cross-task generalization between CI and depression classification is limited, indicating that each task depends on distinct representations. These findings emphasize the need for fairness-aware model evaluation and subgroup-specific analysis in clinical speech applications, particularly in light of demographic and clinical heterogeneity in real-world applications.

