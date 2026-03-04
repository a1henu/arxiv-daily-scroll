---
layout: default
title: Beyond Anatomy: Explainable ASD Classification from rs-fMRI via Functional Parcellation and Graph Attention Networks
---

# Beyond Anatomy: Explainable ASD Classification from rs-fMRI via Functional Parcellation and Graph Attention Networks
**arXiv**：[2603.02518v1](https://arxiv.org/abs/2603.02518) · [PDF](https://arxiv.org/pdf/2603.02518.pdf)  
**作者**：Syeda Hareem Madani, Noureen Bibi, Adam Rafiq Jeraj, Sumra Khan, Anas Zafar, Rizwan Qureshi  

**一句话要点**：提出基于功能分区和图注意力网络的rs-fMRI自闭症谱系障碍分类框架，超越解剖分区限制。

**关键词**：自闭症谱系障碍分类, 静息态功能磁共振成像, 功能分区, 图注意力网络, 图神经网络, 可解释性分析

## 3 点简述
- 核心问题：解剖分区在rs-fMRI自闭症分类中可能无法捕捉个体化连接模式。
- 方法要点：比较解剖与功能分区策略，采用图注意力网络集成提升性能。
- 实验或效果：在ABIDE I数据集上达到95.0%准确率，验证模型决策反映神经病理学。

## 摘要（原文）

> Anatomical brain parcellations dominate rs-fMRI-based Autism Spectrum Disorder (ASD) classification, yet their rigid boundaries may fail to capture the idiosyncratic connectivity patterns that characterise ASD. We present a graph-based deep learning framework comparing anatomical (AAL, 116 ROIs) and functionally-derived (MSDL, 39 ROIs) parcellation strategies on the ABIDE I dataset. Our FSL preprocessing pipeline handles multi-site heterogeneity across 400 balanced subjects, with site-stratified 70/15/15 splits to prevent data leakage. Gaussian noise augmentation within training folds expands samples from 280 to 1,680. A three phase pipeline progresses from a baseline GCN with AAL (73.3% accuracy, AUC=0.74), to an optimised GCN with MSDL (84.0%, AUC=0.84), to a Graph Attention Network ensemble achieving 95.0% accuracy (AUC=0.98), outperforming all recent GNN-based benchmarks on ABIDE I. The 10.7-point gain from atlas substitution alone demonstrates that functional parcellation is the most impactful modelling decision. Gradient-based saliency and GNNExplainer analyses converge on the Posterior Cingulate Cortex and Precuneus as core Default Mode Network hubs, validating that model decisions reflect ASD neuropathology rather than acquisition artefacts. All code and datasets will be publicly released upon acceptance.

