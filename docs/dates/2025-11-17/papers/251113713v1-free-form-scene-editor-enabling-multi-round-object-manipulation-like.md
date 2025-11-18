---
layout: default
title: Free-Form Scene Editor: Enabling Multi-Round Object Manipulation like in a 3D Engine
---

# Free-Form Scene Editor: Enabling Multi-Round Object Manipulation like in a 3D Engine
**arXiv**：[2511.13713v1](https://arxiv.org/abs/2511.13713) · [PDF](https://arxiv.org/pdf/2511.13713.pdf)  
**作者**：Xincheng Shuai, Zhenyuan Qin, Henghui Ding, Dacheng Tao  

**一句话要点**：提出FFSE框架以支持真实图像上的多轮3D感知对象编辑

**关键词**：3D感知编辑, 自回归框架, 多轮操作, 物理一致性, 真实图像编辑

## 3 点简述
- 现有文本到图像方法在3D感知对象编辑上不足，难以保持物理一致性
- FFSE采用自回归框架建模3D变换序列，支持平移、缩放和旋转等操作
- 实验显示FFSE在单轮和多轮3D编辑场景中显著优于现有方法

## 摘要（原文）

> Recent advances in text-to-image (T2I) diffusion models have significantly improved semantic image editing, yet most methods fall short in performing 3D-aware object manipulation. In this work, we present FFSE, a 3D-aware autoregressive framework designed to enable intuitive, physically-consistent object editing directly on real-world images. Unlike previous approaches that either operate in image space or require slow and error-prone 3D reconstruction, FFSE models editing as a sequence of learned 3D transformations, allowing users to perform arbitrary manipulations, such as translation, scaling, and rotation, while preserving realistic background effects (e.g., shadows, reflections) and maintaining global scene consistency across multiple editing rounds. To support learning of multi-round 3D-aware object manipulation, we introduce 3DObjectEditor, a hybrid dataset constructed from simulated editing sequences across diverse objects and scenes, enabling effective training under multi-round and dynamic conditions. Extensive experiments show that the proposed FFSE significantly outperforms existing methods in both single-round and multi-round 3D-aware editing scenarios.

