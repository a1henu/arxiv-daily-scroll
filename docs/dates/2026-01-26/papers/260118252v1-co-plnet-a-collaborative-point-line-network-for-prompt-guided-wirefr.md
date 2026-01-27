---
layout: default
title: Co-PLNet: A Collaborative Point-Line Network for Prompt-Guided Wireframe Parsing
---

# Co-PLNet: A Collaborative Point-Line Network for Prompt-Guided Wireframe Parsing
**arXiv**：[2601.18252v1](https://arxiv.org/abs/2601.18252) · [PDF](https://arxiv.org/pdf/2601.18252.pdf)  
**作者**：Chao Wang, Xuanying Li, Cheng Dai, Jinglei Feng, Yuxiang Luo, Yuqi Ouyang, Hao Qin  

**一句话要点**：提出Co-PLNet协作点线网络，通过点线提示编码与交叉引导解码解决线框解析中的不匹配问题。

**关键词**：线框解析, 点线协作, 空间提示编码, 交叉引导解码, 结构化几何感知

## 3 点简述
- 核心问题：现有方法分离预测线与交点，导致后处理不匹配和鲁棒性降低。
- 方法要点：使用点线提示编码器将早期检测转换为空间提示，交叉引导线解码器通过稀疏注意力细化预测。
- 实验效果：在Wireframe和YorkUrban数据集上提升准确性和鲁棒性，并实现实时效率。

## 摘要（原文）

> Wireframe parsing aims to recover line segments and their junctions to form a structured geometric representation useful for downstream tasks such as Simultaneous Localization and Mapping (SLAM). Existing methods predict lines and junctions separately and reconcile them post-hoc, causing mismatches and reduced robustness. We present Co-PLNet, a point-line collaborative framework that exchanges spatial cues between the two tasks, where early detections are converted into spatial prompts via a Point-Line Prompt Encoder (PLP-Encoder), which encodes geometric attributes into compact and spatially aligned maps. A Cross-Guidance Line Decoder (CGL-Decoder) then refines predictions with sparse attention conditioned on complementary prompts, enforcing point-line consistency and efficiency. Experiments on Wireframe and YorkUrban show consistent improvements in accuracy and robustness, together with favorable real-time efficiency, demonstrating our effectiveness for structured geometry perception.

