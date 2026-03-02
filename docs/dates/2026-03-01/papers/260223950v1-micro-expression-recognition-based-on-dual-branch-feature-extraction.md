---
layout: default
title: Micro-expression Recognition Based on Dual-branch Feature Extraction and Fusion
---

# Micro-expression Recognition Based on Dual-branch Feature Extraction and Fusion
**arXiv**：[2602.23950v1](https://arxiv.org/abs/2602.23950) · [PDF](https://arxiv.org/pdf/2602.23950.pdf)  
**作者**：Mingjie Zhang, Bo Li, Wanting Liu, Hongyan Cui, Yue Li, Qingwen Li, Hong Li, Ge Gao  

**一句话要点**：提出双分支特征提取与融合网络以解决微表情识别中光流方法的挑战

**关键词**：微表情识别, 双分支网络, 特征融合, 并行注意力, 残差网络, Inception网络

## 3 点简述
- 核心问题：微表情短暂细微，现有光流方法识别困难
- 方法要点：结合残差网络和Inception网络，集成并行注意力与自适应特征融合
- 实验或效果：在CASME II数据集上准确率达74.67%，优于LBP-TOP和MSMMT等方法

## 摘要（原文）

> Micro-expressions, characterized by transience and subtlety, pose challenges to existing optical flow-based recognition methods. To address this, this paper proposes a dual-branch micro-expression feature extraction network integrated with parallel attention. Key contributions include: 1) a residual network designed to alleviate gradient anishing and network degradation; 2) an Inception network constructed to enhance model representation and suppress interference from irrelevant regions; 3) an adaptive feature fusion module developed to integrate dual-branch features. Experiments on the CASME II dataset demonstrate that the proposed method achieves 74.67% accuracy, outperforming LBP-TOP (by 11.26%), MSMMT (by 3.36%), and other comparative methods.

