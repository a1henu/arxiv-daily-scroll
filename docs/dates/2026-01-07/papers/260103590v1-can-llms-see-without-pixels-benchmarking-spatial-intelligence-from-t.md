---
layout: default
title: Can LLMs See Without Pixels? Benchmarking Spatial Intelligence from Textual Descriptions
---

# Can LLMs See Without Pixels? Benchmarking Spatial Intelligence from Textual Descriptions
**arXiv**：[2601.03590v1](https://arxiv.org/abs/2601.03590) · [PDF](https://arxiv.org/pdf/2601.03590.pdf)  
**作者**：Zhongbin Guo, Zhen Yang, Yushan Li, Xinyue Zhang, Wenyu Gao, Jiacheng Wang, Chengzhi Li, Xiangrui Liu, Ping Jian  

**一句话要点**：提出SiT-Bench基准以评估无像素输入下大语言模型的空间智能表现

**关键词**：空间智能基准, 文本推理评估, 大语言模型, 坐标感知描述, 世界建模潜力

## 3 点简述
- 核心问题：探究空间智能源于视觉编码器还是推理主干，需无像素评估
- 方法要点：构建坐标感知文本描述数据集，涵盖多类空间推理任务
- 实验或效果：SOTA模型在局部语义任务表现佳，但全局一致性存在空间差距

## 摘要（原文）

> Recent advancements in Spatial Intelligence (SI) have predominantly relied on Vision-Language Models (VLMs), yet a critical question remains: does spatial understanding originate from visual encoders or the fundamental reasoning backbone? Inspired by this question, we introduce SiT-Bench, a novel benchmark designed to evaluate the SI performance of Large Language Models (LLMs) without pixel-level input, comprises over 3,800 expert-annotated items across five primary categories and 17 subtasks, ranging from egocentric navigation and perspective transformation to fine-grained robotic manipulation. By converting single/multi-view scenes into high-fidelity, coordinate-aware textual descriptions, we challenge LLMs to perform symbolic textual reasoning rather than visual pattern matching. Evaluation results of state-of-the-art (SOTA) LLMs reveals that while models achieve proficiency in localized semantic tasks, a significant "spatial gap" remains in global consistency. Notably, we find that explicit spatial reasoning significantly boosts performance, suggesting that LLMs possess latent world-modeling potential. Our proposed dataset SiT-Bench serves as a foundational resource to foster the development of spatially-grounded LLM backbones for future VLMs and embodied agents. Our code and benchmark will be released at https://github.com/binisalegend/SiT-Bench .

