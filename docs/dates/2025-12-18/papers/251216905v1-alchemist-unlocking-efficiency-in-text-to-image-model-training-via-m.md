---
layout: default
title: Alchemist: Unlocking Efficiency in Text-to-Image Model Training via Meta-Gradient Data Selection
---

# Alchemist: Unlocking Efficiency in Text-to-Image Model Training via Meta-Gradient Data Selection
**arXiv**：[2512.16905v1](https://arxiv.org/abs/2512.16905) · [PDF](https://arxiv.org/pdf/2512.16905.pdf)  
**作者**：Kaixin Ding, Yang Zhou, Xi Chen, Miao Yang, Jiarong Ou, Rui Chen, Xin Tao, Hengshuang Zhao  

**一句话要点**：提出Alchemist框架，通过元梯度数据选择提升文本到图像模型训练效率

**关键词**：文本到图像生成, 数据选择, 元梯度学习, 训练效率, 多粒度感知

## 3 点简述
- 核心问题：文本到图像模型训练受低质量或冗余数据限制，影响视觉质量和计算效率。
- 方法要点：基于元梯度自动学习样本影响力，结合多粒度感知和Shift-G采样策略选择数据子集。
- 实验或效果：在合成和网络爬取数据集上验证，使用50%数据可超越全数据集训练效果。

## 摘要（原文）

> Recent advances in Text-to-Image (T2I) generative models, such as Imagen, Stable Diffusion, and FLUX, have led to remarkable improvements in visual quality. However, their performance is fundamentally limited by the quality of training data. Web-crawled and synthetic image datasets often contain low-quality or redundant samples, which lead to degraded visual fidelity, unstable training, and inefficient computation. Hence, effective data selection is crucial for improving data efficiency. Existing approaches rely on costly manual curation or heuristic scoring based on single-dimensional features in Text-to-Image data filtering. Although meta-learning based method has been explored in LLM, there is no adaptation for image modalities. To this end, we propose **Alchemist**, a meta-gradient-based framework to select a suitable subset from large-scale text-image data pairs. Our approach automatically learns to assess the influence of each sample by iteratively optimizing the model from a data-centric perspective. Alchemist consists of two key stages: data rating and data pruning. We train a lightweight rater to estimate each sample's influence based on gradient information, enhanced with multi-granularity perception. We then use the Shift-Gsampling strategy to select informative subsets for efficient model training. Alchemist is the first automatic, scalable, meta-gradient-based data selection framework for Text-to-Image model training. Experiments on both synthetic and web-crawled datasets demonstrate that Alchemist consistently improves visual quality and downstream performance. Training on an Alchemist-selected 50% of the data can outperform training on the full dataset.

