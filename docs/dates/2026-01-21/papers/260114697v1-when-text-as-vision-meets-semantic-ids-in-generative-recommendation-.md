---
layout: default
title: When Text-as-Vision Meets Semantic IDs in Generative Recommendation: An Empirical Study
---

# When Text-as-Vision Meets Semantic IDs in Generative Recommendation: An Empirical Study
**arXiv**：[2601.14697v1](https://arxiv.org/abs/2601.14697) · [PDF](https://arxiv.org/pdf/2601.14697.pdf)  
**作者**：Shutong Qiao, Wei Yuan, Tong Chen, Xiangyu Zhao, Quoc Viet Hung Nguyen, Hongzhi Yin  

**一句话要点**：提出OCR文本表示以提升生成推荐中语义ID学习的鲁棒性与跨模态融合效果

**关键词**：生成推荐, 语义ID学习, OCR文本表示, 跨模态融合, 鲁棒性, 推荐系统

## 3 点简述
- 核心问题：标准文本编码器在推荐数据中处理符号化描述时语义破碎，且跨模态时文本与图像嵌入结构不匹配
- 方法要点：将文本渲染为图像，使用基于视觉的OCR模型编码，作为语义ID学习的新表示
- 实验或效果：在四个数据集和两个生成骨干上，OCR文本表示在单模态和多模态设置中均优于或匹配标准文本嵌入，且对空间分辨率压缩鲁棒

## 摘要（原文）

> Semantic ID learning is a key interface in Generative Recommendation (GR) models, mapping items to discrete identifiers grounded in side information, most commonly via a pretrained text encoder. However, these text encoders are primarily optimized for well-formed natural language. In real-world recommendation data, item descriptions are often symbolic and attribute-centric, containing numerals, units, and abbreviations. These text encoders can break these signals into fragmented tokens, weakening semantic coherence and distorting relationships among attributes. Worse still, when moving to multimodal GR, relying on standard text encoders introduces an additional obstacle: text and image embeddings often exhibit mismatched geometric structures, making cross-modal fusion less effective and less stable.
>   In this paper, we revisit representation design for Semantic ID learning by treating text as a visual signal. We conduct a systematic empirical study of OCR-based text representations, obtained by rendering item descriptions into images and encoding them with vision-based OCR models. Experiments across four datasets and two generative backbones show that OCR-text consistently matches or surpasses standard text embeddings for Semantic ID learning in both unimodal and multimodal settings. Furthermore, we find that OCR-based Semantic IDs remain robust under extreme spatial-resolution compression, indicating strong robustness and efficiency in practical deployments.

