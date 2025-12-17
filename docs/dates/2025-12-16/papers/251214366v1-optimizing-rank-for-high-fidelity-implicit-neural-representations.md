---
layout: default
title: Optimizing Rank for High-Fidelity Implicit Neural Representations
---

# Optimizing Rank for High-Fidelity Implicit Neural Representations
**arXiv**：[2512.14366v1](https://arxiv.org/abs/2512.14366) · [PDF](https://arxiv.org/pdf/2512.14366.pdf)  
**作者**：Julian McGinnis, Florian A. Hölzl, Suprosanna Shit, Florentin Bieder, Paul Friedrich, Mark Mühlau, Björn Menze, Daniel Rueckert, Benedikt Wiestler  

**一句话要点**：提出通过优化网络秩来提升隐式神经表示的高频信号保真度

**关键词**：隐式神经表示, 网络秩优化, 高频信号学习, Muon优化器, 多领域应用

## 3 点简述
- 核心问题：传统MLP在隐式神经表示中难以学习高频内容，常归因于架构限制
- 方法要点：研究发现低频偏差源于训练中秩退化，通过调节秩（如使用Muon优化器）改善信号保真度
- 实验或效果：在自然图像、医学图像和新视角合成等任务中，PSNR提升高达9dB，超越现有方法

## 摘要（原文）

> Implicit Neural Representations (INRs) based on vanilla Multi-Layer Perceptrons (MLPs) are widely believed to be incapable of representing high-frequency content. This has directed research efforts towards architectural interventions, such as coordinate embeddings or specialized activation functions, to represent high-frequency signals. In this paper, we challenge the notion that the low-frequency bias of vanilla MLPs is an intrinsic, architectural limitation to learn high-frequency content, but instead a symptom of stable rank degradation during training. We empirically demonstrate that regulating the network's rank during training substantially improves the fidelity of the learned signal, rendering even simple MLP architectures expressive. Extensive experiments show that using optimizers like Muon, with high-rank, near-orthogonal updates, consistently enhances INR architectures even beyond simple ReLU MLPs. These substantial improvements hold across a diverse range of domains, including natural and medical images, and novel view synthesis, with up to 9 dB PSNR improvements over the previous state-of-the-art. Our project page, which includes code and experimental results, is available at: (https://muon-inrs.github.io).

