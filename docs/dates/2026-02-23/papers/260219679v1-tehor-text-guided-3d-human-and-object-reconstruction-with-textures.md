---
layout: default
title: TeHOR: Text-Guided 3D Human and Object Reconstruction with Textures
---

# TeHOR: Text-Guided 3D Human and Object Reconstruction with Textures
**arXiv**：[2602.19679v1](https://arxiv.org/abs/2602.19679) · [PDF](https://arxiv.org/pdf/2602.19679.pdf)  
**作者**：Hyeongjin Nam, Daniel Sungho Jung, Kyoung Mu Lee  

**一句话要点**：提出TeHOR框架，利用文本描述和外观线索实现单图像中3D人与物体的联合重建，解决非接触交互和全局上下文缺失问题。

**关键词**：3D重建, 人机交互, 文本引导, 语义对齐, 外观建模, 单图像重建

## 3 点简述
- 核心问题：现有方法依赖物理接触信息，无法处理非接触交互，且忽视外观提供的全局上下文。
- 方法要点：引入文本描述进行语义对齐，并整合外观线索以捕获整体交互信息。
- 实验或效果：实现准确且语义一致的重建，达到先进性能，适用于机器人学和数字内容创建。

## 摘要（原文）

> Joint reconstruction of 3D human and object from a single image is an active research area, with pivotal applications in robotics and digital content creation. Despite recent advances, existing approaches suffer from two fundamental limitations. First, their reconstructions rely heavily on physical contact information, which inherently cannot capture non-contact human-object interactions, such as gazing at or pointing toward an object. Second, the reconstruction process is primarily driven by local geometric proximity, neglecting the human and object appearances that provide global context crucial for understanding holistic interactions. To address these issues, we introduce TeHOR, a framework built upon two core designs. First, beyond contact information, our framework leverages text descriptions of human-object interactions to enforce semantic alignment between the 3D reconstruction and its textual cues, enabling reasoning over a wider spectrum of interactions, including non-contact cases. Second, we incorporate appearance cues of the 3D human and object into the alignment process to capture holistic contextual information, thereby ensuring visually plausible reconstructions. As a result, our framework produces accurate and semantically coherent reconstructions, achieving state-of-the-art performance.

