---
layout: default
title: FunCineForge: A Unified Dataset Toolkit and Model for Zero-Shot Movie Dubbing in Diverse Cinematic Scenes
---

# FunCineForge: A Unified Dataset Toolkit and Model for Zero-Shot Movie Dubbing in Diverse Cinematic Scenes
**arXiv**：[2601.14777v1](https://arxiv.org/abs/2601.14777) · [PDF](https://arxiv.org/pdf/2601.14777.pdf)  
**作者**：Jiaxuan Liu, Yang Xiang, Han Zhao, Xiangang Li, Zhenhua Ling  

**一句话要点**：提出FunCineForge以解决电影配音中数据集不足和模型性能受限的问题

**关键词**：电影配音, 零样本学习, 多模态数据集, 唇部同步, 音色转换, MLLM模型

## 3 点简述
- 现有电影配音方法面临高质量多模态数据集规模小、标注稀疏和模型仅依赖唇部区域导致性能不佳的挑战
- FunCineForge包含大规模配音数据集生产流程和基于MLLM的配音模型，支持多样电影场景
- 实验在多种场景中显示模型在音频质量、唇部同步和音色转换上优于现有方法

## 摘要（原文）

> Movie dubbing is the task of synthesizing speech from scripts conditioned on video scenes, requiring accurate lip sync, faithful timbre transfer, and proper modeling of character identity and emotion. However, existing methods face two major limitations: (1) high-quality multimodal dubbing datasets are limited in scale, suffer from high word error rates, contain sparse annotations, rely on costly manual labeling, and are restricted to monologue scenes, all of which hinder effective model training; (2) existing dubbing models rely solely on the lip region to learn audio-visual alignment, which limits their applicability to complex live-action cinematic scenes, and exhibit suboptimal performance in lip sync, speech quality, and emotional expressiveness. To address these issues, we propose FunCineForge, which comprises an end-to-end production pipeline for large-scale dubbing datasets and an MLLM-based dubbing model designed for diverse cinematic scenes. Using the pipeline, we construct the first Chinese television dubbing dataset with rich annotations, and demonstrate the high quality of these data. Experiments across monologue, narration, dialogue, and multi-speaker scenes show that our dubbing model consistently outperforms SOTA methods in audio quality, lip sync, timbre transfer, and instruction following. Code and demos are available at https://anonymous.4open.science/w/FunCineForge.

