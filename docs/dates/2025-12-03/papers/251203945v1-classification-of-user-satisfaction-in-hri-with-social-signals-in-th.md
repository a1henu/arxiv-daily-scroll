---
layout: default
title: Classification of User Satisfaction in HRI with Social Signals in the Wild
---

# Classification of User Satisfaction in HRI with Social Signals in the Wild
**arXiv**：[2512.03945v1](https://arxiv.org/abs/2512.03945) · [PDF](https://arxiv.org/pdf/2512.03945.pdf)  
**作者**：Michael Schiffmann, Sabina Jeschke, Anja Richert  

**一句话要点**：提出基于社交信号的时间序列分类方法，以自动评估人机交互中的用户满意度。

**关键词**：社交信号分析, 时间序列分类, 用户满意度评估, 人机交互, 野外数据集

## 3 点简述
- 核心问题：如何自动评估社交交互代理的用户满意度，替代传统问卷或系统指标方法。
- 方法要点：利用身体姿态、面部表情和物理距离的社交信号时间序列，结合特征工程和机器学习模型进行分类。
- 实验或效果：在野外数据集上验证方法，能可靠识别低满意度交互，无需手动标注数据。

## 摘要（原文）

> Socially interactive agents (SIAs) are being used in various scenarios and are nearing productive deployment. Evaluating user satisfaction with SIAs' performance is a key factor in designing the interaction between the user and SIA. Currently, subjective user satisfaction is primarily assessed manually through questionnaires or indirectly via system metrics. This study examines the automatic classification of user satisfaction through analysis of social signals, aiming to enhance both manual and autonomous evaluation methods for SIAs. During a field trial at the Deutsches Museum Bonn, a Furhat Robotics head was employed as a service and information hub, collecting an "in-the-wild" dataset. This dataset comprises 46 single-user interactions, including questionnaire responses and video data. Our method focuses on automatically classifying user satisfaction based on time series classification. We use time series of social signal metrics derived from the body pose, time series of facial expressions, and physical distance. This study compares three feature engineering approaches on different machine learning models. The results confirm the method's effectiveness in reliably identifying interactions with low user satisfaction without the need for manually annotated datasets. This approach offers significant potential for enhancing SIA performance and user experience through automated feedback mechanisms.

