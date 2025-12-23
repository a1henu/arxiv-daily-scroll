---
layout: default
title: D2Pruner: Debiased Importance and Structural Diversity for MLLM Token Pruning
---

# D2Pruner: Debiased Importance and Structural Diversity for MLLM Token Pruning
**arXiv**：[2512.19443v1](https://arxiv.org/abs/2512.19443) · [PDF](https://arxiv.org/pdf/2512.19443.pdf)  
**作者**：Evelyn Zhang, Fufu Yu, Aoqi Wu, Zichen Wen, Ke Yan, Shouhong Ding, Biqing Qi, Linfeng Zhang  

**一句话要点**：提出D2Pruner框架，结合去偏重要性和结构多样性以解决MLLM细粒度定位任务中的令牌剪枝失败问题。

**关键词**：多模态大语言模型, 令牌剪枝, 细粒度定位, 去偏重要性, 结构多样性, 计算效率

## 3 点简述
- 核心问题：现有令牌剪枝方法在MLLM细粒度定位任务中表现不佳，重要性方法存在位置偏差，多样性方法忽视用户提示和空间冗余。
- 方法要点：D2Pruner通过去偏注意力分数选择核心令牌作为支点，并在混合图上使用最大独立集选择补充令牌，确保重要性和多样性。
- 实验或效果：在LLaVA-1.5-7B上减少74.2% FLOPs并保持99.2%性能，在InternVL-2.5-8B定位任务中90%令牌减少率下保持85.7%性能，提升达63.53%。

## 摘要（原文）

> Processing long visual token sequences poses a significant computational burden on Multimodal Large Language Models (MLLMs). While token pruning offers a path to acceleration, we find that current methods, while adequate for general understanding, catastrophically fail on fine-grained localization tasks. We attribute this failure to the inherent flaws of the two prevailing strategies: importance-based methods suffer from a strong positional bias, an inherent model artifact that distracts from semantic content, while diversity-based methods exhibit structural blindness, disregarding the user's prompt and spatial redundancy. To address this, we introduce D2Pruner, a framework that rectifies these issues by uniquely combining debiased importance with a structural pruning mechanism. Our method first secures a core set of the most critical tokens as pivots based on a debiased attention score. It then performs a Maximal Independent Set (MIS) selection on the remaining tokens, which are modeled on a hybrid graph where edges signify spatial proximity and semantic similarity. This process iteratively preserves the most important and available token while removing its neighbors, ensuring that the supplementary tokens are chosen to maximize importance and diversity. Extensive experiments demonstrate that D2Pruner has exceptional efficiency and fidelity. Applied to LLaVA-1.5-7B for general understanding tasks, it reduces FLOPs by 74.2\% while retaining 99.2\% of its original performance. Furthermore, in challenging localization benchmarks with InternVL-2.5-8B, it maintains 85.7\% performance at a 90\% token reduction rate, marking a significant advancement with up to 63. 53\% improvement over existing methods.

