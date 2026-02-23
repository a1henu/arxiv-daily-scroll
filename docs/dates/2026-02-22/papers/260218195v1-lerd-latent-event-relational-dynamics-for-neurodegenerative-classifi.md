---
layout: default
title: LERD: Latent Event-Relational Dynamics for Neurodegenerative Classification
---

# LERD: Latent Event-Relational Dynamics for Neurodegenerative Classification
**arXiv**：[2602.18195v1](https://arxiv.org/abs/2602.18195) · [PDF](https://arxiv.org/pdf/2602.18195.pdf)  
**作者**：Hairong Chen, Yicheng Feng, Ziyu Jia, Samir Bhatt, Hengguan Huang  

**一句话要点**：提出LERD贝叶斯神经动力学系统，以无标注方式从多通道EEG推断潜在事件关系，用于阿尔茨海默病分类。

**关键词**：神经动力学建模, 贝叶斯推断, 脑电图分类, 阿尔茨海默病诊断, 潜在事件检测

## 3 点简述
- 核心问题：阿尔茨海默病改变脑电生理，现有方法多为黑盒，未显式建模信号生成动力学。
- 方法要点：结合连续时间事件推断与随机事件生成过程，引入电生理启发的动力学先验进行端到端贝叶斯学习。
- 实验或效果：在合成基准和真实AD EEG队列中优于基线，提供生理对齐的潜在摘要以表征群体动力学差异。

## 摘要（原文）

> Alzheimer's disease (AD) alters brain electrophysiology and disrupts multichannel EEG dynamics, making accurate and clinically useful EEG-based diagnosis increasingly important for screening and disease monitoring. However, many existing approaches rely on black-box classifiers and do not explicitly model the underlying dynamics that generate observed signals. To address these limitations, we propose LERD, an end-to-end Bayesian electrophysiological neural dynamical system that infers latent neural events and their relational structure directly from multichannel EEG without event or interaction annotations. LERD combines a continuous-time event inference module with a stochastic event-generation process to capture flexible temporal patterns, while incorporating an electrophysiology-inspired dynamical prior to guide learning in a principled way. We further provide theoretical analysis that yields a tractable bound for training and stability guarantees for the inferred relational dynamics. Extensive experiments on synthetic benchmarks and two real-world AD EEG cohorts demonstrate that LERD consistently outperforms strong baselines and yields physiology-aligned latent summaries that help characterize group-level dynamical differences.

