---
layout: default
title: Incorporating Eye-Tracking Signals Into Multimodal Deep Visual Models For Predicting User Aesthetic Experience In Residential Interiors
---

# Incorporating Eye-Tracking Signals Into Multimodal Deep Visual Models For Predicting User Aesthetic Experience In Residential Interiors
**arXiv**：[2601.16811v1](https://arxiv.org/abs/2601.16811) · [PDF](https://arxiv.org/pdf/2601.16811.pdf)  
**作者**：Chen-Ying Chien, Po-Chih Kuo  

**一句话要点**：提出融合眼动信号的双分支CNN-LSTM框架，以预测住宅室内美学体验

**关键词**：眼动信号融合, 美学体验预测, 室内设计评估, 多模态深度学习, CNN-LSTM框架

## 3 点简述
- 核心问题：美学体验预测因主观性和视觉响应复杂性而困难
- 方法要点：使用双分支CNN-LSTM融合视觉特征与眼动信号，预测15个美学维度
- 实验或效果：模型在客观维度准确率72.2%，主观维度66.8%，优于基线，眼动训练后仅用视觉输入性能相近

## 摘要（原文）

> Understanding how people perceive and evaluate interior spaces is essential for designing environments that promote well-being. However, predicting aesthetic experiences remains difficult due to the subjective nature of perception and the complexity of visual responses. This study introduces a dual-branch CNN-LSTM framework that fuses visual features with eye-tracking signals to predict aesthetic evaluations of residential interiors. We collected a dataset of 224 interior design videos paired with synchronized gaze data from 28 participants who rated 15 aesthetic dimensions. The proposed model attains 72.2% accuracy on objective dimensions (e.g., light) and 66.8% on subjective dimensions (e.g., relaxation), outperforming state-of-the-art video baselines and showing clear gains on subjective evaluation tasks. Notably, models trained with eye-tracking retain comparable performance when deployed with visual input alone. Ablation experiments further reveal that pupil responses contribute most to objective assessments, while the combination of gaze and visual cues enhances subjective evaluations. These findings highlight the value of incorporating eye-tracking as privileged information during training, enabling more practical tools for aesthetic assessment in interior design.

