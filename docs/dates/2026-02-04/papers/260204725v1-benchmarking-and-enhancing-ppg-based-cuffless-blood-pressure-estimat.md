---
layout: default
title: Benchmarking and Enhancing PPG-Based Cuffless Blood Pressure Estimation Methods
---

# Benchmarking and Enhancing PPG-Based Cuffless Blood Pressure Estimation Methods
**arXiv**：[2602.04725v1](https://arxiv.org/abs/2602.04725) · [PDF](https://arxiv.org/pdf/2602.04725.pdf)  
**作者**：Neville Mathew, Yidan Shen, Renjie Hu, Maham Rahimi, George Zouridakis  

**一句话要点**：提出基于标准化数据集和人口统计数据的改进方法，以提升PPG无袖带血压估计的临床准确性。

**关键词**：无袖带血压估计, 光电容积描记术, 标准化数据集, 人口统计数据, 临床精度评估, 模型改进

## 3 点简述
- 核心问题：现有PPG血压估计模型在标准化条件下未达临床精度标准，且公开数据集缺乏生理控制。
- 方法要点：创建标准化数据集NBPDB，并修改模型加入年龄、性别等人口统计数据作为输入。
- 实验或效果：改进后模型性能提升，MInception模型误差降低23%，接近AAMI/ISO标准。

## 摘要（原文）

> Cuffless blood pressure screening based on easily acquired photoplethysmography (PPG) signals offers a practical pathway toward scalable cardiovascular health assessment. Despite rapid progress, existing PPG-based blood pressure estimation models have not consistently achieved the established clinical numerical limits such as AAMI/ISO 81060-2, and prior evaluations often lack the rigorous experimental controls necessary for valid clinical assessment. Moreover, the publicly available datasets commonly used are heterogeneous and lack physiologically controlled conditions for fair benchmarking. To enable fair benchmarking under physiologically controlled conditions, we created a standardized benchmarking subset NBPDB comprising 101,453 high-quality PPG segments from 1,103 healthy adults, derived from MIMIC-III and VitalDB. Using this dataset, we systematically benchmarked several state-of-the-art PPG-based models. The results showed that none of the evaluated models met the AAMI/ISO 81060-2 accuracy requirements (mean error $<$ 5 mmHg and standard deviation $<$ 8 mmHg). To improve model accuracy, we modified these models and added patient demographic data such as age, sex, and body mass index as additional inputs. Our modifications consistently improved performance across all models. In particular, the MInception model reduced error by 23\% after adding the demographic data and yielded mean absolute errors of 4.75 mmHg (SBP) and 2.90 mmHg (DBP), achieves accuracy comparable to the numerical limits defined by AAMI/ISO accuracy standards. Our results show that existing PPG-based BP estimation models lack clinical practicality under standardized conditions, while incorporating demographic information markedly improves their accuracy and physiological validity.

