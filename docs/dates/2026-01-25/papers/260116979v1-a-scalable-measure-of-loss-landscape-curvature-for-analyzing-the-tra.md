---
layout: default
title: A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs
---

# A Scalable Measure of Loss Landscape Curvature for Analyzing the Training Dynamics of LLMs
**arXiv**：[2601.16979v1](https://arxiv.org/abs/2601.16979) · [PDF](https://arxiv.org/pdf/2601.16979.pdf)  
**作者**：Dayal Singh Kalra, Jean-Christophe Gagnon-Audet, Andrey Gromov, Ishita Mediratta, Kelvin Niu, Alexander H Miller, Michael Shvartsman  

**一句话要点**：提出临界锐度以高效分析大语言模型训练动态中的损失景观曲率

**关键词**：损失景观曲率, 训练动态分析, 大语言模型, 临界锐度, 数据混合策略, 计算效率

## 3 点简述
- 核心问题：直接测量Hessian锐度计算成本高，难以用于大语言模型训练动态分析。
- 方法要点：引入临界锐度，基于更新方向仅需少于10次前向传播，高效近似Hessian锐度。
- 实验或效果：在OLMo-2模型上首次大规模验证渐进锐化和稳定性边缘现象，并应用相对临界锐度指导数据混合。

## 摘要（原文）

> Understanding the curvature evolution of the loss landscape is fundamental to analyzing the training dynamics of neural networks. The most commonly studied measure, Hessian sharpness ($λ_{\max}^H$) -- the largest eigenvalue of the loss Hessian -- determines local training stability and interacts with the learning rate throughout training. Despite its significance in analyzing training dynamics, direct measurement of Hessian sharpness remains prohibitive for Large Language Models (LLMs) due to high computational cost. We analyze $\textit{critical sharpness}$ ($λ_c$), a computationally efficient measure requiring fewer than $10$ forward passes given the update direction $Δ\mathbfθ$. Critically, this measure captures well-documented Hessian sharpness phenomena, including progressive sharpening and Edge of Stability. Using this measure, we provide the first demonstration of these sharpness phenomena at scale, up to $7$B parameters, spanning both pre-training and mid-training of OLMo-2 models. We further introduce $\textit{relative critical sharpness}$ ($λ_c^{1\to 2}$), which quantifies the curvature of one loss landscape while optimizing another, to analyze the transition from pre-training to fine-tuning and guide data mixing strategies. Critical sharpness provides practitioners with a practical tool for diagnosing curvature dynamics and informing data composition choices at scale. More broadly, our work shows that scalable curvature measures can provide actionable insights for large-scale training.

