---
layout: default
title: Estimating the Event-Related Potential from Few EEG Trials
---

# Estimating the Event-Related Potential from Few EEG Trials
**arXiv**：[2511.23162v1](https://arxiv.org/abs/2511.23162) · [PDF](https://arxiv.org/pdf/2511.23162.pdf)  
**作者**：Anders Vestergaard Nørskov, Kasper Jørgensen, Alexander Neergaard Zahid, Morten Mørup  

**一句话要点**：提出EEG2ERP以从少量EEG试次中估计事件相关电位

**关键词**：事件相关电位估计, 不确定性建模, 自编码器, 脑电图信号处理, 零样本学习

## 3 点简述
- 核心问题：事件相关电位通常需多试次平均降噪，但试次数少时估计困难。
- 方法要点：使用不确定性感知自编码器，通过引导训练目标和方差解码器建模ERP不确定性。
- 实验或效果：在零样本跨被试场景中，相比传统平均方法，显著提升少试次下的ERP估计精度。

## 摘要（原文）

> Event-related potentials (ERP) are measurements of brain activity with wide applications in basic and clinical neuroscience, that are typically estimated using the average of many trials of electroencephalography signals (EEG) to sufficiently reduce noise and signal variability. We introduce EEG2ERP, a novel uncertainty-aware autoencoder approach that maps an arbitrary number of EEG trials to their associated ERP. To account for the ERP uncertainty we use bootstrapped training targets and introduce a separate variance decoder to model the uncertainty of the estimated ERP. We evaluate our approach in the challenging zero-shot scenario of generalizing to new subjects considering three different publicly available data sources; i) the comprehensive ERP CORE dataset that includes over 50,000 EEG trials across six ERP paradigms from 40 subjects, ii) the large P300 Speller BCI dataset, and iii) a neuroimaging dataset on face perception consisting of both EEG and magnetoencephalography (MEG) data. We consistently find that our method in the few trial regime provides substantially better ERP estimates than commonly used conventional and robust averaging procedures. EEG2ERP is the first deep learning approach to map EEG signals to their associated ERP, moving toward reducing the number of trials necessary for ERP research. Code is available at https://github.com/andersxa/EEG2ERP

