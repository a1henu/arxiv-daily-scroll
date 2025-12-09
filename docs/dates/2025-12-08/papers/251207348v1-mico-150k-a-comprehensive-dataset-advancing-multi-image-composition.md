---
layout: default
title: MICo-150K: A Comprehensive Dataset Advancing Multi-Image Composition
---

# MICo-150K: A Comprehensive Dataset Advancing Multi-Image Composition
**arXiv**：[2512.07348v1](https://arxiv.org/abs/2512.07348) · [PDF](https://arxiv.org/pdf/2512.07348.pdf)  
**作者**：Xinyu Wei, Kangrui Cen, Hongyang Wei, Zhen Guo, Bairui Li, Zeqing Wang, Jinrui Zhang, Lei Zhang  

**一句话要点**：提出MICo-150K数据集以解决多图像组合中高质量训练数据缺乏的问题

**关键词**：多图像组合, 可控图像生成, 数据集构建, 身份一致性, 基准测试, 模型微调

## 3 点简述
- 核心问题：多图像组合任务因缺乏高质量数据而受限，阻碍可控图像生成发展
- 方法要点：构建包含7类任务的大规模数据集，通过合成与人工过滤确保身份一致性
- 实验或效果：微调模型在基准测试中提升性能，基线模型支持任意多图像输入

## 摘要（原文）

> In controllable image generation, synthesizing coherent and consistent images from multiple reference inputs, i.e., Multi-Image Composition (MICo), remains a challenging problem, partly hindered by the lack of high-quality training data. To bridge this gap, we conduct a systematic study of MICo, categorizing it into 7 representative tasks and curate a large-scale collection of high-quality source images and construct diverse MICo prompts. Leveraging powerful proprietary models, we synthesize a rich amount of balanced composite images, followed by human-in-the-loop filtering and refinement, resulting in MICo-150K, a comprehensive dataset for MICo with identity consistency. We further build a Decomposition-and-Recomposition (De&Re) subset, where 11K real-world complex images are decomposed into components and recomposed, enabling both real and synthetic compositions. To enable comprehensive evaluation, we construct MICo-Bench with 100 cases per task and 300 challenging De&Re cases, and further introduce a new metric, Weighted-Ref-VIEScore, specifically tailored for MICo evaluation. Finally, we fine-tune multiple models on MICo-150K and evaluate them on MICo-Bench. The results show that MICo-150K effectively equips models without MICo capability and further enhances those with existing skills. Notably, our baseline model, Qwen-MICo, fine-tuned from Qwen-Image-Edit, matches Qwen-Image-2509 in 3-image composition while supporting arbitrary multi-image inputs beyond the latter's limitation. Our dataset, benchmark, and baseline collectively offer valuable resources for further research on Multi-Image Composition.

