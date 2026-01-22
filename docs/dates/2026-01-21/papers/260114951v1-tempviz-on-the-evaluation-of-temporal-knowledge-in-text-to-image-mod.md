---
layout: default
title: TempViz: On the Evaluation of Temporal Knowledge in Text-to-Image Models
---

# TempViz: On the Evaluation of Temporal Knowledge in Text-to-Image Models
**arXiv**：[2601.14951v1](https://arxiv.org/abs/2601.14951) · [PDF](https://arxiv.org/pdf/2601.14951.pdf)  
**作者**：Carolin Holtermann, Nina Krebs, Anne Lauscher  

**一句话要点**：提出TempViz数据集以评估文本到图像模型中的时间知识能力。

**关键词**：文本到图像模型, 时间知识评估, 数据集构建, 人类评估, 自动评估方法

## 3 点简述
- 核心问题：时间知识在文本到图像模型中的评估研究稀缺，影响生成图像的上下文准确性。
- 方法要点：构建首个全面评估时间知识的数据集，包含7.9k提示和600+参考图像，覆盖五个时间知识类别。
- 实验或效果：人类评估显示模型时间能力普遍较弱，准确率未超75%，自动评估方法不可靠，需未来研究。

## 摘要（原文）

> Time alters the visual appearance of entities in our world, like objects, places, and animals. Thus, for accurately generating contextually-relevant images, knowledge and reasoning about time can be crucial (e.g., for generating a landscape in spring vs. in winter). Yet, although substantial work exists on understanding and improving temporal knowledge in natural language processing, research on how temporal phenomena appear and are handled in text-to-image (T2I) models remains scarce. We address this gap with TempViz, the first data set to holistically evaluate temporal knowledge in image generation, consisting of 7.9k prompts and more than 600 reference images. Using TempViz, we study the capabilities of five T2I models across five temporal knowledge categories. Human evaluation shows that temporal competence is generally weak, with no model exceeding 75% accuracy across categories. Towards larger-scale studies, we also examine automated evaluation methods, comparing several established approaches against human judgments. However, none of these approaches provides a reliable assessment of temporal cues - further indicating the pressing need for future research on temporal knowledge in T2I.

