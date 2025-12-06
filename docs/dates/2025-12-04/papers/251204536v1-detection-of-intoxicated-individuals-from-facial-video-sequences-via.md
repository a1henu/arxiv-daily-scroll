---
layout: default
title: Detection of Intoxicated Individuals from Facial Video Sequences via a Recurrent Fusion Model
---

# Detection of Intoxicated Individuals from Facial Video Sequences via a Recurrent Fusion Model
**arXiv**：[2512.04536v1](https://arxiv.org/abs/2512.04536) · [PDF](https://arxiv.org/pdf/2512.04536.pdf)  
**作者**：Bita Baroutian, Atefe Aghaei, Mohsen Ebrahimi Moghaddam  

**一句话要点**：提出基于图注意力网络与3D ResNet的循环融合模型，用于视频序列中酒精中毒检测

**关键词**：酒精中毒检测, 视频序列分析, 图注意力网络, 3D ResNet, 特征融合, 公共安全系统

## 3 点简述
- 核心问题：酒精中毒是全球公共健康问题，需非侵入性检测方法以减少事故。
- 方法要点：融合面部关键点图注意力网络和时空视觉特征，通过自适应优先级动态融合提升分类性能。
- 实验或效果：在自建数据集上达到95.82%准确率，优于3D-CNN和VGGFace+LSTM基线模型。

## 摘要（原文）

> Alcohol consumption is a significant public health concern and a major cause of accidents and fatalities worldwide. This study introduces a novel video-based facial sequence analysis approach dedicated to the detection of alcohol intoxication. The method integrates facial landmark analysis via a Graph Attention Network (GAT) with spatiotemporal visual features extracted using a 3D ResNet. These features are dynamically fused with adaptive prioritization to enhance classification performance. Additionally, we introduce a curated dataset comprising 3,542 video segments derived from 202 individuals to support training and evaluation. Our model is compared against two baselines: a custom 3D-CNN and a VGGFace+LSTM architecture. Experimental results show that our approach achieves 95.82% accuracy, 0.977 precision, and 0.97 recall, outperforming prior methods. The findings demonstrate the model's potential for practical deployment in public safety systems for non-invasive, reliable alcohol intoxication detection.

