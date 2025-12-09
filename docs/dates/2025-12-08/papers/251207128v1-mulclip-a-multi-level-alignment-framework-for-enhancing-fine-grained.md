---
layout: default
title: MulCLIP: A Multi-level Alignment Framework for Enhancing Fine-grained Long-context CLIP
---

# MulCLIP: A Multi-level Alignment Framework for Enhancing Fine-grained Long-context CLIP
**arXiv**：[2512.07128v1](https://arxiv.org/abs/2512.07128) · [PDF](https://arxiv.org/pdf/2512.07128.pdf)  
**作者**：Chau Truong, Hieu Ta Quang, Dung D. Le  

**一句话要点**：提出MulCLIP多级对齐框架以增强细粒度长上下文CLIP能力

**关键词**：视觉语言模型, 长文本对齐, 细粒度理解, 多级对齐, CLIP增强

## 3 点简述
- CLIP模型在长文本描述上表现不佳，因训练数据为简短标题
- MulCLIP通过全局对比对齐、局部特征重建和子标题聚合补丁对齐实现多级对齐
- 实验显示MulCLIP在多个基准上提升性能，优于区域提议方法

## 摘要（原文）

> Vision-language models like CLIP show impressive ability to align images and text, but their training on short, concise captions makes them struggle with lengthy, detailed descriptions. Recent advances mitigate this challenge by leveraging region-proposal information to map visual regions with corresponding sentences from lengthy captions, yet incurring notable deployment costs. We introduce MulCLIP, a novel end-to-end multi-level alignment framework that bridges natural long-text structures with image components. MulCLIP first preserves global contrastive alignment between images and both summary and long captions, while extending positional embeddings for longer text sequences. To further enhance fine-grained understanding, we propose two novel strategies: (1) a token reconstruction alignment over locally calibrated features to strengthen semantic connections between words and image patches, and (2) a subcaption-aggregated patch alignment that automatically extracts and aggregates context-rich patches for each subcaption. Experimental results across diverse benchmarks demonstrate our method consistently improves downstream performance, while ablation studies confirm its multi-scale alignment is the key factor driving better fine-grained capability than region-proposal-assisted approaches, making it particularly suitable for diverse real-world applications.

