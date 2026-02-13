---
layout: default
title: DeepGen 1.0: A Lightweight Unified Multimodal Model for Advancing Image Generation and Editing
---

# DeepGen 1.0: A Lightweight Unified Multimodal Model for Advancing Image Generation and Editing
**arXiv**：[2602.12205v1](https://arxiv.org/abs/2602.12205) · [PDF](https://arxiv.org/pdf/2602.12205.pdf)  
**作者**：Dianyi Wang, Ruihang Li, Feng Han, Chaofan Ma, Wei Song, Siyuan Wang, Yibin Wang, Yi Xin, Hongjian Liu, Zhixiong Zhang, Shengyuan Ding, Tianhang Wang, Zhenglin Cheng, Tao Lin, Cheng Jin, Kaicheng Yu, Jingjing Chen, Wenjie Wang, Zhongyu Wei, Jiaqi Wang  

**一句话要点**：提出DeepGen 1.0轻量统一多模态模型，通过SCB框架和三阶段训练策略，在图像生成与编辑任务中实现高效高性能。

**关键词**：轻量多模态模型, 图像生成与编辑, 深度对齐框架, 三阶段训练, 强化学习优化, 开源模型

## 3 点简述
- 核心问题：现有统一多模态模型参数量大（>10B），训练和部署成本高，轻量模型在语义理解和细粒度控制上受限。
- 方法要点：引入Stacked Channel Bridging（SCB）深度对齐框架，提取VLM层次特征并与可学习'think tokens'融合，提供结构化推理指导；采用三阶段数据中心训练策略，包括对齐预训练、联合监督微调和强化学习。
- 实验或效果：模型参数量5B，仅训练约50M样本，在WISE和UniREditBench等基准上超越更大模型，如超越80B HunyuanImage 28%和27B Qwen-Image-Edit 37%。

## 摘要（原文）

> Current unified multimodal models for image generation and editing typically rely on massive parameter scales (e.g., >10B), entailing prohibitive training costs and deployment footprints. In this work, we present DeepGen 1.0, a lightweight 5B unified model that achieves comprehensive capabilities competitive with or surpassing much larger counterparts. To overcome the limitations of compact models in semantic understanding and fine-grained control, we introduce Stacked Channel Bridging (SCB), a deep alignment framework that extracts hierarchical features from multiple VLM layers and fuses them with learnable 'think tokens' to provide the generative backbone with structured, reasoning-rich guidance. We further design a data-centric training strategy spanning three progressive stages: (1) Alignment Pre-training on large-scale image-text pairs and editing triplets to synchronize VLM and DiT representations, (2) Joint Supervised Fine-tuning on a high-quality mixture of generation, editing, and reasoning tasks to foster omni-capabilities, and (3) Reinforcement Learning with MR-GRPO, which leverages a mixture of reward functions and supervision signals, resulting in substantial gains in generation quality and alignment with human preferences, while maintaining stable training progress and avoiding visual artifacts. Despite being trained on only ~50M samples, DeepGen 1.0 achieves leading performance across diverse benchmarks, surpassing the 80B HunyuanImage by 28% on WISE and the 27B Qwen-Image-Edit by 37% on UniREditBench. By open-sourcing our training code, weights, and datasets, we provide an efficient, high-performance alternative to democratize unified multimodal research.

