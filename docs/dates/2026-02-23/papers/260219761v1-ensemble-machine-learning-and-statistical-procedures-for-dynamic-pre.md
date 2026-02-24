---
layout: default
title: Ensemble Machine Learning and Statistical Procedures for Dynamic Predictions of Time-to-Event Outcomes
---

# Ensemble Machine Learning and Statistical Procedures for Dynamic Predictions of Time-to-Event Outcomes
**arXiv**：[2602.19761v1](https://arxiv.org/abs/2602.19761) · [PDF](https://arxiv.org/pdf/2602.19761.pdf)  
**作者**：Nina van Gerwen, Sten Willemsen, Bettina E. Hansen, Christophe Corpechot, Marco Carbone, Cynthia Levy, Maria-Carlota Londõno, Atsushi Tanaka, Palak Trivedi, Alejandra Villamil, Gideon Hirschfield, Dimitris Rizopoulos  

**一句话要点**：提出集成机器学习框架Super Learner，结合多种动态预测模型以提升原发性胆汁性胆管炎患者生存预测精度。

**关键词**：动态预测, 集成学习, 生存分析, 原发性胆汁性胆管炎, Super Learner, 机器学习

## 3 点简述
- 核心问题：动态预测时间到事件结果中，单一统计或机器学习方法难以在所有场景下最优，影响临床决策准确性。
- 方法要点：扩展Super Learner框架，通过交叉验证和定制目标函数，加权组合不同模型的动态预测输出。
- 实验或效果：在原发性胆汁性胆管炎应用中，Super Learner灵活结合多样模型，实现等同或优于单独模型的预测性能。

## 摘要（原文）

> Dynamic predictions for longitudinal and time-to-event outcomes have become a versatile tool in precision medicine. Our work is motivated by the application of dynamic predictions in the decision-making process for primary biliary cholangitis patients. For these patients, serial biomarker measurements (e.g., bilirubin and alkaline phosphatase levels) are routinely collected to inform treating physicians of the risk of liver failure and guide clinical decision-making. Two popular statistical approaches to derive dynamic predictions are joint modelling and landmarking. However, recently, machine learning techniques have also been proposed. Each approach has its merits, and no single method exists to outperform all others. Consequently, obtaining the best possible survival estimates is challenging. Therefore, we extend the Super Learner framework to combine dynamic predictions from different models and procedures. Super Learner is an ensemble learning technique that allows users to combine different prediction algorithms to improve predictive accuracy and flexibility. It uses cross-validation and different objective functions of performance (e.g., squared loss) that suit specific applications to build the optimally weighted combination of predictions from a library of candidate algorithms. In our work, we pay special attention to appropriate objective functions for Super Learner to obtain the most optimal weighted combination of dynamic predictions. In our primary biliary cholangitis application, Super Learner presented unique benefits due to its ability to flexibly combine outputs from a diverse set of models with varying assumptions for equal or better predictive performance than any model fit separately.

