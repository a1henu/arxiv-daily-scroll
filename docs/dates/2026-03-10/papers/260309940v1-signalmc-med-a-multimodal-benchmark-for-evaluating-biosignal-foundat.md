---
layout: default
title: SignalMC-MED: A Multimodal Benchmark for Evaluating Biosignal Foundation Models on Single-Lead ECG and PPG
---

# SignalMC-MED: A Multimodal Benchmark for Evaluating Biosignal Foundation Models on Single-Lead ECG and PPG
**arXiv**：[2603.09940v1](https://arxiv.org/abs/2603.09940) · [PDF](https://arxiv.org/pdf/2603.09940.pdf)  
**作者**：Fredrik K. Gustafsson, Xiao Gu, Mattia Carletti, Patitapaban Palo, David W. Eyre, David A. Clifton  

**一句话要点**：提出SignalMC-MED基准以评估生物信号基础模型在单导联ECG和PPG上的性能

**关键词**：生物信号基础模型, 单导联ECG, PPG, 多模态基准, 临床预测任务, 时序模型评估

## 3 点简述
- 核心问题：现有生物信号基础模型在长时程多模态数据上缺乏系统评估
- 方法要点：基于MC-MED数据集构建包含22,256次访问的同步ECG和PPG基准，涵盖20个临床任务
- 实验或效果：发现特定领域模型优于通用时序模型，多模态融合和全信号使用提升性能

## 摘要（原文）

> Recent biosignal foundation models (FMs) have demonstrated promising performance across diverse clinical prediction tasks, yet systematic evaluation on long-duration multimodal data remains limited. We introduce SignalMC-MED, a benchmark for evaluating biosignal FMs on synchronized single-lead electrocardiogram (ECG) and photoplethysmogram (PPG) data. Derived from the MC-MED dataset, SignalMC-MED comprises 22,256 visits with 10-minute overlapping ECG and PPG signals, and includes 20 clinically relevant tasks spanning prediction of demographics, emergency department disposition, laboratory value regression, and detection of prior ICD-10 diagnoses. Using this benchmark, we perform a systematic evaluation of representative time-series and biosignal FMs across ECG-only, PPG-only, and ECG + PPG settings. We find that domain-specific biosignal FMs consistently outperform general time-series models, and that multimodal ECG + PPG fusion yields robust improvements over unimodal inputs. Moreover, using the full 10-minute signal consistently outperforms shorter segments, and larger model variants do not reliably outperform smaller ones. Hand-crafted ECG domain features provide a strong baseline and offer complementary value when combined with learned FM representations. Together, these results establish SignalMC-MED as a standardized benchmark and provide practical guidance for evaluating and deploying biosignal FMs.

