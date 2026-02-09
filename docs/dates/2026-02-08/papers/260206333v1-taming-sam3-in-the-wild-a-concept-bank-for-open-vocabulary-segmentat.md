---
layout: default
title: Taming SAM3 in the Wild: A Concept Bank for Open-Vocabulary Segmentation
---

# Taming SAM3 in the Wild: A Concept Bank for Open-Vocabulary Segmentation
**arXiv**：[2602.06333v1](https://arxiv.org/abs/2602.06333) · [PDF](https://arxiv.org/pdf/2602.06333.pdf)  
**作者**：Gensheng Pei, Xiruo Jiang, Yazhou Yao, Xiangbo Shu, Fumin Shen, Byeungwoo Jeon  

**一句话要点**：提出ConceptBank校准框架，以解决SAM3在开放词汇分割中因数据漂移和概念漂移导致的性能下降问题。

**关键词**：开放词汇分割, 概念漂移校准, 视觉原型, 数据漂移抑制, 参数无关框架

## 3 点简述
- 核心问题：SAM3依赖预定义概念，在目标域数据漂移或概念漂移时视觉证据与提示对齐失效。
- 方法要点：构建数据集特定概念库，通过视觉原型锚定证据、抑制异常值并融合候选概念来校准对齐。
- 实验或效果：在自然场景和遥感场景中有效适应分布漂移，提升开放词汇分割的鲁棒性和效率。

## 摘要（原文）

> The recent introduction of \texttt{SAM3} has revolutionized Open-Vocabulary Segmentation (OVS) through \textit{promptable concept segmentation}, which grounds pixel predictions in flexible concept prompts. However, this reliance on pre-defined concepts makes the model vulnerable: when visual distributions shift (\textit{data drift}) or conditional label distributions evolve (\textit{concept drift}) in the target domain, the alignment between visual evidence and prompts breaks down. In this work, we present \textsc{ConceptBank}, a parameter-free calibration framework to restore this alignment on the fly. Instead of adhering to static prompts, we construct a dataset-specific concept bank from the target statistics. Our approach (\textit{i}) anchors target-domain evidence via class-wise visual prototypes, (\textit{ii}) mines representative supports to suppress outliers under data drift, and (\textit{iii}) fuses candidate concepts to rectify concept drift. We demonstrate that \textsc{ConceptBank} effectively adapts \texttt{SAM3} to distribution drifts, including challenging natural-scene and remote-sensing scenarios, establishing a new baseline for robustness and efficiency in OVS. Code and model are available at https://github.com/pgsmall/ConceptBank.

