---
layout: default
title: ImmuVis: Hyperconvolutional Foundation Model for Imaging Mass Cytometry
---

# ImmuVis: Hyperconvolutional Foundation Model for Imaging Mass Cytometry
**arXiv**：[2602.04585v1](https://arxiv.org/abs/2602.04585) · [PDF](https://arxiv.org/pdf/2602.04585.pdf)  
**作者**：Marcin Możejko, Dawid Uchal, Krzysztof Gogolewski, Piotr Kupidura, Szymon Łukasik, Jakub Giezgała, Tomasz Nocoń, Kacper Pietrzyk, Robert Pieniuta, Mateusz Sulimowicz, Michal Orzyłowski, Tomasz Siłkowski, Karol Zagródka, Eike Staub, Ewa Szczurek  

**一句话要点**：提出ImmuVis超卷积基础模型，通过标记自适应超卷积解决成像质谱流式细胞术中标记集可变性问题。

**关键词**：成像质谱流式细胞术, 超卷积, 基础模型, 自监督学习, 标记自适应, 不确定性校准

## 3 点简述
- 核心问题：成像质谱流式细胞术缺乏固定通道空间，标记集因研究而异，违反标准视觉骨干网络假设。
- 方法要点：引入标记自适应超卷积，从学习到的标记嵌入生成卷积核，使单一模型无需重训练即可处理任意标记子集。
- 实验或效果：在IMC17M数据集上自监督预训练，虚拟染色和下游分类任务中优于SOTA基线，计算成本低且提供校准不确定性。

## 摘要（原文）

> We present ImmuVis, an efficient convolutional foundation model for imaging mass cytometry (IMC), a high-throughput multiplex imaging technology that handles molecular marker measurements as image channels and enables large-scale spatial tissue profiling. Unlike natural images, multiplex imaging lacks a fixed channel space, as real-world marker sets vary across studies, violating a core assumption of standard vision backbones. To address this, ImmuVis introduces marker-adaptive hyperconvolutions that generate convolutional kernels from learned marker embeddings, enabling a single model to operate on arbitrary measured marker subsets without retraining. We pretrain ImmuVis on the largest to-date dataset, IMC17M (28 cohorts, 24,405 images, 265 markers, over 17M patches), using self-supervised masked reconstruction. ImmuVis outperforms SOTA baselines and ablations in virtual staining and downstream classification tasks at substantially lower compute cost than transformer-based alternatives, and is the sole model that provides calibrated uncertainty via a heteroscedastic likelihood objective. These results position ImmuVis as a practical, efficient foundation model for real-world IMC modeling.

