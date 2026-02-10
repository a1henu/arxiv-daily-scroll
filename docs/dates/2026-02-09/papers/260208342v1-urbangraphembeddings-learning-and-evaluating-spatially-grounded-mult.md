---
layout: default
title: UrbanGraphEmbeddings: Learning and Evaluating Spatially Grounded Multimodal Embeddings for Urban Science
---

# UrbanGraphEmbeddings: Learning and Evaluating Spatially Grounded Multimodal Embeddings for Urban Science
**arXiv**：[2602.08342v1](https://arxiv.org/abs/2602.08342) · [PDF](https://arxiv.org/pdf/2602.08342.pdf)  
**作者**：Jie Zhang, Xingtong Yu, Yuan Fang, Rudi Stouffs, Zdravko Trivic  

**一句话要点**：提出UrbanGraphEmbeddings以解决城市环境中多模态嵌入空间对齐不足的问题

**关键词**：城市科学, 多模态嵌入, 空间图学习, 街景图像, 对比学习, 基准评估

## 3 点简述
- 核心问题：城市理解依赖空间结构，但现有数据集缺乏街景图像与城市结构的显式对齐。
- 方法要点：引入UGData数据集和UGE两阶段训练策略，结合指令引导对比学习和图空间编码。
- 实验或效果：在多个VLM骨干上训练，图像检索和地理位置排名任务提升显著，验证空间接地的有效性。

## 摘要（原文）

> Learning transferable multimodal embeddings for urban environments is challenging because urban understanding is inherently spatial, yet existing datasets and benchmarks lack explicit alignment between street-view images and urban structure. We introduce UGData, a spatially grounded dataset that anchors street-view images to structured spatial graphs and provides graph-aligned supervision via spatial reasoning paths and spatial context captions, exposing distance, directionality, connectivity, and neighborhood context beyond image content. Building on UGData, we propose UGE, a two-stage training strategy that progressively and stably aligns images, text, and spatial structures by combining instruction-guided contrastive learning with graph-based spatial encoding. We finally introduce UGBench, a comprehensive benchmark to evaluate how spatially grounded embeddings support diverse urban understanding tasks -- including geolocation ranking, image retrieval, urban perception, and spatial grounding. We develop UGE on multiple state-of-the-art VLM backbones, including Qwen2-VL, Qwen2.5-VL, Phi-3-Vision, and LLaVA1.6-Mistral, and train fixed-dimensional spatial embeddings with LoRA tuning. UGE built upon Qwen2.5-VL-7B backbone achieves up to 44% improvement in image retrieval and 30% in geolocation ranking on training cities, and over 30% and 22% gains respectively on held-out cities, demonstrating the effectiveness of explicit spatial grounding for spatially intensive urban tasks.

