---
layout: default
title: EEG-based Graph-guided Domain Adaptation for Robust Cross-Session Emotion Recognition
---

# EEG-based Graph-guided Domain Adaptation for Robust Cross-Session Emotion Recognition
**arXiv**：[2512.23526v1](https://arxiv.org/abs/2512.23526) · [PDF](https://arxiv.org/pdf/2512.23526.pdf)  
**作者**：Maryam Mirzaei, Farzaneh Shayegh, Hamed Narimani  

**一句话要点**：提出EGDA框架，通过图正则化域适应解决跨会话EEG情感识别中的模型泛化问题。

**关键词**：脑电图情感识别, 域适应, 图正则化, 跨会话泛化, SEED-IV数据集

## 3 点简述
- 核心问题：EEG情感识别中，不同记录会话间的数据差异阻碍模型泛化。
- 方法要点：联合对齐全局和类特定分布，并利用图正则化保持EEG内在结构。
- 实验或效果：在SEED-IV数据集上，跨三个迁移任务达到81.22%至83.27%的准确率，优于基线方法。

## 摘要（原文）

> Accurate recognition of human emotional states is critical for effective human-machine interaction. Electroencephalography (EEG) offers a reliable source for emotion recognition due to its high temporal resolution and its direct reflection of neural activity. Nevertheless, variations across recording sessions present a major challenge for model generalization. To address this issue, we propose EGDA, a framework that reduces cross-session discrepancies by jointly aligning the global (marginal) and class-specific (conditional) distributions, while preserving the intrinsic structure of EEG data through graph regularization. Experimental results on the SEED-IV dataset demonstrate that EGDA achieves robust cross-session performance, obtaining accuracies of 81.22%, 80.15%, and 83.27% across three transfer tasks, and surpassing several baseline methods. Furthermore, the analysis highlights the Gamma frequency band as the most discriminative and identifies the central-parietal and prefrontal brain regions as critical for reliable emotion recognition.

