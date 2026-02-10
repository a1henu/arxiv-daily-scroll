---
layout: default
title: OneVision-Encoder: Codec-Aligned Sparsity as a Foundational Principle for Multimodal Intelligence
---

# OneVision-Encoder: Codec-Aligned Sparsity as a Foundational Principle for Multimodal Intelligence
**arXiv**：[2602.08683v1](https://arxiv.org/abs/2602.08683) · [PDF](https://arxiv.org/pdf/2602.08683.pdf)  
**作者**：Feilong Tang, Xiang An, Yunyao Yan, Yin Xie, Bin Qin, Kaicheng Yang, Yifei Shen, Yuanhan Zhang, Chunyuan Li, Shikun Feng, Changrui Chen, Huajie Tan, Ming Hu, Manyuan Zhang, Bo Li, Ziyong Feng, Ziwei Liu, Zongyuan Ge, Jiankang Deng  

**一句话要点**：提出OneVision-Encoder，通过编解码器对齐的稀疏性提升多模态智能效率与准确性。

**关键词**：视频理解, 稀疏编码, 编解码器对齐, 多模态智能, 3D RoPE, 语义压缩

## 3 点简述
- 核心问题：当前视觉架构处理密集像素网格，浪费计算在冗余背景而非关键信息上。
- 方法要点：采用编解码器补丁化，聚焦信号熵丰富的区域，结合共享3D RoPE统一时空推理。
- 实验或效果：在16个基准测试中超越Qwen3-ViT等模型，视频任务平均提升4.1%，使用更少视觉令牌。

## 摘要（原文）

> Hypothesis. Artificial general intelligence is, at its core, a compression problem. Effective compression demands resonance: deep learning scales best when its architecture aligns with the fundamental structure of the data. These are the fundamental principles. Yet, modern vision architectures have strayed from these truths: visual signals are highly redundant, while discriminative information, the surprise, is sparse. Current models process dense pixel grids uniformly, wasting vast compute on static background rather than focusing on the predictive residuals that define motion and meaning. We argue that to solve visual understanding, we must align our architectures with the information-theoretic principles of video, i.e., Codecs.
>   Method. OneVision-Encoder encodes video by compressing predictive visual structure into semantic meaning. By adopting Codec Patchification, OV-Encoder abandons uniform computation to focus exclusively on the 3.1%-25% of regions rich in signal entropy. To unify spatial and temporal reasoning under irregular token layouts, OneVision-Encoder employs a shared 3D RoPE and is trained with a large-scale cluster discrimination objective over more than one million semantic concepts, jointly capturing object permanence and motion dynamics.
>   Evidence. The results validate our core hypothesis: efficiency and accuracy are not a trade-off; they are positively correlated. When integrated into LLM, it consistently outperforms strong vision backbones such as Qwen3-ViT and SigLIP2 across 16 image, video, and document understanding benchmarks, despite using substantially fewer visual tokens and pretraining data. Notably, on video understanding tasks, OV-Encoder achieves an average improvement of 4.1% over Qwen3-ViT. Codec-aligned, patch-level sparsity is a foundational principle, enabling OV-Encoder as a scalable engine for next-generation visual generalists.

