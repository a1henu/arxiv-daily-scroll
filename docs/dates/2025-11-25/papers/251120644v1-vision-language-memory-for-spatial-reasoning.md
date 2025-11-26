---
layout: default
title: Vision-Language Memory for Spatial Reasoning
---

# Vision-Language Memory for Spatial Reasoning
**arXiv**：[2511.20644v1](https://arxiv.org/abs/2511.20644) · [PDF](https://arxiv.org/pdf/2511.20644.pdf)  
**作者**：Zuntao Liu, Yi Du, Taimeng Fu, Shaoshu Su, Cherie Ho, Chen Wang  

**一句话要点**：提出VLM^2模型以解决视频空间推理中的语义几何错位和记忆缺失问题

**关键词**：空间推理, 视觉语言模型, 持久记忆, 双记忆模块, 视频理解, 3D表示

## 3 点简述
- 核心问题：语义几何错位和缺乏持久记忆阻碍视频空间推理达到人类水平
- 方法要点：引入双记忆模块，包括工作记忆和情景记忆，实现固定计算成本的长时推理
- 实验或效果：在多个基准测试中，VLM^2在纯视频模型中达到最先进性能

## 摘要（原文）

> Spatial reasoning is a critical capability for intelligent robots, yet current vision-language models (VLMs) still fall short of human-level performance in video-based spatial reasoning. This gap mainly stems from two challenges: a semantic-geometric misalignment that prevents consistent 3D understanding, and the absence of persistent memory to retain 3D representation and understanding over time. To address these limitations, we present VLM$^2$, a Vision-Language Model with persistent Memory for spatial reasoning with a view-consistent, 3D-aware representation purely from 2D video. Specifically, to enhance long-horizon reasoning, we incorporate a dual-memory module, consisting of a working memory that operates as a sliding window to focus on immediate context, and an episodic memory that consolidates and stores critical long-term information. This design enables efficient and long-horizon spatial reasoning with a fixed computational cost. Extensive experiments on multiple benchmarks show that VLM$^2$ achieves state-of-the-art performance among video-only models, significantly advancing the frontier of visual-spatial intelligence.

