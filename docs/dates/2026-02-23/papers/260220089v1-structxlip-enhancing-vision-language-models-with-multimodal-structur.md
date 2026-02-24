---
layout: default
title: StructXLIP: Enhancing Vision-language Models with Multimodal Structural Cues
---

# StructXLIP: Enhancing Vision-language Models with Multimodal Structural Cues
**arXiv**：[2602.20089v1](https://arxiv.org/abs/2602.20089) · [PDF](https://arxiv.org/pdf/2602.20089.pdf)  
**作者**：Zanxi Ruan, Qiuyu Kong, Songqun Gao, Yiming Wang, Marco Cristani  

**一句话要点**：提出StructXLIP，通过多模态结构线索增强视觉语言模型，提升跨模态检索性能。

**关键词**：视觉语言对齐, 跨模态检索, 结构线索, 边缘图, 微调范式, 多模态增强

## 3 点简述
- 核心问题：标准视觉语言对齐在长、细节丰富的描述上可能不足，需增强结构理解。
- 方法要点：提取图像边缘图作为结构代理，过滤文本强调结构线索，并引入三个结构中心损失进行微调。
- 实验或效果：在通用和专用领域的跨模态检索任务中超越现有方法，可作为即插即用增强方案。

## 摘要（原文）

> Edge-based representations are fundamental cues for visual understanding, a principle rooted in early vision research and still central today. We extend this principle to vision-language alignment, showing that isolating and aligning structural cues across modalities can greatly benefit fine-tuning on long, detail-rich captions, with a specific focus on improving cross-modal retrieval. We introduce StructXLIP, a fine-tuning alignment paradigm that extracts edge maps (e.g., Canny), treating them as proxies for the visual structure of an image, and filters the corresponding captions to emphasize structural cues, making them "structure-centric". Fine-tuning augments the standard alignment loss with three structure-centric losses: (i) aligning edge maps with structural text, (ii) matching local edge regions to textual chunks, and (iii) connecting edge maps to color images to prevent representation drift. From a theoretical standpoint, while standard CLIP maximizes the mutual information between visual and textual embeddings, StructXLIP additionally maximizes the mutual information between multimodal structural representations. This auxiliary optimization is intrinsically harder, guiding the model toward more robust and semantically stable minima, enhancing vision-language alignment. Beyond outperforming current competitors on cross-modal retrieval in both general and specialized domains, our method serves as a general boosting recipe that can be integrated into future approaches in a plug-and-play manner. Code and pretrained models are publicly available at: https://github.com/intelligolabs/StructXLIP.

