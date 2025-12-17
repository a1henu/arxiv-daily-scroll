---
layout: default
title: Synthetic Electrogram Generation with Variational Autoencoders for ECGI
---

# Synthetic Electrogram Generation with Variational Autoencoders for ECGI
**arXiv**：[2512.14537v1](https://arxiv.org/abs/2512.14537) · [PDF](https://arxiv.org/pdf/2512.14537.pdf)  
**作者**：Miriam Gutiérrez Fernández, Karen López-Linares, Carlos Fambuena Santos, María S. Guillem, Andreu M. Climent, Óscar Barquero Pérez  

**一句话要点**：提出变分自编码器生成合成心房电图以缓解非侵入性电生理成像数据稀缺问题

**关键词**：变分自编码器, 合成心电图生成, 非侵入性电生理成像, 数据增强, 心房颤动, 深度学习

## 3 点简述
- 核心问题：心房颤动评估中，配对体表电位与心内电图数据集有限，阻碍深度学习应用。
- 方法要点：设计两种变分自编码器模型，分别针对窦性心律和心律类别，生成多通道合成心房电图。
- 实验或效果：生成电图在形态、频谱和分布相似性上评估，数据增强可适度提升下游重建任务性能。

## 摘要（原文）

> Atrial fibrillation (AF) is the most prevalent sustained cardiac arrhythmia, and its clinical assessment requires accurate characterization of atrial electrical activity. Noninvasive electrocardiographic imaging (ECGI) combined with deep learning (DL) approaches for estimating intracardiac electrograms (EGMs) from body surface potentials (BSPMs) has shown promise, but progress is hindered by the limited availability of paired BSPM-EGM datasets. To address this limitation, we investigate variational autoencoders (VAEs) for the generation of synthetic multichannel atrial EGMs. Two models are proposed: a sinus rhythm-specific VAE (VAE-S) and a class-conditioned VAE (VAE-C) trained on both sinus rhythm and AF signals. Generated EGMs are evaluated using morphological, spectral, and distributional similarity metrics. VAE-S achieves higher fidelity with respect to in silico EGMs, while VAE-C enables rhythm-specific generation at the expense of reduced sinus reconstruction quality. As a proof of concept, the generated EGMs are used for data augmentation in a downstream noninvasive EGM reconstruction task, where moderate augmentation improves estimation performance. These results demonstrate the potential of VAE-based generative modeling to alleviate data scarcity and enhance deep learning-based ECGI pipelines.

