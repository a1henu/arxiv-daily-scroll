---
layout: default
title: Kiwi-Edit: Versatile Video Editing via Instruction and Reference Guidance
---

# Kiwi-Edit: Versatile Video Editing via Instruction and Reference Guidance
**arXiv**：[2603.02175v1](https://arxiv.org/abs/2603.02175) · [PDF](https://arxiv.org/pdf/2603.02175.pdf)  
**作者**：Yiqi Lin, Guoqiang Liang, Ziyun Zeng, Zechen Bai, Yanzhe Chen, Mike Zheng Shou  

**一句话要点**：提出Kiwi-Edit架构与RefVIE数据集，通过指令与参考引导实现可控视频编辑。

**关键词**：视频编辑, 指令引导, 参考引导, 数据集构建, 可控生成, 多阶段训练

## 3 点简述
- 核心问题：基于指令的视频编辑方法因自然语言描述视觉细节有限而难以精确控制，且参考引导方法缺乏高质量配对训练数据。
- 方法要点：构建可扩展数据生成管道，将现有视频编辑对转化为高质量训练四元组，并设计统一架构结合可学习查询和潜在视觉特征进行参考语义引导。
- 实验或效果：通过渐进多阶段训练，模型在指令遵循和参考保真度上显著提升，在可控视频编辑中达到新最优性能。

## 摘要（原文）

> Instruction-based video editing has witnessed rapid progress, yet current methods often struggle with precise visual control, as natural language is inherently limited in describing complex visual nuances. Although reference-guided editing offers a robust solution, its potential is currently bottlenecked by the scarcity of high-quality paired training data. To bridge this gap, we introduce a scalable data generation pipeline that transforms existing video editing pairs into high-fidelity training quadruplets, leveraging image generative models to create synthesized reference scaffolds. Using this pipeline, we construct RefVIE, a large-scale dataset tailored for instruction-reference-following tasks, and establish RefVIE-Bench for comprehensive evaluation. Furthermore, we propose a unified editing architecture, Kiwi-Edit, that synergizes learnable queries and latent visual features for reference semantic guidance. Our model achieves significant gains in instruction following and reference fidelity via a progressive multi-stage training curriculum. Extensive experiments demonstrate that our data and architecture establish a new state-of-the-art in controllable video editing. All datasets, models, and code is released at https://github.com/showlab/Kiwi-Edit.

