---
layout: default
title: SHINE: Sequential Hierarchical Integration Network for EEG and MEG
---

# SHINE: Sequential Hierarchical Integration Network for EEG and MEG
**arXiv**：[2602.23960v1](https://arxiv.org/abs/2602.23960) · [PDF](https://arxiv.org/pdf/2602.23960.pdf)  
**作者**：Xiran Xu, Yujie Yan, Xihong Wu, Jing Chen  

**一句话要点**：提出SHINE网络，从MEG信号中重建语音-静默序列，用于脑机接口的语音检测任务

**关键词**：脑磁图信号处理, 语音检测, 序列重建, 分层神经网络, 脑机接口竞赛

## 3 点简述
- 核心问题：如何从脑磁图信号中准确检测自然语音的存在与静默状态
- 方法要点：设计序列化分层集成网络，结合语音包络和梅尔谱图辅助训练
- 实验效果：在LibriBrain竞赛测试集上，集成方法达到0.9184的F1-macro分数

## 摘要（原文）

> How natural speech is represented in the brain constitutes a major challenge for cognitive neuroscience, with cortical envelope-following responses playing a central role in speech decoding. This paper presents our approach to the Speech Detection task in the LibriBrain Competition 2025, utilizing over 50 hours of magnetoencephalography (MEG) signals from a single participant listening to LibriVox audiobooks. We introduce the proposed Sequential Hierarchical Integration Network for EEG and MEG (SHINE) to reconstruct the binary speech-silence sequences from MEG signals. In the Extended Track, we further incorporated auxiliary reconstructions of speech envelopes and Mel spectrograms to enhance training. Ensemble methods combining SHINE with baselines (BrainMagic, AWavNet, ConvConcatNet) achieved F1-macro scores of 0.9155 (Standard Track) and 0.9184 (Extended Track) on the leaderboard test set.

