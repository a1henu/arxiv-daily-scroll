---
layout: default
title: In-Hospital Stroke Prediction from PPG-Derived Hemodynamic Features
---

# In-Hospital Stroke Prediction from PPG-Derived Hemodynamic Features
**arXiv**：[2602.09328v1](https://arxiv.org/abs/2602.09328) · [PDF](https://arxiv.org/pdf/2602.09328.pdf)  
**作者**：Jiaming Liu, Cheng Ding, Daoqiang Zhang  

**一句话要点**：提出基于PPG血流动力学特征的院内卒中预测方法，利用连续监测数据实现卒中前数小时预警。

**关键词**：卒中预测, 光电容积描记术, 血流动力学特征, 深度学习模型, 院内监测, 早期预警

## 3 点简述
- 核心问题：标准临床数据缺乏卒中前生理数据，限制早期预测，需验证PPG等连续监测信号的预测价值。
- 方法要点：聚焦院内卒中患者，使用LLM辅助数据挖掘提取卒中发作时间，结合ResNet-1D模型从PPG提取特征进行预测。
- 实验或效果：在MIMIC-III和MC-MED数据集上，模型在卒中前4-6小时达到高F1分数，提供PPG预测卒中的实证证据。

## 摘要（原文）

> The absence of pre-hospital physiological data in standard clinical datasets fundamentally constrains the early prediction of stroke, as patients typically present only after stroke has occurred, leaving the predictive value of continuous monitoring signals such as photoplethysmography (PPG) unvalidated. In this work, we overcome this limitation by focusing on a rare but clinically critical cohort - patients who suffered stroke during hospitalization while already under continuous monitoring - thereby enabling the first large-scale analysis of pre-stroke PPG waveforms aligned to verified onset times. Using MIMIC-III and MC-MED, we develop an LLM-assisted data mining pipeline to extract precise in-hospital stroke onset timestamps from unstructured clinical notes, followed by physician validation, identifying 176 patients (MIMIC) and 158 patients (MC-MED) with high-quality synchronized pre-onset PPG data, respectively. We then extract hemodynamic features from PPG and employ a ResNet-1D model to predict impending stroke across multiple early-warning horizons. The model achieves F1-scores of 0.7956, 0.8759, and 0.9406 at 4, 5, and 6 hours prior to onset on MIMIC-III, and, without re-tuning, reaches 0.9256, 0.9595, and 0.9888 on MC-MED for the same horizons. These results provide the first empirical evidence from real-world clinical data that PPG contains predictive signatures of stroke several hours before onset, demonstrating that passively acquired physiological signals can support reliable early warning, supporting a shift from post-event stroke recognition to proactive, physiology-based surveillance that may materially improve patient outcomes in routine clinical care.

