---
layout: default
title: Multi-Grained Text-Guided Image Fusion for Multi-Exposure and Multi-Focus Scenarios
---

# Multi-Grained Text-Guided Image Fusion for Multi-Exposure and Multi-Focus Scenarios
**arXiv**：[2512.20556v1](https://arxiv.org/abs/2512.20556) · [PDF](https://arxiv.org/pdf/2512.20556.pdf)  
**作者**：Mingwei Tang, Jiahao Nie, Guang Yang, Ziqing Cui, Jie Li  

**一句话要点**：提出多粒度文本引导图像融合方法，以解决多曝光和多焦点场景下的融合挑战。

**关键词**：图像融合, 多粒度文本引导, 跨模态对齐, 多曝光融合, 多焦点融合

## 3 点简述
- 核心问题：现有方法使用粗粒度文本描述，难以处理输入图像间的动态范围和焦点深度差异，影响融合质量。
- 方法要点：引入多粒度文本描述，通过分层跨模态调制模块和监督信号，增强视觉与文本特征的对齐。
- 实验或效果：在多项实验中，该方法在多曝光和多焦点图像融合任务上优于先前方法。

## 摘要（原文）

> Image fusion aims to synthesize a single high-quality image from a pair of inputs captured under challenging conditions, such as differing exposure levels or focal depths. A core challenge lies in effectively handling disparities in dynamic range and focus depth between the inputs. With the advent of vision-language models, recent methods incorporate textual descriptions as auxiliary guidance to enhance fusion quality. However, simply incorporating coarse-grained descriptions hampers the understanding of fine-grained details and poses challenges for precise cross-modal alignment. To address these limitations, we propose Multi-grained Text-guided Image Fusion (MTIF), a novel fusion paradigm with three key designs. First, it introduces multi-grained textual descriptions that separately capture fine details, structural cues, and semantic content, guiding image fusion through a hierarchical cross-modal modulation module. Second, it involves supervision signals at each granularity to facilitate alignment between visual and textual features and enhance the utility of auxiliary text. Third, it adopts a saliency-driven enrichment module to augment training data with dense semantic content, further strengthening the cross-modal modulation and alignment. Extensive experiments show that MTIF consistently outperforms previous methods on both multi-exposure and multi-focus image fusion tasks.

