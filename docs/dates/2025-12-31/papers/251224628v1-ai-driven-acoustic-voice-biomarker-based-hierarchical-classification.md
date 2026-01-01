---
layout: default
title: AI-Driven Acoustic Voice Biomarker-Based Hierarchical Classification of Benign Laryngeal Voice Disorders from Sustained Vowels
---

# AI-Driven Acoustic Voice Biomarker-Based Hierarchical Classification of Benign Laryngeal Voice Disorders from Sustained Vowels
**arXiv**：[2512.24628v1](https://arxiv.org/abs/2512.24628) · [PDF](https://arxiv.org/pdf/2512.24628.pdf)  
**作者**：Mohsen Annabestani, Samira Aghadoost, Anais Rameau, Olivier Elemento, Gloria Chia-Yi Chiang  

**一句话要点**：提出基于声学语音生物标志的分层机器学习框架，用于从持续元音中自动分类良性喉部嗓音障碍。

**关键词**：声学语音生物标志, 分层机器学习, 良性喉部嗓音障碍分类, 持续元音分析, 卷积神经网络, 支持向量机

## 3 点简述
- 核心问题：良性喉部嗓音障碍影响近五分之一人群，需非侵入性早期筛查与诊断分类。
- 方法要点：采用临床启发的三层分层框架，结合卷积神经网络梅尔谱特征与21个可解释声学生物标志。
- 实验或效果：在Saarbruecken语音数据库上验证，优于扁平多类分类器和预训练自监督模型，提升结构性与炎症性障碍的区分。

## 摘要（原文）

> Benign laryngeal voice disorders affect nearly one in five individuals and often manifest as dysphonia, while also serving as non-invasive indicators of broader physiological dysfunction. We introduce a clinically inspired hierarchical machine learning framework for automated classification of eight benign voice disorders alongside healthy controls, using acoustic features extracted from short, sustained vowel phonations. Experiments utilized 15,132 recordings from 1,261 speakers in the Saarbruecken Voice Database, covering vowels /a/, /i/, and /u/ at neutral, high, low, and gliding pitches. Mirroring clinical triage workflows, the framework operates in three sequential stages: Stage 1 performs binary screening of pathological versus non-pathological voices by integrating convolutional neural network-derived mel-spectrogram features with 21 interpretable acoustic biomarkers; Stage 2 stratifies voices into Healthy, Functional or Psychogenic, and Structural or Inflammatory groups using a cubic support vector machine; Stage 3 achieves fine-grained classification by incorporating probabilistic outputs from prior stages, improving discrimination of structural and inflammatory disorders relative to functional conditions. The proposed system consistently outperformed flat multi-class classifiers and pre-trained self-supervised models, including META HuBERT and Google HeAR, whose generic objectives are not optimized for sustained clinical phonation. By combining deep spectral representations with interpretable acoustic features, the framework enhances transparency and clinical alignment. These results highlight the potential of quantitative voice biomarkers as scalable, non-invasive tools for early screening, diagnostic triage, and longitudinal monitoring of vocal health.

