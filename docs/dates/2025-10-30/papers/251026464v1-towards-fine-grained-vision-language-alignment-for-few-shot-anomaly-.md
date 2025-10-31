---
layout: default
title: Towards Fine-Grained Vision-Language Alignment for Few-Shot Anomaly Detection
---

# Towards Fine-Grained Vision-Language Alignment for Few-Shot Anomaly Detection
**arXiv**：[2510.26464v1](https://arxiv.org/abs/2510.26464) · [PDF](https://arxiv.org/pdf/2510.26464.pdf)  
**作者**：Yuanting Fan, Jun Liu, Xiaochen Chen, Bin-Bin Gao, Jian Li, Yong Liu, Jinlong Peng, Chengjie Wang  

**一句话要点**：提出FineGrainedAD框架以解决少样本异常检测中的语义对齐问题

**关键词**：少样本异常检测, 视觉语言对齐, 多级语义描述, 异常定位, 可学习提示, 区域聚合

## 3 点简述
- 核心问题：现有方法因缺乏细粒度文本描述，导致图像描述与补丁级视觉异常语义不匹配。
- 方法要点：引入多级细粒度语义描述和可学习提示，通过区域聚合和多级对齐提升定位性能。
- 实验效果：在MVTec-AD和VisA数据集上，少样本设置下实现优越的整体性能。

## 摘要（原文）

> Few-shot anomaly detection (FSAD) methods identify anomalous regions with few
> known normal samples. Most existing methods rely on the generalization ability
> of pre-trained vision-language models (VLMs) to recognize potentially anomalous
> regions through feature similarity between text descriptions and images.
> However, due to the lack of detailed textual descriptions, these methods can
> only pre-define image-level descriptions to match each visual patch token to
> identify potential anomalous regions, which leads to the semantic misalignment
> between image descriptions and patch-level visual anomalies, achieving
> sub-optimal localization performance. To address the above issues, we propose
> the Multi-Level Fine-Grained Semantic Caption (MFSC) to provide multi-level and
> fine-grained textual descriptions for existing anomaly detection datasets with
> automatic construction pipeline. Based on the MFSC, we propose a novel
> framework named FineGrainedAD to improve anomaly localization performance,
> which consists of two components: Multi-Level Learnable Prompt (MLLP) and
> Multi-Level Semantic Alignment (MLSA). MLLP introduces fine-grained semantics
> into multi-level learnable prompts through automatic replacement and
> concatenation mechanism, while MLSA designs region aggregation strategy and
> multi-level alignment training to facilitate learnable prompts better align
> with corresponding visual regions. Experiments demonstrate that the proposed
> FineGrainedAD achieves superior overall performance in few-shot settings on
> MVTec-AD and VisA datasets.

