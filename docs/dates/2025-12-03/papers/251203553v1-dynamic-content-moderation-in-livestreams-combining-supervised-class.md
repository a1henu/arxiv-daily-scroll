---
layout: default
title: Dynamic Content Moderation in Livestreams: Combining Supervised Classification with MLLM-Boosted Similarity Matching
---

# Dynamic Content Moderation in Livestreams: Combining Supervised Classification with MLLM-Boosted Similarity Matching
**arXiv**：[2512.03553v1](https://arxiv.org/abs/2512.03553) · [PDF](https://arxiv.org/pdf/2512.03553.pdf)  
**作者**：Wei Chee Yew, Hailun Xu, Sanjay Saha, Xiaotian Fan, Hiok Hian Ong, David Yuchen Wang, Kanchan Sarkar, Zhenheng Yang, Danhui Guan  

**一句话要点**：提出结合监督分类与MLLM增强相似性匹配的混合框架，以解决直播中动态内容审核的挑战。

**关键词**：直播内容审核, 混合框架, 多模态大语言模型, 相似性匹配, 监督分类, 生产部署

## 3 点简述
- 核心问题：直播内容审核需及时、多模态且能应对新型违规内容。
- 方法要点：混合框架结合监督分类与相似性匹配，MLLM蒸馏知识提升准确性。
- 实验或效果：生产部署中，分类管道召回率67%精度80%，相似性管道召回率76%精度80%，A/B测试减少6-8%不良内容观看。

## 摘要（原文）

> Content moderation remains a critical yet challenging task for large-scale user-generated video platforms, especially in livestreaming environments where moderation must be timely, multimodal, and robust to evolving forms of unwanted content. We present a hybrid moderation framework deployed at production scale that combines supervised classification for known violations with reference-based similarity matching for novel or subtle cases. This hybrid design enables robust detection of both explicit violations and novel edge cases that evade traditional classifiers. Multimodal inputs (text, audio, visual) are processed through both pipelines, with a multimodal large language model (MLLM) distilling knowledge into each to boost accuracy while keeping inference lightweight. In production, the classification pipeline achieves 67% recall at 80% precision, and the similarity pipeline achieves 76% recall at 80% precision. Large-scale A/B tests show a 6-8% reduction in user views of unwanted livestreams}. These results demonstrate a scalable and adaptable approach to multimodal content governance, capable of addressing both explicit violations and emerging adversarial behaviors.

