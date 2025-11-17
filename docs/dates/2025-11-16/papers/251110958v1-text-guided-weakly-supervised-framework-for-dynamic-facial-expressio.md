---
layout: default
title: Text-guided Weakly Supervised Framework for Dynamic Facial Expression Recognition
---

# Text-guided Weakly Supervised Framework for Dynamic Facial Expression Recognition
**arXiv**：[2511.10958v1](https://arxiv.org/abs/2511.10958) · [PDF](https://arxiv.org/pdf/2511.10958.pdf)  
**作者**：Gunho Jung, Heejo Kong, Seong-Whan Lee  

**一句话要点**：提出文本引导弱监督框架TG-DFER以解决动态面部表情识别中的视觉多样性和时序复杂性

**关键词**：动态面部表情识别, 弱监督学习, 多实例学习, 视觉语言模型, 时序建模, 情感识别

## 3 点简述
- 核心问题：动态面部表情识别存在多对一标注问题，视频帧与单一情感标签不匹配。
- 方法要点：集成视觉语言预训练模型，通过文本描述提供语义指导，增强多实例学习。
- 实验或效果：在弱监督下，TG-DFER提高了泛化性、可解释性和时序敏感性。

## 摘要（原文）

> Dynamic facial expression recognition (DFER) aims to identify emotional states by modeling the temporal changes in facial movements across video sequences. A key challenge in DFER is the many-to-one labeling problem, where a video composed of numerous frames is assigned a single emotion label. A common strategy to mitigate this issue is to formulate DFER as a Multiple Instance Learning (MIL) problem. However, MIL-based approaches inherently suffer from the visual diversity of emotional expressions and the complexity of temporal dynamics. To address this challenge, we propose TG-DFER, a text-guided weakly supervised framework that enhances MIL-based DFER by incorporating semantic guidance and coherent temporal modeling. We incorporate a vision-language pre-trained (VLP) model is integrated to provide semantic guidance through fine-grained textual descriptions of emotional context. Furthermore, we introduce visual prompts, which align enriched textual emotion labels with visual instance features, enabling fine-grained reasoning and frame-level relevance estimation. In addition, a multi-grained temporal network is designed to jointly capture short-term facial dynamics and long-range emotional flow, ensuring coherent affective understanding across time. Extensive results demonstrate that TG-DFER achieves improved generalization, interpretability, and temporal sensitivity under weak supervision.

