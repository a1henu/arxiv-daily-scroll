---
layout: default
title: Unifying Speech Editing Detection and Content Localization via Prior-Enhanced Audio LLMs
---

# Unifying Speech Editing Detection and Content Localization via Prior-Enhanced Audio LLMs
**arXiv**：[2601.21463v1](https://arxiv.org/abs/2601.21463) · [PDF](https://arxiv.org/pdf/2601.21463.pdf)  
**作者**：Jun Xue, Yi Chai, Yanzhen Ren, Jinshen He, Zhiqiang Tang, Zhuolin Yi, Yihuan Huang, Yuankun Xie, Yujie Chen  

**一句话要点**：提出PELM框架，通过先验增强音频大模型统一语音编辑检测与内容定位任务。

**关键词**：语音编辑检测, 内容定位, 音频大模型, 先验增强, 声学一致性感知

## 3 点简述
- 核心问题：现有检测方法难以应对无缝神经语音编辑技术，缺乏高质量数据集。
- 方法要点：构建AiEdit数据集，设计PELM框架，引入词级概率先验和声学一致性感知损失。
- 实验或效果：在HumanEdit和AiEdit数据集上显著优于现有方法，定位EER分别为0.57%和9.28%。

## 摘要（原文）

> Speech editing achieves semantic inversion by performing fine-grained segment-level manipulation on original utterances, while preserving global perceptual naturalness. Existing detection studies mainly focus on manually edited speech with explicit splicing artifacts, and therefore struggle to cope with emerging end-to-end neural speech editing techniques that generate seamless acoustic transitions. To address this challenge, we first construct a large-scale bilingual dataset, AiEdit, which leverages large language models to drive precise semantic tampering logic and employs multiple advanced neural speech editing methods for data synthesis, thereby filling the gap of high-quality speech editing datasets. Building upon this foundation, we propose PELM (Prior-Enhanced Audio Large Language Model), the first large-model framework that unifies speech editing detection and content localization by formulating them as an audio question answering task. To mitigate the inherent forgery bias and semantic-priority bias observed in existing audio large models, PELM incorporates word-level probability priors to provide explicit acoustic cues, and further designs a centroid-aggregation-based acoustic consistency perception loss to explicitly enforce the modeling of subtle local distribution anomalies. Extensive experimental results demonstrate that PELM significantly outperforms state-of-the-art methods on both the HumanEdit and AiEdit datasets, achieving equal error rates (EER) of 0.57\% and 9.28\% (localization), respectively.

