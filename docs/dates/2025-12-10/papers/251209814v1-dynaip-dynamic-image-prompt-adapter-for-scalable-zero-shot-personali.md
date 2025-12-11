---
layout: default
title: DynaIP: Dynamic Image Prompt Adapter for Scalable Zero-shot Personalized Text-to-Image Generation
---

# DynaIP: Dynamic Image Prompt Adapter for Scalable Zero-shot Personalized Text-to-Image Generation
**arXiv**：[2512.09814v1](https://arxiv.org/abs/2512.09814) · [PDF](https://arxiv.org/pdf/2512.09814.pdf)  
**作者**：Zhizhong Wang, Tianyi Chu, Zeyi Huang, Nanyang Wang, Kehan Li  

**一句话要点**：提出DynaIP动态图像提示适配器，以增强零样本个性化文本到图像生成的细粒度保真度、概念-提示平衡和主题可扩展性。

**关键词**：个性化文本到图像生成, 零样本学习, 多模态扩散变换器, 动态解耦策略, 分层特征融合, 多主题可扩展性

## 3 点简述
- 核心问题：现有方法在概念保留与提示跟随平衡、细粒度细节保留和多主题可扩展性方面存在挑战。
- 方法要点：基于MM-DiT的解耦学习行为，设计动态解耦策略和分层专家混合特征融合模块，提升性能。
- 实验或效果：在单主题和多主题任务中验证DynaIP优于现有方法，推动领域进展。

## 摘要（原文）

> Personalized Text-to-Image (PT2I) generation aims to produce customized images based on reference images. A prominent interest pertains to the integration of an image prompt adapter to facilitate zero-shot PT2I without test-time fine-tuning. However, current methods grapple with three fundamental challenges: 1. the elusive equilibrium between Concept Preservation (CP) and Prompt Following (PF), 2. the difficulty in retaining fine-grained concept details in reference images, and 3. the restricted scalability to extend to multi-subject personalization. To tackle these challenges, we present Dynamic Image Prompt Adapter (DynaIP), a cutting-edge plugin to enhance the fine-grained concept fidelity, CP-PF balance, and subject scalability of SOTA T2I multimodal diffusion transformers (MM-DiT) for PT2I generation. Our key finding is that MM-DiT inherently exhibit decoupling learning behavior when injecting reference image features into its dual branches via cross attentions. Based on this, we design an innovative Dynamic Decoupling Strategy that removes the interference of concept-agnostic information during inference, significantly enhancing the CP-PF balance and further bolstering the scalability of multi-subject compositions. Moreover, we identify the visual encoder as a key factor affecting fine-grained CP and reveal that the hierarchical features of commonly used CLIP can capture visual information at diverse granularity levels. Therefore, we introduce a novel Hierarchical Mixture-of-Experts Feature Fusion Module to fully leverage the hierarchical features of CLIP, remarkably elevating the fine-grained concept fidelity while also providing flexible control of visual granularity. Extensive experiments across single- and multi-subject PT2I tasks verify that our DynaIP outperforms existing approaches, marking a notable advancement in the field of PT2l generation.

