---
layout: default
title: FlowDC: Flow-Based Decoupling-Decay for Complex Image Editing
---

# FlowDC: Flow-Based Decoupling-Decay for Complex Image Editing
**arXiv**：[2512.11395v1](https://arxiv.org/abs/2512.11395) · [PDF](https://arxiv.org/pdf/2512.11395.pdf)  
**作者**：Yilei Jiang, Zhen Wang, Yanghao Wang, Jun Yu, Yueting Zhuang, Jun Xiao, Long Chen  

**一句话要点**：提出FlowDC方法，通过解耦-衰减机制解决复杂图像编辑中的语义对齐与源一致性平衡问题。

**关键词**：复杂图像编辑, 流匹配模型, 解耦编辑, 源一致性, 文本到图像编辑, 基准构建

## 3 点简述
- 核心问题：现有复杂图像编辑方法在单轮和多轮编辑中面临长文本跟随和累积不一致性挑战，难以平衡语义对齐与源一致性。
- 方法要点：将复杂编辑解耦为多个子编辑效果，并行叠加；分解速度并衰减正交部分以提升源结构保持。
- 实验或效果：构建Complex-PIE-Bench基准，FlowDC在多个基准上优于现有方法，并通过消融实验验证模块设计。

## 摘要（原文）

> With the surge of pre-trained text-to-image flow matching models, text-based image editing performance has gained remarkable improvement, especially for \underline{simple editing} that only contains a single editing target. To satisfy the exploding editing requirements, the \underline{complex editing} which contains multiple editing targets has posed as a more challenging task. However, current complex editing solutions: single-round and multi-round editing are limited by long text following and cumulative inconsistency, respectively. Thus, they struggle to strike a balance between semantic alignment and source consistency. In this paper, we propose \textbf{FlowDC}, which decouples the complex editing into multiple sub-editing effects and superposes them in parallel during the editing process. Meanwhile, we observed that the velocity quantity that is orthogonal to the editing displacement harms the source structure preserving. Thus, we decompose the velocity and decay the orthogonal part for better source consistency. To evaluate the effectiveness of complex editing settings, we construct a complex editing benchmark: Complex-PIE-Bench. On two benchmarks, FlowDC shows superior results compared with existing methods. We also detail the ablations of our module designs.

