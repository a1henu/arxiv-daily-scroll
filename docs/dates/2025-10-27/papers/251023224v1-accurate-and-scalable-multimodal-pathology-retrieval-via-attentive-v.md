---
layout: default
title: Accurate and Scalable Multimodal Pathology Retrieval via Attentive Vision-Language Alignment
---

# Accurate and Scalable Multimodal Pathology Retrieval via Attentive Vision-Language Alignment
**arXiv**：[2510.23224v1](https://arxiv.org/abs/2510.23224) · [PDF](https://arxiv.org/pdf/2510.23224.pdf)  
**作者**：Hongyi Wang, Zhengjie Zhu, Jiabo Ma, Fang Wang, Yue Shi, Bo Luo, Jili Wang, Qiuyu Cai, Xiuming Zhang, Yen-Wei Chen, Lanfen Lin, Hao Chen  

**一句话要点**：提出PathSearch框架以解决数字病理学中全切片图像检索的挑战

**关键词**：数字病理学, 图像检索, 视觉-语言对齐, 注意力机制, 对比学习, 多模态检索

## 3 点简述
- 核心问题：全切片图像规模巨大且语义差异细微，导致检索困难。
- 方法要点：结合细粒度注意力马赛克表示和全局嵌入，通过视觉-语言对比学习对齐。
- 实验或效果：在多个数据集上验证，提升检索准确性、诊断信心和观察者间一致性。

## 摘要（原文）

> The rapid digitization of histopathology slides has opened up new
> possibilities for computational tools in clinical and research workflows. Among
> these, content-based slide retrieval stands out, enabling pathologists to
> identify morphologically and semantically similar cases, thereby supporting
> precise diagnoses, enhancing consistency across observers, and assisting
> example-based education. However, effective retrieval of whole slide images
> (WSIs) remains challenging due to their gigapixel scale and the difficulty of
> capturing subtle semantic differences amid abundant irrelevant content. To
> overcome these challenges, we present PathSearch, a retrieval framework that
> unifies fine-grained attentive mosaic representations with global-wise slide
> embeddings aligned through vision-language contrastive learning. Trained on a
> corpus of 6,926 slide-report pairs, PathSearch captures both fine-grained
> morphological cues and high-level semantic patterns to enable accurate and
> flexible retrieval. The framework supports two key functionalities: (1)
> mosaic-based image-to-image retrieval, ensuring accurate and efficient slide
> research; and (2) multi-modal retrieval, where text queries can directly
> retrieve relevant slides. PathSearch was rigorously evaluated on four public
> pathology datasets and three in-house cohorts, covering tasks including
> anatomical site retrieval, tumor subtyping, tumor vs. non-tumor discrimination,
> and grading across diverse organs such as breast, lung, kidney, liver, and
> stomach. External results show that PathSearch outperforms traditional
> image-to-image retrieval frameworks. A multi-center reader study further
> demonstrates that PathSearch improves diagnostic accuracy, boosts confidence,
> and enhances inter-observer agreement among pathologists in real clinical
> scenarios. These results establish PathSearch as a scalable and generalizable
> retrieval solution for digital pathology.

