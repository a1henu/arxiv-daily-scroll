---
layout: default
title: PathoSyn: Imaging-Pathology MRI Synthesis via Disentangled Deviation Diffusion
---

# PathoSyn: Imaging-Pathology MRI Synthesis via Disentangled Deviation Diffusion
**arXiv**：[2512.23130v1](https://arxiv.org/abs/2512.23130) · [PDF](https://arxiv.org/pdf/2512.23130.pdf)  
**作者**：Jian Wang, Sixing Rong, Jiarui Xing, Yuling Xu, Weide Liu  

**一句话要点**：提出PathoSyn框架，通过解耦偏差扩散实现MRI成像-病理合成，以解决特征纠缠问题。

**关键词**：MRI图像合成, 解耦生成, 扩散模型, 病理建模, 解剖保真, 偏差空间学习

## 3 点简述
- 核心问题：现有生成模型在MRI合成中常导致特征纠缠，破坏解剖结构或产生不连续。
- 方法要点：将合成任务分解为确定性解剖重建和随机偏差建模，使用偏差空间扩散模型学习病理残差分布。
- 实验或效果：在肿瘤成像基准上，PathoSyn在感知真实性和解剖保真度上显著优于基线方法。

## 摘要（原文）

> We present PathoSyn, a unified generative framework for Magnetic Resonance Imaging (MRI) image synthesis that reformulates imaging-pathology as a disentangled additive deviation on a stable anatomical manifold. Current generative models typically operate in the global pixel domain or rely on binary masks, these paradigms often suffer from feature entanglement, leading to corrupted anatomical substrates or structural discontinuities. PathoSyn addresses these limitations by decomposing the synthesis task into deterministic anatomical reconstruction and stochastic deviation modeling. Central to our framework is a Deviation-Space Diffusion Model designed to learn the conditional distribution of pathological residuals, thereby capturing localized intensity variations while preserving global structural integrity by construction. To ensure spatial coherence, the diffusion process is coupled with a seam-aware fusion strategy and an inference-time stabilization module, which collectively suppress boundary artifacts and produce high-fidelity internal lesion heterogeneity. PathoSyn provides a mathematically principled pipeline for generating high-fidelity patient-specific synthetic datasets, facilitating the development of robust diagnostic algorithms in low-data regimes. By allowing interpretable counterfactual disease progression modeling, the framework supports precision intervention planning and provides a controlled environment for benchmarking clinical decision-support systems. Quantitative and qualitative evaluations on tumor imaging benchmarks demonstrate that PathoSyn significantly outperforms holistic diffusion and mask-conditioned baselines in both perceptual realism and anatomical fidelity. The source code of this work will be made publicly available.

