---
layout: default
title: Multi-Track Multimodal Learning on iMiGUE: Micro-Gesture and Emotion Recognition
---

# Multi-Track Multimodal Learning on iMiGUE: Micro-Gesture and Emotion Recognition
**arXiv**：[2512.23291v1](https://arxiv.org/abs/2512.23291) · [PDF](https://arxiv.org/pdf/2512.23291.pdf)  
**作者**：Arman Martirosyan, Shahane Tigranyan, Maria Razzhivina, Artak Aslanyan, Nazgul Salikhova, Ilya Makarov, Andrey Savchenko, Aram Avetisyan  

**一句话要点**：提出多模态框架以解决iMiGUE数据集上的微手势识别和行为情感预测任务

**关键词**：微手势识别, 行为情感预测, 多模态学习, 骨骼姿态分析, 视频理解, iMiGUE数据集

## 3 点简述
- 核心问题：微手势识别和行为情感预测需建模视频和骨骼姿态的细粒度行为模式
- 方法要点：使用MViTv2-S和2s-AGCN提取多模态嵌入，通过Cross-Modal Token Fusion和InterFusion模块融合信息
- 实验或效果：在MiGA 2025挑战中，行为情感预测任务获得第二名，验证了方法的鲁棒性

## 摘要（原文）

> Micro-gesture recognition and behavior-based emotion prediction are both highly challenging tasks that require modeling subtle, fine-grained human behaviors, primarily leveraging video and skeletal pose data. In this work, we present two multimodal frameworks designed to tackle both problems on the iMiGUE dataset. For micro-gesture classification, we explore the complementary strengths of RGB and 3D pose-based representations to capture nuanced spatio-temporal patterns. To comprehensively represent gestures, video, and skeletal embeddings are extracted using MViTv2-S and 2s-AGCN, respectively. Then, they are integrated through a Cross-Modal Token Fusion module to combine spatial and pose information. For emotion recognition, our framework extends to behavior-based emotion prediction, a binary classification task identifying emotional states based on visual cues. We leverage facial and contextual embeddings extracted using SwinFace and MViTv2-S models and fuse them through an InterFusion module designed to capture emotional expressions and body gestures. Experiments conducted on the iMiGUE dataset, within the scope of the MiGA 2025 Challenge, demonstrate the robust performance and accuracy of our method in the behavior-based emotion prediction task, where our approach secured 2nd place.

