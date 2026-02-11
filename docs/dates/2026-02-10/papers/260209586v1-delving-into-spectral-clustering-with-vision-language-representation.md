---
layout: default
title: Delving into Spectral Clustering with Vision-Language Representations
---

# Delving into Spectral Clustering with Vision-Language Representations
**arXiv**：[2602.09586v1](https://arxiv.org/abs/2602.09586) · [PDF](https://arxiv.org/pdf/2602.09586.pdf)  
**作者**：Bo Peng, Yuanwei Hu, Bo Liu, Ling Chen, Jie Lu, Zhen Fang  

**一句话要点**：提出基于神经正切核的谱聚类方法，利用视觉-语言预训练模型增强多模态数据聚类性能。

**关键词**：谱聚类, 视觉-语言表示, 神经正切核, 多模态学习, 亲和矩阵, 无监督分析

## 3 点简述
- 核心问题：传统谱聚类多依赖单模态，未充分利用多模态表示中的丰富信息。
- 方法要点：通过神经正切核结合视觉邻近性和语义重叠，构建亲和矩阵，并引入正则化扩散机制。
- 实验或效果：在16个基准数据集上大幅超越现有方法，验证了方法的有效性和鲁棒性。

## 摘要（原文）

> Spectral clustering is known as a powerful technique in unsupervised data analysis. The vast majority of approaches to spectral clustering are driven by a single modality, leaving the rich information in multi-modal representations untapped. Inspired by the recent success of vision-language pre-training, this paper enriches the landscape of spectral clustering from a single-modal to a multi-modal regime. Particularly, we propose Neural Tangent Kernel Spectral Clustering that leverages cross-modal alignment in pre-trained vision-language models. By anchoring the neural tangent kernel with positive nouns, i.e., those semantically close to the images of interest, we arrive at formulating the affinity between images as a coupling of their visual proximity and semantic overlap. We show that this formulation amplifies within-cluster connections while suppressing spurious ones across clusters, hence encouraging block-diagonal structures. In addition, we present a regularized affinity diffusion mechanism that adaptively ensembles affinity matrices induced by different prompts. Extensive experiments on \textbf{16} benchmarks -- including classical, large-scale, fine-grained and domain-shifted datasets -- manifest that our method consistently outperforms the state-of-the-art by a large margin.

