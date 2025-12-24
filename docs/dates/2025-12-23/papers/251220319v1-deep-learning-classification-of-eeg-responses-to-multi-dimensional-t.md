---
layout: default
title: Deep Learning Classification of EEG Responses to Multi-Dimensional Transcranial Electrical Stimulation
---

# Deep Learning Classification of EEG Responses to Multi-Dimensional Transcranial Electrical Stimulation
**arXiv**：[2512.20319v1](https://arxiv.org/abs/2512.20319) · [PDF](https://arxiv.org/pdf/2512.20319.pdf)  
**作者**：Alexis Pomares Pastor, Ines Ribeiro Violante, Gregory Scott  

**一句话要点**：提出基于深度学习的EEG-TES分类框架，用于临床意识水平客观测量

**关键词**：脑电图分类, 经颅电刺激, 深度学习, 意识测量, 临床神经科学

## 3 点简述
- 核心问题：缺乏客观意识测量方法，影响脑损伤等患者评估
- 方法要点：使用多维度经颅电刺激诱发EEG响应，并应用卷积神经网络分类
- 实验或效果：在未见参与者数据上达到92% F1分数，超越人类水平

## 摘要（原文）

> A major shortcoming of medical practice is the lack of an objective measure of conscious level. Impairment of consciousness is common, e.g. following brain injury and seizures, which can also interfere with sensory processing and volitional responses. This is also an important pitfall in neurophysiological methods that infer awareness via command following, e.g. using functional MRI or electroencephalography (EEG).
>   Transcranial electrical stimulation (TES) can be employed to non-invasively stimulate the brain, bypassing sensory inputs, and has already showed promising results in providing reliable indicators of brain state. However, current non-invasive solutions have been limited to magnetic stimulation, which is not easily translatable to clinical settings. Our long-term vision is to develop an objective measure of brain state that can be used at the bedside, without requiring patients to understand commands or initiate motor responses.
>   In this study, we demonstrated the feasibility of a framework using Deep Learning algorithms to classify EEG brain responses evoked by a defined multi-dimensional pattern of TES. We collected EEG-TES data from 11 participants and found that delivering transcranial direct current stimulation (tDCS) to posterior cortical areas targeting the angular gyrus elicited an exceptionally reliable brain response. For this paradigm, our best Convolutional Neural Network model reached a 92% classification F1-score on Holdout data from participants never seen during training, significantly surpassing human-level performance at 60-70% accuracy.
>   These findings establish a framework for robust consciousness measurement for clinical use. In this spirit, we documented and open-sourced our datasets and codebase in full, to be used freely by the neuroscience and AI research communities, who may replicate our results with free tools like GitHub, Kaggle, and Colab.

