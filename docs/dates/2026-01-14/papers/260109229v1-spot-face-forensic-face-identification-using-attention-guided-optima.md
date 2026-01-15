---
layout: default
title: SPOT-Face: Forensic Face Identification using Attention Guided Optimal Transport
---

# SPOT-Face: Forensic Face Identification using Attention Guided Optimal Transport
**arXiv**：[2601.09229v1](https://arxiv.org/abs/2601.09229) · [PDF](https://arxiv.org/pdf/2601.09229.pdf)  
**作者**：Ravi Shankar Prasad, Dinesh Singh  

**一句话要点**：提出SPOT-Face框架，通过注意力引导最优传输解决跨域法医人脸识别问题

**关键词**：法医人脸识别, 跨域匹配, 图神经网络, 最优传输, 注意力机制, 超像素图

## 3 点简述
- 核心问题：法医调查中缺乏DNA时，跨模态（如骨骼与素描）人脸识别困难，现有方法缺乏有效跨域结构对应建模
- 方法要点：基于超像素图构建，结合图神经网络提取嵌入，利用注意力引导最优传输机制建立跨域对应
- 实验或效果：在IIT_Mandi_S2F和CUFS数据集上评估，相比现有图基线，召回率和mAP指标显著提升

## 摘要（原文）

> Person identification in forensic investigations becomes very challenging when common identification means for DNA (i.e., hair strands, soft tissue) are not available. Current methods utilize deep learning methods for face recognition. However, these methods lack effective mechanisms to model cross-domain structural correspondence between two different forensic modalities. In this paper, we introduce a SPOT-Face, a superpixel graph-based framework designed for cross-domain forensic face identification of victims using their skeleton and sketch images. Our unified framework involves constructing a superpixel-based graph from an image and then using different graph neural networks(GNNs) backbones to extract the embeddings of these graphs, while cross-domain correspondence is established through attention-guided optimal transport mechanism. We have evaluated our proposed framework on two publicly available dataset: IIT\_Mandi\_S2F (S2F) and CUFS. Extensive experiments were conducted to evaluate our proposed framework. The experimental results show significant improvement in identification metrics ( i.e., Recall, mAP) over existing graph-based baselines. Furthermore, our framework demonstrates to be highly effective for matching skulls and sketches to faces in forensic investigations.

