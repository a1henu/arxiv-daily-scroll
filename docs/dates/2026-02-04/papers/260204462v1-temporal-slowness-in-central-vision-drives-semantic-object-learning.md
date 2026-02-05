---
layout: default
title: Temporal Slowness in Central Vision Drives Semantic Object Learning
---

# Temporal Slowness in Central Vision Drives Semantic Object Learning
**arXiv**：[2602.04462v1](https://arxiv.org/abs/2602.04462) · [PDF](https://arxiv.org/pdf/2602.04462.pdf)  
**作者**：Timothy Schaumlöffel, Arthur Aubret, Gemma Roig, Jochen Triesch  

**一句话要点**：结合中央视觉与时间慢度学习，提升从人类视觉经验中学习语义对象表示的效果。

**关键词**：语义对象学习, 中央视觉, 时间慢度学习, 自监督学习, Ego4D数据集, 注视预测

## 3 点简述
- 研究人类如何从自我中心视觉流中无监督学习语义对象表示，关注中央视觉和时间慢度的作用。
- 模拟人类视觉经验，使用Ego4D数据集和注视预测模型提取中央视觉裁剪，训练时间对比自监督学习模型。
- 结果显示，中央视觉增强前景对象特征提取，时间慢度（尤其在注视眼动中）编码更广泛的语义信息。

## 摘要（原文）

> Humans acquire semantic object representations from egocentric visual streams with minimal supervision. Importantly, the visual system processes with high resolution only the center of its field of view and learns similar representations for visual inputs occurring close in time. This emphasizes slowly changing information around gaze locations. This study investigates the role of central vision and slowness learning in the formation of semantic object representations from human-like visual experience. We simulate five months of human-like visual experience using the Ego4D dataset and generate gaze coordinates with a state-of-the-art gaze prediction model. Using these predictions, we extract crops that mimic central vision and train a time-contrastive Self-Supervised Learning model on them. Our results show that combining temporal slowness and central vision improves the encoding of different semantic facets of object representations. Specifically, focusing on central vision strengthens the extraction of foreground object features, while considering temporal slowness, especially during fixational eye movements, allows the model to encode broader semantic information about objects. These findings provide new insights into the mechanisms by which humans may develop semantic object representations from natural visual experience.

