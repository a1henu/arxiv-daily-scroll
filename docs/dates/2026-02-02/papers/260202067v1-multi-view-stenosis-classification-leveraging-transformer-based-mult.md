---
layout: default
title: Multi-View Stenosis Classification Leveraging Transformer-Based Multiple-Instance Learning Using Real-World Clinical Data
---

# Multi-View Stenosis Classification Leveraging Transformer-Based Multiple-Instance Learning Using Real-World Clinical Data
**arXiv**：[2602.02067v1](https://arxiv.org/abs/2602.02067) · [PDF](https://arxiv.org/pdf/2602.02067.pdf)  
**作者**：Nikola Cenikj, Özgün Turgut, Alexander Müller, Alexander Steger, Jan Kehrer, Marcus Brugger, Daniel Rueckert, Eimo Martens, Philip Müller  

**一句话要点**：提出SegmentMIL，基于Transformer的多视图多示例学习框架，用于患者级冠状动脉狭窄分类。

**关键词**：冠状动脉狭窄分类, 多视图学习, 多示例学习, Transformer, 患者级监督, 临床诊断

## 3 点简述
- 核心问题：冠状动脉狭窄诊断依赖多视图分析，现有单视图模型需昂贵视图级标注且忽略视图间动态依赖。
- 方法要点：SegmentMIL利用Transformer处理多视图数据，仅需患者级监督，无需视图级标注，同时预测狭窄存在并定位受影响解剖区域。
- 实验或效果：在真实临床数据集上，SegmentMIL在内外评估中表现优异，超越视图级模型和经典MIL基线，具有临床可行性和可扩展性。

## 摘要（原文）

> Coronary artery stenosis is a leading cause of cardiovascular disease, diagnosed by analyzing the coronary arteries from multiple angiography views. Although numerous deep-learning models have been proposed for stenosis detection from a single angiography view, their performance heavily relies on expensive view-level annotations, which are often not readily available in hospital systems. Moreover, these models fail to capture the temporal dynamics and dependencies among multiple views, which are crucial for clinical diagnosis. To address this, we propose SegmentMIL, a transformer-based multi-view multiple-instance learning framework for patient-level stenosis classification. Trained on a real-world clinical dataset, using patient-level supervision and without any view-level annotations, SegmentMIL jointly predicts the presence of stenosis and localizes the affected anatomical region, distinguishing between the right and left coronary arteries and their respective segments. SegmentMIL obtains high performance on internal and external evaluations and outperforms both view-level models and classical MIL baselines, underscoring its potential as a clinically viable and scalable solution for coronary stenosis diagnosis. Our code is available at https://github.com/NikolaCenic/mil-stenosis.

