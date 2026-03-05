---
layout: default
title: Order Is Not Layout: Order-to-Space Bias in Image Generation
---

# Order Is Not Layout: Order-to-Space Bias in Image Generation
**arXiv**：[2603.03714v1](https://arxiv.org/abs/2603.03714) · [PDF](https://arxiv.org/pdf/2603.03714.pdf)  
**作者**：Yongkang Zhang, Zonglin Zhao, Yuechen Zhang, Fei Ding, Pei Li, Wenxuan Wang  

**一句话要点**：提出Order-to-Space Bias以揭示图像生成模型中的顺序-空间偏差问题

**关键词**：图像生成, 顺序-空间偏差, 文本到图像, 布局形成, 数据驱动偏差, 模型评估

## 3 点简述
- 核心问题：现代图像生成模型存在顺序-空间偏差，实体提及顺序错误决定空间布局和角色绑定
- 方法要点：引入OTS-Bench量化偏差，通过配对提示隔离顺序效应，评估同质化和正确性
- 实验或效果：偏差广泛存在，源于数据驱动，早期干预和微调可有效减少偏差并保持生成质量

## 摘要（原文）

> We study a systematic bias in modern image generation models: the mention order of entities in text spuriously determines spatial layout and entity--role binding. We term this phenomenon Order-to-Space Bias (OTS) and show that it arises in both text-to-image and image-to-image generation, often overriding grounded cues and causing incorrect layouts or swapped assignments. To quantify OTS, we introduce OTS-Bench, which isolates order effects with paired prompts differing only in entity order and evaluates models along two dimensions: homogenization and correctness. Experiments show that Order-to-Space Bias (OTS) is widespread in modern image generation models, and provide evidence that it is primarily data-driven and manifests during the early stages of layout formation. Motivated by this insight, we show that both targeted fine-tuning and early-stage intervention strategies can substantially reduce OTS, while preserving generation quality.

