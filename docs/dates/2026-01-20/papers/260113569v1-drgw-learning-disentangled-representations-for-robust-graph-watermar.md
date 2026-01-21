---
layout: default
title: DRGW: Learning Disentangled Representations for Robust Graph Watermarking
---

# DRGW: Learning Disentangled Representations for Robust Graph Watermarking
**arXiv**：[2601.13569v1](https://arxiv.org/abs/2601.13569) · [PDF](https://arxiv.org/pdf/2601.13569.pdf)  
**作者**：Jiasen Li, Yanwei Liu, Zhuoyi Shang, Xiaoyan Gu, Weiping Wang  

**一句话要点**：提出DRGW框架，通过解耦表示学习实现鲁棒图水印，保护图数据知识产权。

**关键词**：图水印, 解耦表示学习, 对抗训练, 可逆神经网络, 鲁棒性, 知识产权保护

## 3 点简述
- 核心问题：现有图水印方法因结构或表示耦合导致水印透明性和鲁棒性不足。
- 方法要点：设计对抗训练编码器学习不变结构表示，并利用可逆神经网络无损嵌入水印。
- 实验或效果：在多个基准数据集上验证了DRGW的优越有效性，确保高检测性和透明度。

## 摘要（原文）

> Graph-structured data is foundational to numerous web applications, and watermarking is crucial for protecting their intellectual property and ensuring data provenance. Existing watermarking methods primarily operate on graph structures or entangled graph representations, which compromise the transparency and robustness of watermarks due to the information coupling in representing graphs and uncontrollable discretization in transforming continuous numerical representations into graph structures. This motivates us to propose DRGW, the first graph watermarking framework that addresses these issues through disentangled representation learning. Specifically, we design an adversarially trained encoder that learns an invariant structural representation against diverse perturbations and derives a statistically independent watermark carrier, ensuring both robustness and transparency of watermarks. Meanwhile, we devise a graph-aware invertible neural network to provide a lossless channel for watermark embedding and extraction, guaranteeing high detectability and transparency of watermarks. Additionally, we develop a structure-aware editor that resolves the issue of latent modifications into discrete graph edits, ensuring robustness against structural perturbations. Experiments on diverse benchmark datasets demonstrate the superior effectiveness of DRGW.

