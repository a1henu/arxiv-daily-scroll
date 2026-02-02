---
layout: default
title: SCOPE-PD: Explainable AI on Subjective and Clinical Objective Measurements of Parkinson's Disease for Precision Decision-Making
---

# SCOPE-PD: Explainable AI on Subjective and Clinical Objective Measurements of Parkinson's Disease for Precision Decision-Making
**arXiv**：[2601.22516v1](https://arxiv.org/abs/2601.22516) · [PDF](https://arxiv.org/pdf/2601.22516.pdf)  
**作者**：Md Mezbahul Islam, John Michael Templeton, Masrur Sobhan, Christian Poellabauer, Ananda Mohan Mondal  

**一句话要点**：提出SCOPE-PD框架，通过整合主观与客观评估实现帕金森病的可解释AI预测，以支持精准决策。

**关键词**：帕金森病预测, 可解释人工智能, 多模态框架, SHAP分析, 随机森林算法, 临床评估整合

## 3 点简述
- 核心问题：帕金森病诊断依赖主观方法，缺乏客观解释，导致预测延迟和个体化风险估计不足。
- 方法要点：集成主观和客观临床评估数据，应用机器学习技术，并利用SHAP分析增强模型可解释性。
- 实验或效果：随机森林算法在结合特征下达到98.66%准确率，识别震颤、运动迟缓和面部表情为关键预测特征。

## 摘要（原文）

> Parkinson's disease (PD) is a chronic and complex neurodegenerative disorder influenced by genetic, clinical, and lifestyle factors. Predicting this disease early is challenging because it depends on traditional diagnostic methods that face issues of subjectivity, which commonly delay diagnosis. Several objective analyses are currently in practice to help overcome the challenges of subjectivity; however, a proper explanation of these analyses is still lacking. While machine learning (ML) has demonstrated potential in supporting PD diagnosis, existing approaches often rely on subjective reports only and lack interpretability for individualized risk estimation. This study proposes SCOPE-PD, an explainable AI-based prediction framework, by integrating subjective and objective assessments to provide personalized health decisions. Subjective and objective clinical assessment data are collected from the Parkinson's Progression Markers Initiative (PPMI) study to construct a multimodal prediction framework. Several ML techniques are applied to these data, and the best ML model is selected to interpret the results. Model interpretability is examined using SHAP-based analysis. The Random Forest algorithm achieves the highest accuracy of 98.66 percent using combined features from both subjective and objective test data. Tremor, bradykinesia, and facial expression are identified as the top three contributing features from the MDS-UPDRS test in the prediction of PD.

