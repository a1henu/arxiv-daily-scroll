---
layout: default
title: MSAM: Multi-Semantic Adaptive Mining for Cross-Modal Drone Video-Text Retrieval
---

# MSAM: Multi-Semantic Adaptive Mining for Cross-Modal Drone Video-Text Retrieval
**arXiv**：[2510.15470v1](https://arxiv.org/abs/2510.15470) · [PDF](https://arxiv.org/pdf/2510.15470.pdf)  
**作者**：Jinghao Huang, Yaxiong Chen, Ganchao Liu  

**一句话要点**：提出多语义自适应挖掘方法以解决无人机视频-文本检索中的语义建模挑战

**关键词**：无人机视频检索, 跨模态学习, 多语义挖掘, 自适应机制, 特征融合

## 3 点简述
- 核心问题：无人机视频具有俯视视角、结构同质性和目标组合多样性，现有跨模态方法难以有效建模。
- 方法要点：引入多语义自适应学习机制，通过动态帧间变化和区域语义提取增强视频内容理解。
- 实验或效果：在自建数据集上实验表明，MSAM优于现有方法，提升了检索性能。

## 摘要（原文）

> With the advancement of drone technology, the volume of video data increases
> rapidly, creating an urgent need for efficient semantic retrieval. We are the
> first to systematically propose and study the drone video-text retrieval (DVTR)
> task. Drone videos feature overhead perspectives, strong structural
> homogeneity, and diverse semantic expressions of target combinations, which
> challenge existing cross-modal methods designed for ground-level views in
> effectively modeling their characteristics. Therefore, dedicated retrieval
> mechanisms tailored for drone scenarios are necessary. To address this issue,
> we propose a novel approach called Multi-Semantic Adaptive Mining (MSAM). MSAM
> introduces a multi-semantic adaptive learning mechanism, which incorporates
> dynamic changes between frames and extracts rich semantic information from
> specific scene regions, thereby enhancing the deep understanding and reasoning
> of drone video content. This method relies on fine-grained interactions between
> words and drone video frames, integrating an adaptive semantic construction
> module, a distribution-driven semantic learning term and a diversity semantic
> term to deepen the interaction between text and drone video modalities and
> improve the robustness of feature representation. To reduce the interference of
> complex backgrounds in drone videos, we introduce a cross-modal interactive
> feature fusion pooling mechanism that focuses on feature extraction and
> matching in target regions, minimizing noise effects. Extensive experiments on
> two self-constructed drone video-text datasets show that MSAM outperforms other
> existing methods in the drone video-text retrieval task. The source code and
> dataset will be made publicly available.

