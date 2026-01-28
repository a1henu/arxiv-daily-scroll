---
layout: default
title: A Non-Invasive 3D Gait Analysis Framework for Quantifying Psychomotor Retardation in Major Depressive Disorder
---

# A Non-Invasive 3D Gait Analysis Framework for Quantifying Psychomotor Retardation in Major Depressive Disorder
**arXiv**：[2601.19526v1](https://arxiv.org/abs/2601.19526) · [PDF](https://arxiv.org/pdf/2601.19526.pdf)  
**作者**：Fouad Boutaleb, Emery Pierson, Mohamed Daoudi, Clémence Nineuil, Ali Amad, Fabien D'Hondt  

**一句话要点**：提出非侵入式3D步态分析框架，用于量化重度抑郁症中的精神运动迟缓

**关键词**：3D步态分析, 精神运动迟缓, 单目视频, 生物力学标志物, 机器学习框架, 重度抑郁症

## 3 点简述
- 核心问题：重度抑郁症的精神运动迟缓临床评估主观，3D运动捕捉依赖专业硬件，难以常规应用。
- 方法要点：基于单目RGB视频，通过重力视图坐标和轨迹校正算法提取297个步态生物力学标志物。
- 实验或效果：在CALYPSO数据集上，检测精神运动迟缓准确率达83.3%，解释64%的抑郁严重性方差。

## 摘要（原文）

> Predicting the status of Major Depressive Disorder (MDD) from objective, non-invasive methods is an active research field. Yet, extracting automatically objective, interpretable features for a detailed analysis of the patient state remains largely unexplored.
>   Among MDD's symptoms, Psychomotor retardation (PMR) is a core item, yet its clinical assessment remains largely subjective. While 3D motion capture offers an objective alternative, its reliance on specialized hardware often precludes routine clinical use. In this paper, we propose a non-invasive computational framework that transforms monocular RGB video into clinically relevant 3D gait kinematics. Our pipeline uses Gravity-View Coordinates along with a novel trajectory-correction algorithm that leverages the closed-loop topology of our adapted Timed Up and Go (TUG) protocol to mitigate monocular depth errors. This novel pipeline enables the extraction of 297 explicit gait biomechanical biomarkers from a single camera capture.
>   To address the challenges of small clinical datasets, we introduce a stability-based machine learning framework that identifies robust motor signatures while preventing overfitting. Validated on the CALYPSO dataset, our method achieves an 83.3% accuracy in detecting PMR and explains 64% of the variance in overall depression severity (R^2=0.64). Notably, our study reveals a strong link between reduced ankle propulsion and restricted pelvic mobility to the depressive motor phenotype. These results demonstrate that physical movement serves as a robust proxy for the cognitive state, offering a transparent and scalable tool for the objective monitoring of depression in standard clinical environments.

