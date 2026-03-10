---
layout: default
title: Echo2ECG: Enhancing ECG Representations with Cardiac Morphology from Multi-View Echos
---

# Echo2ECG: Enhancing ECG Representations with Cardiac Morphology from Multi-View Echos
**arXiv**：[2603.08505v1](https://arxiv.org/abs/2603.08505) · [PDF](https://arxiv.org/pdf/2603.08505.pdf)  
**作者**：Michelle Espranita Liman, Özgün Turgut, Alexander Müller, Eimo Martens, Daniel Rueckert, Philip Müller  

**一句话要点**：提出Echo2ECG框架，通过多视图超声增强心电图表征以预测心脏形态表型。

**关键词**：心电图表征学习, 多模态自监督学习, 心脏形态预测, 超声心动图, 特征提取

## 3 点简述
- 核心问题：心电图无法直接测量心脏形态表型，现有方法因单视图超声对齐导致表征不匹配。
- 方法要点：采用多模态自监督学习，利用多视图超声捕获心脏形态结构来丰富心电图表征。
- 实验或效果：在分类和检索任务中表现优于基线，表征尺寸小18倍，代码已开源。

## 摘要（原文）

> Electrocardiography (ECG) is a low-cost, widely used modality for diagnosing electrical abnormalities like atrial fibrillation by capturing the heart's electrical activity. However, it cannot directly measure cardiac morphological phenotypes, such as left ventricular ejection fraction (LVEF), which typically require echocardiography (Echo). Predicting these phenotypes from ECG would enable early, accessible health screening. Existing self-supervised methods suffer from a representational mismatch by aligning ECGs to single-view Echos, which only capture local, spatially restricted anatomical snapshots. To address this, we propose Echo2ECG, a multimodal self-supervised learning framework that enriches ECG representations with the heart's morphological structure captured in multi-view Echos. We evaluate Echo2ECG as an ECG feature extractor on two clinically relevant tasks that fundamentally require morphological information: (1) classification of structural cardiac phenotypes across three datasets, and (2) retrieval of Echo studies with similar morphological characteristics using ECG queries. Our extracted ECG representations consistently outperform those of state-of-the-art unimodal and multimodal baselines across both tasks, despite being 18x smaller than the largest baseline. These results demonstrate that Echo2ECG is a robust, powerful ECG feature extractor. Our code is accessible at https://github.com/michelleespranita/Echo2ECG.

