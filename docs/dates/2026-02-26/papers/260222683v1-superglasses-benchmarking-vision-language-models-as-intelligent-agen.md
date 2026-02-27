---
layout: default
title: SUPERGLASSES: Benchmarking Vision Language Models as Intelligent Agents for AI Smart Glasses
---

# SUPERGLASSES: Benchmarking Vision Language Models as Intelligent Agents for AI Smart Glasses
**arXiv**：[2602.22683v1](https://arxiv.org/abs/2602.22683) · [PDF](https://arxiv.org/pdf/2602.22683.pdf)  
**作者**：Zhuohang Jiang, Xu Yuan, Haohao Qu, Shanru Lin, Kanglong Liu, Wenqi Fan, Qing Li  

**一句话要点**：提出SUPERGLASSES基准和SUPERLENS智能体，以解决智能眼镜场景中视觉语言模型评估与性能不足的问题。

**关键词**：智能眼镜视觉问答, 多模态基准, 检索增强生成, 对象检测, 查询解耦, 多模态网络搜索

## 3 点简述
- 现有智能眼镜视觉语言模型评估数据集缺乏真实性和多样性，无法反映实际使用场景。
- 引入基于真实智能眼镜数据的SUPERGLASSES基准，包含2422个图像-问题对，覆盖14个图像域和8个查询类别。
- 提出SUPERLENS智能体，集成对象检测、查询解耦和多模态网络搜索，在基准上超越GPT-4o 2.19%。

## 摘要（原文）

> The rapid advancement of AI-powered smart glasses, one of the hottest wearable devices, has unlocked new frontiers for multimodal interaction, with Visual Question Answering (VQA) over external knowledge sources emerging as a core application. Existing Vision Language Models (VLMs) adapted to smart glasses are typically trained and evaluated on traditional multimodal datasets; however, these datasets lack the variety and realism needed to reflect smart glasses usage scenarios and diverge from their specific challenges, where accurately identifying the object of interest must precede any external knowledge retrieval. To bridge this gap, we introduce SUPERGLASSES, the first comprehensive VQA benchmark built on real-world data entirely collected by smart glasses devices. SUPERGLASSES comprises 2,422 egocentric image-question pairs spanning 14 image domains and 8 query categories, enriched with full search trajectories and reasoning annotations. We evaluate 26 representative VLMs on this benchmark, revealing significant performance gaps. To address the limitations of existing models, we further propose SUPERLENS, a multimodal smart glasses agent that enables retrieval-augmented answer generation by integrating automatic object detection, query decoupling, and multimodal web search. Our agent achieves state-of-the-art performance, surpassing GPT-4o by 2.19 percent, and highlights the need for task-specific solutions in smart glasses VQA scenarios.

