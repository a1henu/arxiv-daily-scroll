---
layout: default
title: Establishing Stochastic Object Models from Noisy Data via Ambient Measurement-Integrated Diffusion
---

# Establishing Stochastic Object Models from Noisy Data via Ambient Measurement-Integrated Diffusion
**arXiv**：[2512.14187v1](https://arxiv.org/abs/2512.14187) · [PDF](https://arxiv.org/pdf/2512.14187.pdf)  
**作者**：Jianwei Sun, Xiaoning Lei, Wenhao Cai, Xichen Xu, Yanshu Wang, Hu Gao  

**一句话要点**：提出AMID方法，通过噪声解耦从噪声测量中直接建立干净随机对象模型，用于医学成像分析。

**关键词**：随机对象模型, 噪声解耦, 扩散模型, 医学成像分析, 无监督学习, 图像质量评估

## 3 点简述
- 核心问题：传统随机对象模型难以捕捉真实解剖结构，数据驱动方法需干净数据，临床中常缺乏。
- 方法要点：AMID采用测量集成策略，对齐测量噪声与扩散轨迹，并建模噪声耦合，设计环境损失学习干净模型。
- 实验或效果：在真实CT和乳腺摄影数据集上，AMID在生成保真度和任务图像质量评估方面优于现有方法。

## 摘要（原文）

> Task-based measures of image quality (IQ) are critical for evaluating medical imaging systems, which must account for randomness including anatomical variability. Stochastic object models (SOMs) provide a statistical description of such variability, but conventional mathematical SOMs fail to capture realistic anatomy, while data-driven approaches typically require clean data rarely available in clinical tasks. To address this challenge, we propose AMID, an unsupervised Ambient Measurement-Integrated Diffusion with noise decoupling, which establishes clean SOMs directly from noisy measurements. AMID introduces a measurement-integrated strategy aligning measurement noise with the diffusion trajectory, and explicitly models coupling between measurement and diffusion noise across steps, an ambient loss is thus designed base on it to learn clean SOMs. Experiments on real CT and mammography datasets show that AMID outperforms existing methods in generation fidelity and yields more reliable task-based IQ evaluation, demonstrating its potential for unsupervised medical imaging analysis.

