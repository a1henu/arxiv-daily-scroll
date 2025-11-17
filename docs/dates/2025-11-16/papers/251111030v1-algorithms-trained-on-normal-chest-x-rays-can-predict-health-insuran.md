---
layout: default
title: Algorithms Trained on Normal Chest X-rays Can Predict Health Insurance Types
---

# Algorithms Trained on Normal Chest X-rays Can Predict Health Insurance Types
**arXiv**：[2511.11030v1](https://arxiv.org/abs/2511.11030) · [PDF](https://arxiv.org/pdf/2511.11030.pdf)  
**作者**：Chi-Yu Chen, Rawan Abulibdeh, Arash Asgari, Leo Anthony Celi, Deirdre Goode, Hassan Hamidi, Laleh Seyyed-Kalantari, Po-Chih Kuo, Ned McCague, Thomas Sounack  

**一句话要点**：基于正常胸部X光片预测健康保险类型，揭示医疗AI中的社会不平等信号

**关键词**：胸部X光分析, 医疗AI公平性, 社会经济预测, 深度学习模型, 图像特征提取, 社会不平等检测

## 3 点简述
- 核心问题：医疗AI模型能否从正常胸部X光片中检测社会不平等，如健康保险类型作为社会经济地位代理。
- 方法要点：使用DenseNet121、SwinV2-B和MedMamba等先进架构，在MIMIC-CXR-JPG和CheXpert数据集上训练。
- 实验效果：模型预测AUC约0.67-0.68，信号在控制年龄、种族和性别后仍存在，且呈弥散分布。

## 摘要（原文）

> Artificial intelligence is revealing what medicine never intended to encode. Deep vision models, trained on chest X-rays, can now detect not only disease but also invisible traces of social inequality. In this study, we show that state-of-the-art architectures (DenseNet121, SwinV2-B, MedMamba) can predict a patient's health insurance type, a strong proxy for socioeconomic status, from normal chest X-rays with significant accuracy (AUC around 0.67 on MIMIC-CXR-JPG, 0.68 on CheXpert). The signal persists even when age, race, and sex are controlled for, and remains detectable when the model is trained exclusively on a single racial group. Patch-based occlusion reveals that the signal is diffuse rather than localized, embedded in the upper and mid-thoracic regions. This suggests that deep networks may be internalizing subtle traces of clinical environments, equipment differences, or care pathways; learning socioeconomic segregation itself. These findings challenge the assumption that medical images are neutral biological data. By uncovering how models perceive and exploit these hidden social signatures, this work reframes fairness in medical AI: the goal is no longer only to balance datasets or adjust thresholds, but to interrogate and disentangle the social fingerprints embedded in clinical data itself.

