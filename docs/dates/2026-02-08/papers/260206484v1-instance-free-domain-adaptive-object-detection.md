---
layout: default
title: Instance-Free Domain Adaptive Object Detection
---

# Instance-Free Domain Adaptive Object Detection
**arXiv**：[2602.06484v1](https://arxiv.org/abs/2602.06484) · [PDF](https://arxiv.org/pdf/2602.06484.pdf)  
**作者**：Hengfu Yu, Jinhong Deng, Lixin Duan, Wen Li  

**一句话要点**：提出RSCN以解决目标域无实例的域自适应目标检测问题

**关键词**：域自适应目标检测, 实例缺失场景, 背景特征对齐, 关系一致性, 野生动物检测, 肺结节检测

## 3 点简述
- 核心问题：目标域仅含背景数据，传统域自适应方法失效
- 方法要点：基于背景特征原型对齐，并保持域内前景与背景关系一致性
- 实验或效果：在三个基准测试中显著优于现有方法

## 摘要（原文）

> While Domain Adaptive Object Detection (DAOD) has made significant strides, most methods rely on unlabeled target data that is assumed to contain sufficient foreground instances. However, in many practical scenarios (e.g., wildlife monitoring, lesion detection), collecting target domain data with objects of interest is prohibitively costly, whereas background-only data is abundant. This common practical constraint introduces a significant technical challenge: the difficulty of achieving domain alignment when target instances are unavailable, forcing adaptation to rely solely on the target background information. We formulate this challenge as the novel problem of Instance-Free Domain Adaptive Object Detection. To tackle this, we propose the Relational and Structural Consistency Network (RSCN) which pioneers an alignment strategy based on background feature prototypes while simultaneously encouraging consistency in the relationship between the source foreground features and the background features within each domain, enabling robust adaptation even without target instances. To facilitate research, we further curate three specialized benchmarks, including simulative auto-driving detection, wildlife detection, and lung nodule detection. Extensive experiments show that RSCN significantly outperforms existing DAOD methods across all three benchmarks in the instance-free scenario. The code and benchmarks will be released soon.

