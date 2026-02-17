---
layout: default
title: S2D: Selective Spectral Decay for Quantization-Friendly Conditioning of Neural Activations
---

# S2D: Selective Spectral Decay for Quantization-Friendly Conditioning of Neural Activations
**arXiv**：[2602.14432v1](https://arxiv.org/abs/2602.14432) · [PDF](https://arxiv.org/pdf/2602.14432.pdf)  
**作者**：Arnav Chavan, Nahush Lele, Udbhav Bamba, Sankalp Dayal, Aditi Raghunathan, Deepak Gupta  

**一句话要点**：提出选择性谱衰减方法以解决大模型激活异常值导致的量化精度下降问题

**关键词**：模型量化, 激活异常值, 谱正则化, Transformer模型, 视觉语言模型

## 3 点简述
- 核心问题：大规模Transformer模型中的激活异常值加剧量化难度，与权重矩阵的奇异值直接相关
- 方法要点：通过几何原理，在微调时仅正则化对应最大奇异值的权重分量，减少激活异常值
- 实验或效果：在W4A4量化下，ImageNet上PTQ精度提升达7%，下游任务和视觉语言模型中泛化良好

## 摘要（原文）

> Activation outliers in large-scale transformer models pose a fundamental challenge to model quantization, creating excessively large ranges that cause severe accuracy drops during quantization. We empirically observe that outlier severity intensifies with pre-training scale (e.g., progressing from CLIP to the more extensively trained SigLIP and SigLIP2). Through theoretical analysis as well as empirical correlation studies, we establish the direct link between these activation outliers and dominant singular values of the weights. Building on this insight, we propose Selective Spectral Decay ($S^2D$), a geometrically-principled conditioning method that surgically regularizes only the weight components corresponding to the largest singular values during fine-tuning. Through extensive experiments, we demonstrate that $S^2D$ significantly reduces activation outliers and produces well-conditioned representations that are inherently quantization-friendly. Models trained with $S^2D$ achieve up to 7% improved PTQ accuracy on ImageNet under W4A4 quantization and 4% gains when combined with QAT. These improvements also generalize across downstream tasks and vision-language models, enabling the scaling of increasingly large and rigorously trained models without sacrificing deployment efficiency.

