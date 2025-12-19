---
layout: default
title: Semi-Supervised Multi-View Crowd Counting by Ranking Multi-View Fusion Models
---

# Semi-Supervised Multi-View Crowd Counting by Ranking Multi-View Fusion Models
**arXiv**：[2512.16243v1](https://arxiv.org/abs/2512.16243) · [PDF](https://arxiv.org/pdf/2512.16243.pdf)  
**作者**：Qi Zhang, Yunfei Gong, Zhidan Xie, Zhizi Wang, Antoni B. Chan, Hui Huang  

**一句话要点**：提出基于多视图融合模型排序的半监督多视图人群计数方法以解决数据有限问题

**关键词**：多视图人群计数, 半监督学习, 模型排序, 数据增强, 不确定性估计

## 3 点简述
- 核心问题：多视图人群计数因数据收集和标注困难导致数据集规模有限，影响模型性能。
- 方法要点：通过排序多视图融合模型的预测或不确定性，引入半监督约束，减少对标注数据的依赖。
- 实验或效果：实验表明，所提方法优于其他半监督计数方法，验证了模型排序的有效性。

## 摘要（原文）

> Multi-view crowd counting has been proposed to deal with the severe occlusion issue of crowd counting in large and wide scenes. However, due to the difficulty of collecting and annotating multi-view images, the datasets for multi-view counting have a limited number of multi-view frames and scenes. To solve the problem of limited data, one approach is to collect synthetic data to bypass the annotating step, while another is to propose semi- or weakly-supervised or unsupervised methods that demand less multi-view data. In this paper, we propose two semi-supervised multi-view crowd counting frameworks by ranking the multi-view fusion models of different numbers of input views, in terms of the model predictions or the model uncertainties. Specifically, for the first method (vanilla model), we rank the multi-view fusion models' prediction results of different numbers of camera-view inputs, namely, the model's predictions with fewer camera views shall not be larger than the predictions with more camera views. For the second method, we rank the estimated model uncertainties of the multi-view fusion models with a variable number of view inputs, guided by the multi-view fusion models' prediction errors, namely, the model uncertainties with more camera views shall not be larger than those with fewer camera views. These constraints are introduced into the model training in a semi-supervised fashion for multi-view counting with limited labeled data. The experiments demonstrate the advantages of the proposed multi-view model ranking methods compared with other semi-supervised counting methods.

