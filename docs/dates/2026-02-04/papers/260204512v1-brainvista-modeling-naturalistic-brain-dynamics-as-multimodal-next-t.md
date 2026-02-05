---
layout: default
title: BrainVista: Modeling Naturalistic Brain Dynamics as Multimodal Next-Token Prediction
---

# BrainVista: Modeling Naturalistic Brain Dynamics as Multimodal Next-Token Prediction
**arXiv**：[2602.04512v1](https://arxiv.org/abs/2602.04512) · [PDF](https://arxiv.org/pdf/2602.04512.pdf)  
**作者**：Xuanhua Yin, Runkai Zhao, Lina Yao, Weidong Cai  

**一句话要点**：提出BrainVista框架，通过多模态自回归建模自然态fMRI中的脑状态因果演化

**关键词**：自然态fMRI建模, 多模态自回归, 脑网络动态, 因果演化预测, fMRI编码性能

## 3 点简述
- 核心问题：自然态fMRI中多模态输入与脑网络复杂拓扑的时标不匹配阻碍脑状态因果演化建模
- 方法要点：引入网络级分词器解耦系统动态，空间混合头捕获网络间信息流，S2B掩码同步刺激与信号
- 实验或效果：在Algonauts 2025等数据集上实现SOTA fMRI编码性能，长时预测中模式相关性提升超30%

## 摘要（原文）

> Naturalistic fMRI characterizes the brain as a dynamic predictive engine driven by continuous sensory streams. However, modeling the causal forward evolution in realistic neural simulation is impeded by the timescale mismatch between multimodal inputs and the complex topology of cortical networks. To address these challenges, we introduce BrainVista, a multimodal autoregressive framework designed to model the causal evolution of brain states. BrainVista incorporates Network-wise Tokenizers to disentangle system-specific dynamics and a Spatial Mixer Head that captures inter-network information flow without compromising functional boundaries. Furthermore, we propose a novel Stimulus-to-Brain (S2B) masking mechanism to synchronize high-frequency sensory stimuli with hemodynamically filtered signals, enabling strict, history-only causal conditioning. We validate our framework on Algonauts 2025, CineBrain, and HAD, achieving state-of-the-art fMRI encoding performance. In long-horizon rollout settings, our model yields substantial improvements over baselines, increasing pattern correlation by 36.0\% and 33.3\% on relative to the strongest baseline Algonauts 2025 and CineBrain, respectively.

