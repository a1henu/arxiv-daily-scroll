---
layout: default
title: Multi-Perspective Subimage CLIP with Keyword Guidance for Remote Sensing Image-Text Retrieval
---

# Multi-Perspective Subimage CLIP with Keyword Guidance for Remote Sensing Image-Text Retrieval
**arXiv**：[2601.18190v1](https://arxiv.org/abs/2601.18190) · [PDF](https://arxiv.org/pdf/2601.18190.pdf)  
**作者**：Yifan Li, Shiying Wang, Jianqiang Huang  

**一句话要点**：提出MPS-CLIP框架，通过关键词引导多视角子图像对齐解决遥感图像-文本检索中的细粒度语义匹配问题。

**关键词**：遥感图像-文本检索, 多视角对齐, 参数高效微调, 关键词引导, 细粒度语义匹配, 对比学习

## 3 点简述
- 现有方法依赖粗粒度全局对齐，忽略遥感图像密集多尺度语义，且全微调计算成本高。
- 利用LLM提取关键词引导SamGeo生成语义相关子视角，引入G^2A适配器和MPR模块高效聚合局部线索。
- 在RSICD和RSITMD基准上达到最优性能，mR分别为35.18%和48.40%，显著优于基线。

## 摘要（原文）

> Vision-Language Pre-training (VLP) models like CLIP have significantly advanced Remote Sensing Image-Text Retrieval (RSITR). However, existing methods predominantly rely on coarse-grained global alignment, which often overlooks the dense, multi-scale semantics inherent in overhead imagery. Moreover, adapting these heavy models via full fine-tuning incurs prohibitive computational costs and risks catastrophic forgetting. To address these challenges, we propose MPS-CLIP, a parameter-efficient framework designed to shift the retrieval paradigm from global matching to keyword-guided fine-grained alignment. Specifically, we leverage a Large Language Model (LLM) to extract core semantic keywords, guiding the Segment Anything Model (SamGeo) to generate semantically relevant sub-perspectives. To efficiently adapt the frozen backbone, we introduce a Gated Global Attention (G^2A) adapter, which captures global context and long-range dependencies with minimal overhead. Furthermore, a Multi-Perspective Representation (MPR) module aggregates these local cues into robust multi-perspective embeddings. The framework is optimized via a hybrid objective combining multi-perspective contrastive and weighted triplet losses, which dynamically selects maximum-response perspectives to suppress noise and enforce precise semantic matching. Extensive experiments on the RSICD and RSITMD benchmarks demonstrate that MPS-CLIP achieves state-of-the-art performance with 35.18% and 48.40% mean Recall (mR), respectively, significantly outperforming full fine-tuning baselines and recent competitive methods. Code is available at https://github.com/Lcrucial1f/MPS-CLIP.

