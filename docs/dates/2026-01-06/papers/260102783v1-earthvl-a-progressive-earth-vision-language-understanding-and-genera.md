---
layout: default
title: EarthVL: A Progressive Earth Vision-Language Understanding and Generation Framework
---

# EarthVL: A Progressive Earth Vision-Language Understanding and Generation Framework
**arXiv**：[2601.02783v1](https://arxiv.org/abs/2601.02783) · [PDF](https://arxiv.org/pdf/2601.02783.pdf)  
**作者**：Junjue Wang, Yanfei Zhong, Zihang Chen, Zhuo Zheng, Ailong Ma, Liangpei Zhang  

**一句话要点**：提出EarthVL框架以解决地球视觉中对象关系推理不足的问题，聚焦城市规划应用。

**关键词**：地球视觉语言理解, 对象关系推理, 语义分割, 视觉问答, 城市规划, 遥感图像

## 3 点简述
- 核心问题：地球视觉在对象识别方面成熟，但缺乏对象关系推理，限制场景理解。
- 方法要点：构建EarthVLSet数据集和EarthVLNet网络，通过语义分割引导渐进式视觉语言理解与生成。
- 实验或效果：在语义分割、选择题和开放式VQA基准上表现优越，验证了分割特征对VQA的增强作用。

## 摘要（原文）

> Earth vision has achieved milestones in geospatial object recognition but lacks exploration in object-relational reasoning, limiting comprehensive scene understanding. To address this, a progressive Earth vision-language understanding and generation framework is proposed, including a multi-task dataset (EarthVLSet) and a semantic-guided network (EarthVLNet). Focusing on city planning applications, EarthVLSet includes 10.9k sub-meter resolution remote sensing images, land-cover masks, and 761.5k textual pairs involving both multiple-choice and open-ended visual question answering (VQA) tasks. In an object-centric way, EarthVLNet is proposed to progressively achieve semantic segmentation, relational reasoning, and comprehensive understanding. The first stage involves land-cover segmentation to generate object semantics for VQA guidance. Guided by pixel-wise semantics, the object awareness based large language model (LLM) performs relational reasoning and knowledge summarization to generate the required answers. As for optimization, the numerical difference loss is proposed to dynamically add difference penalties, addressing the various objects' statistics. Three benchmarks, including semantic segmentation, multiple-choice, and open-ended VQA demonstrated the superiorities of EarthVLNet, yielding three future directions: 1) segmentation features consistently enhance VQA performance even in cross-dataset scenarios; 2) multiple-choice tasks show greater sensitivity to the vision encoder than to the language decoder; and 3) open-ended tasks necessitate advanced vision encoders and language decoders for an optimal performance. We believe this dataset and method will provide a beneficial benchmark that connects ''image-mask-text'', advancing geographical applications for Earth vision.

