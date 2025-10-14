---
layout: default
title: G2L:From Giga-Scale to Cancer-Specific Large-Scale Pathology Foundation Models via Knowledge Distillation
---

# G2L:From Giga-Scale to Cancer-Specific Large-Scale Pathology Foundation Models via Knowledge Distillation
**arXiv**：[2510.11176v1](https://arxiv.org/abs/2510.11176) · [PDF](https://arxiv.org/pdf/2510.11176.pdf)  
**作者**：Yesung Cho, Sungmin Lee, Geongyu Lee, Minkyung Lee, Jongbae Park, Dongmyung Shin  

**一句话要点**：提出G2L框架通过知识蒸馏提升病理大模型性能，降低计算成本

**关键词**：病理基础模型, 知识蒸馏, 癌症特异性, 计算效率, 模型压缩

## 3 点简述
- 核心问题：千亿级病理基础模型计算成本高，难以实用部署
- 方法要点：用少量目标癌症数据蒸馏，将千亿模型能力转移至大型模型
- 实验或效果：蒸馏模型在多项基准中超越同规模模型，部分超越千亿模型

## 摘要（原文）

> Recent studies in pathology foundation models have shown that scaling
> training data, diversifying cancer types, and increasing model size
> consistently improve their performance. However, giga-scale foundation models,
> which are trained on hundreds of thousands of slides covering tens of cancer
> types and contain billions of parameters, pose significant challenges for
> practical use due to their tremendous computational costs in both development
> and deployment. In this work, we present a novel strategy, named the G2L
> framework, to increase the performance of large-scale foundation models, which
> consist of only $15\%$ of the parameters of giga-scale models, to a comparable
> performance level of giga-scale models in cancer-specific tasks. Our approach
> applies knowledge distillation, transferring the capabilities of a giga-scale
> model to a large-scale model, using just 1K pathology slides of a target cancer
> (e.g., breast, prostate, etc.). The resulting distilled model not only
> outperformed state-of-the-art models of the same size (i.e., large-scale)
> across several benchmarks but also, interestingly, surpassed the giga-scale
> teacher and huge-scale models in some benchmarks. In addition, the distilled
> model exhibited a higher robustness index, indicating improved resilience to
> image variations originating from multiple institutions. These findings suggest
> that the proposed distillation approach for a large-scale model is a data- and
> parameter-efficient way to achieve giga-scale-level performance for
> cancer-specific applications without prohibitive computational burden.

