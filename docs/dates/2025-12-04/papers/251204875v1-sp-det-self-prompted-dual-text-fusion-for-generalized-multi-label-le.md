---
layout: default
title: SP-Det: Self-Prompted Dual-Text Fusion for Generalized Multi-Label Lesion Detection
---

# SP-Det: Self-Prompted Dual-Text Fusion for Generalized Multi-Label Lesion Detection
**arXiv**：[2512.04875v1](https://arxiv.org/abs/2512.04875) · [PDF](https://arxiv.org/pdf/2512.04875.pdf)  
**作者**：Qing Xu, Yanqian Wang, Xiangjian Hea, Yue Li, Yixuan Zhang, Rong Qu, Wenting Duan, Zhen Chen  

**一句话要点**：提出SP-Det自提示检测框架，自动生成文本提示以解决胸部X光多标签病灶检测依赖专家标注的问题。

**关键词**：病灶检测, 自提示学习, 多标签分类, 胸部X光分析, 文本提示生成, 特征增强

## 3 点简述
- 核心问题：现有可提示检测方法依赖人工标注作为提示，耗时且不适用于临床。
- 方法要点：引入无专家双文本提示生成器，结合语义上下文和疾病信标提示，并设计双向特征增强器融合诊断上下文。
- 实验或效果：在两个胸部X光数据集上超越先进方法，完全消除对专家标注提示的依赖。

## 摘要（原文）

> Automated lesion detection in chest X-rays has demonstrated significant potential for improving clinical diagnosis by precisely localizing pathological abnormalities. While recent promptable detection frameworks have achieved remarkable accuracy in target localization, existing methods typically rely on manual annotations as prompts, which are labor-intensive and impractical for clinical applications. To address this limitation, we propose SP-Det, a novel self-prompted detection framework that automatically generates rich textual context to guide multi-label lesion detection without requiring expert annotations. Specifically, we introduce an expert-free dual-text prompt generator (DTPG) that leverages two complementary textual modalities: semantic context prompts that capture global pathological patterns and disease beacon prompts that focus on disease-specific manifestations. Moreover, we devise a bidirectional feature enhancer (BFE) that synergistically integrates comprehensive diagnostic context with disease-specific embeddings to significantly improve feature representation and detection accuracy. Extensive experiments on two chest X-ray datasets with diverse thoracic disease categories demonstrate that our SP-Det framework outperforms state-of-the-art detection methods while completely eliminating the dependency on expert-annotated prompts compared to existing promptable architectures.

