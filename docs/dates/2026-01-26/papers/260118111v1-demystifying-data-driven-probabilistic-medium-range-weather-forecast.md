---
layout: default
title: Demystifying Data-Driven Probabilistic Medium-Range Weather Forecasting
---

# Demystifying Data-Driven Probabilistic Medium-Range Weather Forecasting
**arXiv**：[2601.18111v1](https://arxiv.org/abs/2601.18111) · [PDF](https://arxiv.org/pdf/2601.18111.pdf)  
**作者**：Jean Kossaifi, Nikola Kovachki, Morteza Mardani, Daniel Leibovici, Suman Ravuri, Ira Shokar, Edoardo Calvello, Mohammad Shoaib Abbas, Peter Harrington, Ashay Subramaniam, Noah Brenowitz, Boris Bonev, Wonmin Byeon, Karsten Kreis, Dale Durran, Arash Vahdat, Mike Pritchard, Jan Kautz  

**一句话要点**：提出可扩展框架以简化数据驱动的中程概率天气预报，无需复杂架构或专门训练策略。

**关键词**：概率天气预报, 数据驱动方法, 多尺度建模, 可扩展框架, 大气动力学, 概率估计器

## 3 点简述
- 核心问题：数据驱动天气预报方法碎片化，复杂架构和训练策略掩盖了准确性的关键驱动因素。
- 方法要点：结合下采样潜在空间和历史条件局部投影器，学习多尺度大气动力学，支持多种概率估计器。
- 实验或效果：验证显示在多数变量上优于集成预报系统和GenCast模型，实现统计显著改进。

## 摘要（原文）

> The recent revolution in data-driven methods for weather forecasting has lead to a fragmented landscape of complex, bespoke architectures and training strategies, obscuring the fundamental drivers of forecast accuracy. Here, we demonstrate that state-of-the-art probabilistic skill requires neither intricate architectural constraints nor specialized training heuristics. We introduce a scalable framework for learning multi-scale atmospheric dynamics by combining a directly downsampled latent space with a history-conditioned local projector that resolves high-resolution physics. We find that our framework design is robust to the choice of probabilistic estimator, seamlessly supporting stochastic interpolants, diffusion models, and CRPS-based ensemble training. Validated against the Integrated Forecasting System and the deep learning probabilistic model GenCast, our framework achieves statistically significant improvements on most of the variables. These results suggest scaling a general-purpose model is sufficient for state-of-the-art medium-range prediction, eliminating the need for tailored training recipes and proving effective across the full spectrum of probabilistic frameworks.

