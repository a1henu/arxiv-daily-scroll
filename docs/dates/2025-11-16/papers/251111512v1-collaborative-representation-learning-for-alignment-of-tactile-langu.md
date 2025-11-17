---
layout: default
title: Collaborative Representation Learning for Alignment of Tactile, Language, and Vision Modalities
---

# Collaborative Representation Learning for Alignment of Tactile, Language, and Vision Modalities
**arXiv**：[2511.11512v1](https://arxiv.org/abs/2511.11512) · [PDF](https://arxiv.org/pdf/2511.11512.pdf)  
**作者**：Yiyun Zhou, Mingjing Xu, Jingwei Shi, Quanjiang Li, Jingyuan Chen  

**一句话要点**：提出TLV-CoRe方法以解决触觉、语言和视觉模态对齐中的传感器冗余和交互不足问题

**关键词**：触觉表示学习, 多模态对齐, 传感器泛化, CLIP模型, 跨模态交互, RSS评估

## 3 点简述
- 核心问题：触觉传感器缺乏标准化，导致冗余特征和跨传感器泛化困难，且现有方法未充分整合多模态中间通信
- 方法要点：引入传感器感知调制器统一触觉特征，采用触觉无关解耦学习分离无关特征，并使用统一桥接适配器增强三模态交互
- 实验或效果：提出RSS评估框架，实验显示TLV-CoRe显著提升传感器无关表示学习和跨模态对齐性能

## 摘要（原文）

> Tactile sensing offers rich and complementary information to vision and language, enabling robots to perceive fine-grained object properties. However, existing tactile sensors lack standardization, leading to redundant features that hinder cross-sensor generalization. Moreover, existing methods fail to fully integrate the intermediate communication among tactile, language, and vision modalities. To address this, we propose TLV-CoRe, a CLIP-based Tactile-Language-Vision Collaborative Representation learning method. TLV-CoRe introduces a Sensor-Aware Modulator to unify tactile features across different sensors and employs tactile-irrelevant decoupled learning to disentangle irrelevant tactile features. Additionally, a Unified Bridging Adapter is introduced to enhance tri-modal interaction within the shared representation space. To fairly evaluate the effectiveness of tactile models, we further propose the RSS evaluation framework, focusing on Robustness, Synergy, and Stability across different methods. Experimental results demonstrate that TLV-CoRe significantly improves sensor-agnostic representation learning and cross-modal alignment, offering a new direction for multimodal tactile representation.

