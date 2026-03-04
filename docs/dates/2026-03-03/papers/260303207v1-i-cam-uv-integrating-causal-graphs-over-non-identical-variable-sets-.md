---
layout: default
title: I-CAM-UV: Integrating Causal Graphs over Non-Identical Variable Sets Using Causal Additive Models with Unobserved Variables
---

# I-CAM-UV: Integrating Causal Graphs over Non-Identical Variable Sets Using Causal Additive Models with Unobserved Variables
**arXiv**：[2603.03207v1](https://arxiv.org/abs/2603.03207) · [PDF](https://arxiv.org/pdf/2603.03207.pdf)  
**作者**：Hirofumi Suzuki, Kentaro Kanamori, Takuya Takagi, Thong Pham, Takashi Nicholas Maeda, Shohei Shimizu  

**一句话要点**：提出I-CAM-UV方法，通过整合非相同变量集上的因果图以处理未观测变量问题

**关键词**：因果发现, 非相同变量集, 未观测变量, CAM-UV, 因果图整合

## 3 点简述
- 核心问题：多数据集因果发现中，变量集不一致和未观测变量限制因果关系识别
- 方法要点：利用CAM-UV提供未观测变量信息，通过枚举一致因果图整合结果
- 实验或效果：未知，但声称优于现有方法，并提供了高效组合搜索算法

## 摘要（原文）

> Causal discovery from observational data is a fundamental tool in various fields of science. While existing approaches are typically designed for a single dataset, we often need to handle multiple datasets with non-identical variable sets in practice. One straightforward approach is to estimate a causal graph from each dataset and construct a single causal graph by overlapping. However, this approach identifies limited causal relationships because unobserved variables in each dataset can be confounders, and some variable pairs may be unobserved in any dataset. To address this issue, we leverage Causal Additive Models with Unobserved Variables (CAM-UV) that provide causal graphs having information related to unobserved variables. We show that the ground truth causal graph has structural consistency with the information of CAM-UV on each dataset. As a result, we propose an approach named I-CAM-UV to integrate CAM-UV results by enumerating all consistent causal graphs. We also provide an efficient combinatorial search algorithm and demonstrate the usefulness of I-CAM-UV against existing methods.

