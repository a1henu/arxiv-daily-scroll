---
layout: default
title: Generative Model via Quantile Assignment
---

# Generative Model via Quantile Assignment
**arXiv**：[2602.18216v1](https://arxiv.org/abs/2602.18216) · [PDF](https://arxiv.org/pdf/2602.18216.pdf)  
**作者**：Georgi Hrusanov, Oliver Y. Chén, Julien S. Bodelet  

**一句话要点**：提出NeuroSQL生成模型，通过分位数分配消除辅助网络，实现快速稳定合成数据生成。

**关键词**：生成模型, 分位数分配, 最优传输, 潜在表示学习, 合成数据生成, 无辅助网络

## 3 点简述
- 传统生成模型依赖编码器或判别器等辅助网络，导致训练不稳定和计算开销。
- NeuroSQL基于渐近近似，将潜在变量学习转化为最优传输问题，无需辅助网络。
- 在多个数据集上，NeuroSQL在图像质量、训练时间和小样本生成方面优于基准模型。

## 摘要（原文）

> Deep Generative models (DGMs) play two key roles in modern machine learning: (i) producing new information (e.g., image synthesis) and (ii) reducing dimensionality. However, traditional architectures often rely on auxiliary networks such as encoders in Variational Autoencoders (VAEs) or discriminators in Generative Adversarial Networks (GANs), which introduce training instability, computational overhead, and risks like mode collapse. We present NeuroSQL, a new generative paradigm that eliminates the need for auxiliary networks by learning low-dimensional latent representations implicitly. NeuroSQL leverages an asymptotic approximation that expresses the latent variables as the solution to an optimal transportation problem. Specifically, NeuroSQL learns the latent variables by solving a linear assignment problem and then passes the latent information to a standalone generator. We benchmark its performance against GANs, VAEs, and a budget-matched diffusion baseline on four datasets: handwritten digits (MNIST), faces (CelebA), animal faces (AFHQ), and brain images (OASIS). Compared to VAEs, GANs, and diffusion models: (1) in terms of image quality, NeuroSQL achieves overall lower mean pixel distance between synthetic and authentic images and stronger perceptual/structural fidelity; (2) computationally, NeuroSQL requires the least training time; and (3) practically, NeuroSQL provides an effective solution for generating synthetic data with limited training samples. By embracing quantile assignment rather than an encoder, NeuroSQL provides a fast, stable, and robust way to generate synthetic data with minimal information loss.

