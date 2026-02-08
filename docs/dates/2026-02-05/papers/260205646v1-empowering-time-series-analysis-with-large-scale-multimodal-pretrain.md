---
layout: default
title: Empowering Time Series Analysis with Large-Scale Multimodal Pretraining
---

# Empowering Time Series Analysis with Large-Scale Multimodal Pretraining
**arXiv**：[2602.05646v1](https://arxiv.org/abs/2602.05646) · [PDF](https://arxiv.org/pdf/2602.05646.pdf)  
**作者**：Peng Chen, Siyuan Wang, Shiyan Hu, Xingjian Wu, Yang Shu, Zhongwen Rao, Meng Wang, Yijie Li, Bin Yang, Chenjuan Guo  

**一句话要点**：提出HORAI多模态基础模型以增强时间序列分析的泛化能力

**关键词**：多模态预训练, 时间序列分析, 基础模型, 零样本学习, 频率增强, 跨模态融合

## 3 点简述
- 现有时间序列基础模型缺乏多模态互补，面临统一预训练范式和大规模数据集缺失的挑战。
- 提出基于内源模态和外源知识的多模态预训练范式，并构建首个大规模多模态时间序列数据集MM-TS。
- HORAI模型通过频率增强跨模态编码器和时频解码器，在零样本预测和异常检测任务中达到最优性能。

## 摘要（原文）

> While existing time series foundation models primarily rely on large-scale unimodal pretraining, they lack complementary modalities to enhance time series understanding. Building multimodal foundation models is a natural next step, but it faces key challenges: 1) lack of a unified multimodal pretraining paradigm and large-scale multimodal corpora for time series analysis; 2) how to effectively integrate heterogeneous modalities and enhance model generalization. To address these challenges, we take an early step toward multimodal foundation models for time series analysis. We first propose a multimodal pretraining paradigm that leverages time series with endogenous modalities (derived images and text) and exogenous knowledge (real-world news), providing a comprehensive multi-view perspective for time series analysis. To support this, we develop an automated data construction pipeline to curate MM-TS, the first large-scale multimodal time series dataset spanning six domains, with up to one billion points. Then we propose HORAI, a frequency-enhanced multimodal foundation model. It integrates two core components: the Frequency-enhanced Cross-Modality Encoder and the Time-Frequency Decoder, designed to effectively fuse multimodal features and enhance model generalization across modalities and domains. After pretraining on MM-TS, HORAI achieves state-of-the-art zero-shot performance on time series forecasting and anomaly detection tasks, demonstrating strong generalization.

