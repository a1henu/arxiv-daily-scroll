---
layout: default
title: Focus-LIME: Surgical Interpretation of Long-Context Large Language Models via Proxy-Based Neighborhood Selection
---

# Focus-LIME: Surgical Interpretation of Long-Context Large Language Models via Proxy-Based Neighborhood Selection
**arXiv**：[2602.04607v1](https://arxiv.org/abs/2602.04607) · [PDF](https://arxiv.org/pdf/2602.04607.pdf)  
**作者**：Junhao Liu, Haonan Yu, Zhenyu Yan, Xin Zhang  

**一句话要点**：提出Focus-LIME框架，通过代理模型优化扰动邻域，以解决长上下文大语言模型外科式解释的可行性问题。

**关键词**：长上下文大语言模型, 模型解释性, 局部解释方法, 代理模型, 扰动邻域选择, 外科式解释

## 3 点简述
- 核心问题：现有局部模型无关解释方法在长上下文场景中面临特征稀释，导致解释不忠实。
- 方法要点：采用粗到细框架，利用代理模型筛选扰动邻域，使目标模型在优化上下文中进行细粒度归因。
- 实验或效果：在长上下文基准测试中验证，使外科式解释可行并提供忠实解释。

## 摘要（原文）

> As Large Language Models (LLMs) scale to handle massive context windows, achieving surgical feature-level interpretation is essential for high-stakes tasks like legal auditing and code debugging. However, existing local model-agnostic explanation methods face a critical dilemma in these scenarios: feature-based methods suffer from attribution dilution due to high feature dimensionality, thus failing to provide faithful explanations. In this paper, we propose Focus-LIME, a coarse-to-fine framework designed to restore the tractability of surgical interpretation. Focus-LIME utilizes a proxy model to curate the perturbation neighborhood, allowing the target model to perform fine-grained attribution exclusively within the optimized context. Empirical evaluations on long-context benchmarks demonstrate that our method makes surgical explanations practicable and provides faithful explanations to users.

