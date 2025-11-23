---
layout: default
title: Domain-Shared Learning and Gradual Alignment for Unsupervised Domain Adaptation Visible-Infrared Person Re-Identification
---

# Domain-Shared Learning and Gradual Alignment for Unsupervised Domain Adaptation Visible-Infrared Person Re-Identification
**arXiv**：[2511.16184v1](https://arxiv.org/abs/2511.16184) · [PDF](https://arxiv.org/pdf/2511.16184.pdf)  
**作者**：Nianchang Huang, Yi Xu, Ruida Xi, Ruida Xi, Qiang Zhang  

**一句话要点**：提出DSLGA模型以解决无监督域自适应可见光-红外行人重识别中的模态差异问题

**关键词**：无监督域自适应, 可见光-红外行人重识别, 模态差异对齐, 两阶段学习, 跨模态对齐

## 3 点简述
- 核心问题：可见光与红外数据间存在域间和域内模态差异，影响模型泛化。
- 方法要点：采用两阶段策略，先预训练共享信息，再逐步对齐跨模态数据。
- 实验或效果：在多种设置下显著优于现有域自适应方法，甚至部分监督方法。

## 摘要（原文）

> Recently, Visible-Infrared person Re-Identification (VI-ReID) has achieved remarkable performance on public datasets. However, due to the discrepancies between public datasets and real-world data, most existing VI-ReID algorithms struggle in real-life applications. To address this, we take the initiative to investigate Unsupervised Domain Adaptation Visible-Infrared person Re-Identification (UDA-VI-ReID), aiming to transfer the knowledge learned from the public data to real-world data without compromising accuracy and requiring the annotation of new samples. Specifically, we first analyze two basic challenges in UDA-VI-ReID, i.e., inter-domain modality discrepancies and intra-domain modality discrepancies. Then, we design a novel two-stage model, i.e., Domain-Shared Learning and Gradual Alignment (DSLGA), to handle these discrepancies. In the first pre-training stage, DSLGA introduces a Domain-Shared Learning Strategy (DSLS) to mitigate ineffective pre-training caused by inter-domain modality discrepancies via exploiting shared information between the source and target domains. While, in the second fine-tuning stage, DSLGA designs a Gradual Alignment Strategy (GAS) to handle the cross-modality alignment challenges between visible and infrared data caused by the large intra-domain modality discrepancies through a cluster-to-holistic alignment way. Finally, a new UDA-VI-ReID testing method i.e., CMDA-XD, is constructed for training and testing different UDA-VI-ReID models. A large amount of experiments demonstrate that our method significantly outperforms existing domain adaptation methods for VI-ReID and even some supervised methods under various settings.

