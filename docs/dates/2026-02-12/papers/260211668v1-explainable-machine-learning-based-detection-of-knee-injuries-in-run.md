---
layout: default
title: Explainable Machine-Learning based Detection of Knee Injuries in Runners
---

# Explainable Machine-Learning based Detection of Knee Injuries in Runners
**arXiv**：[2602.11668v1](https://arxiv.org/abs/2602.11668) · [PDF](https://arxiv.org/pdf/2602.11668.pdf)  
**作者**：David Fuentes-Jiménez, Sara García-de-Villa, David Casillas-Pérez, Pablo Floría, Francisco-Manuel Melgarejo-Meseguer  

**一句话要点**：提出基于光学运动捕捉与机器学习的方法，以检测跑步者膝关节损伤相关步态模式。

**关键词**：膝关节损伤检测, 步态分析, 光学运动捕捉, 深度学习分类, 可解释性机器学习, 跑步生物力学

## 3 点简述
- 核心问题：跑步中膝关节损伤（如PFPS和ITBS）高发，需精准识别相关步态模式以辅助临床决策。
- 方法要点：利用光学运动捕捉系统分析跑步数据，结合传统点值、时间序列和混合特征，测试多种机器学习模型。
- 实验或效果：深度学习模型（如CNN）在分类任务中表现最佳，最高准确率达77.9%，并通过可解释性工具分析模型行为。

## 摘要（原文）

> Running is a widely practiced activity but shows a high incidence of knee injuries, especially Patellofemoral Pain Syndrome (PFPS) and Iliotibial Band Syndrome (ITBS). Identifying gait patterns linked to these injuries can improve clinical decision-making, which requires precise systems capable of capturing and analyzing temporal kinematic data.
>   This study uses optical motion capture systems to enhance detection of injury-related running patterns. We analyze a public dataset of 839 treadmill recordings from healthy and injured runners to evaluate how effectively these systems capture dynamic parameters relevant to injury classification. The focus is on the stance phase, using joint and segment angle time series and discrete point values.
>   Three classification tasks are addressed: healthy vs. injured, healthy vs. PFPS, and healthy vs. ITBS. We examine different feature spaces, from traditional point-based metrics to full stance-phase time series and hybrid representations. Multiple models are tested, including classical algorithms (K-Nearest Neighbors, Gaussian Processes, Decision Trees) and deep learning architectures (CNNs, LSTMs).
>   Performance is evaluated with accuracy, precision, recall, and F1-score. Explainability tools such as Shapley values, saliency maps, and Grad-CAM are used to interpret model behavior. Results show that combining time series with point values substantially improves detection. Deep learning models outperform classical ones, with CNNs achieving the highest accuracy: 77.9% for PFPS, 73.8% for ITBS, and 71.43% for the combined injury class.
>   These findings highlight the potential of motion capture systems coupled with advanced machine learning to identify knee injury-related running patterns.

