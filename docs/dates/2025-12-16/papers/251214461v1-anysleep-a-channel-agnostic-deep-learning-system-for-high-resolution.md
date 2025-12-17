---
layout: default
title: AnySleep: a channel-agnostic deep learning system for high-resolution sleep staging in multi-center cohorts
---

# AnySleep: a channel-agnostic deep learning system for high-resolution sleep staging in multi-center cohorts
**arXiv**：[2512.14461v1](https://arxiv.org/abs/2512.14461) · [PDF](https://arxiv.org/pdf/2512.14461.pdf)  
**作者**：Niklas Grieger, Jannik Raskob, Siamak Mehrkanoon, Stephan Bialonski  

**一句话要点**：提出AnySleep深度学习系统，用于多中心队列中高分辨率睡眠分期，支持任意EEG/EOG通道和可调时间分辨率。

**关键词**：睡眠分期, 深度学习, 多中心研究, 高分辨率分析, 脑电图, 眼电图

## 3 点简述
- 核心问题：传统睡眠分期依赖手动评分，多中心PSG数据在电极配置和受试者特征上存在差异，限制统一研究和短时标生物标志物发现。
- 方法要点：开发通道无关的深度神经网络模型，利用任意EEG或EOG数据，在可调时间分辨率下进行睡眠分期。
- 实验或效果：在21个数据集上训练验证，性能达到先进水平，支持单通道或缺失EOG，并在亚30秒时间尺度上提升生理和病理预测能力。

## 摘要（原文）

> Sleep is essential for good health throughout our lives, yet studying its dynamics requires manual sleep staging, a labor-intensive step in sleep research and clinical care. Across centers, polysomnography (PSG) recordings are traditionally scored in 30-s epochs for pragmatic, not physiological, reasons and can vary considerably in electrode count, montage, and subject characteristics. These constraints present challenges in conducting harmonized multi-center sleep studies and discovering novel, robust biomarkers on shorter timescales. Here, we present AnySleep, a deep neural network model that uses any electroencephalography (EEG) or electrooculography (EOG) data to score sleep at adjustable temporal resolutions. We trained and validated the model on over 19,000 overnight recordings from 21 datasets collected across multiple clinics, spanning nearly 200,000 hours of EEG and EOG data, to promote robust generalization across sites. The model attains state-of-the-art performance and surpasses or equals established baselines at 30-s epochs. Performance improves as more channels are provided, yet remains strong when EOG is absent or when only EOG or single EEG derivations (frontal, central, or occipital) are available. On sub-30-s timescales, the model captures short wake intrusions consistent with arousals and improves prediction of physiological characteristics (age, sex) and pathophysiological conditions (sleep apnea), relative to standard 30-s scoring. We make the model publicly available to facilitate large-scale studies with heterogeneous electrode setups and to accelerate the discovery of novel biomarkers in sleep.

