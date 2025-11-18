---
layout: default
title: Text2Traffic: A Text-to-Image Generation and Editing Method for Traffic Scenes
---

# Text2Traffic: A Text-to-Image Generation and Editing Method for Traffic Scenes
**arXiv**：[2511.12932v1](https://arxiv.org/abs/2511.12932) · [PDF](https://arxiv.org/pdf/2511.12932.pdf)  
**作者**：Feng Lv, Haoxuan Feng, Zilu Zhang, Chunlong Xia, Yanfeng Li  

**一句话要点**：提出Text2Traffic框架，通过可控掩码机制和多视角数据增强交通场景图像生成与编辑

**关键词**：文本驱动图像生成, 交通场景编辑, 可控掩码机制, 多视角数据增强, 两阶段训练, 掩码加权损失

## 3 点简述
- 核心问题：交通场景生成中语义丰富度不足、视角受限、视觉保真度低和文本-图像对齐差
- 方法要点：采用两阶段训练和掩码区域加权损失，提升小元素生成质量和文本对齐
- 实验或效果：在交通场景文本驱动图像生成和编辑中实现领先性能

## 摘要（原文）

> With the rapid advancement of intelligent transportation systems, text-driven image generation and editing techniques have demonstrated significant potential in providing rich, controllable visual scene data for applications such as traffic monitoring and autonomous driving. However, several challenges remain, including insufficient semantic richness of generated traffic elements, limited camera viewpoints, low visual fidelity of synthesized images, and poor alignment between textual descriptions and generated content. To address these issues, we propose a unified text-driven framework for both image generation and editing, leveraging a controllable mask mechanism to seamlessly integrate the two tasks. Furthermore, we incorporate both vehicle-side and roadside multi-view data to enhance the geometric diversity of traffic scenes. Our training strategy follows a two-stage paradigm: first, we perform conceptual learning using large-scale coarse-grained text-image data; then, we fine-tune with fine-grained descriptive data to enhance text-image alignment and detail quality. Additionally, we introduce a mask-region-weighted loss that dynamically emphasizes small yet critical regions during training, thereby substantially enhancing the generation fidelity of small-scale traffic elements. Extensive experiments demonstrate that our method achieves leading performance in text-based image generation and editing within traffic scenes.

