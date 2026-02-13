---
layout: default
title: SToRM: Supervised Token Reduction for Multi-modal LLMs toward efficient end-to-end autonomous driving
---

# SToRM: Supervised Token Reduction for Multi-modal LLMs toward efficient end-to-end autonomous driving
**arXiv**：[2602.11656v1](https://arxiv.org/abs/2602.11656) · [PDF](https://arxiv.org/pdf/2602.11656.pdf)  
**作者**：Seo Hyun Kim, Jin Bok Park, Do Yeon Koo, Ho Gun Park, Il Yong Chun  

**一句话要点**：提出SToRM框架以解决多模态大语言模型在端到端自动驾驶中计算效率低的问题

**关键词**：多模态大语言模型, 令牌减少, 端到端自动驾驶, 监督训练, 计算效率优化

## 3 点简述
- 核心问题：多模态大语言模型在自动驾驶中因视觉令牌过多导致计算资源需求高，影响效率。
- 方法要点：通过轻量级重要性预测器、监督训练和锚点-上下文合并模块，减少令牌冗余。
- 实验或效果：在LangAuto基准上，SToRM在相同令牌预算下优于现有方法，计算成本降低高达30倍。

## 摘要（原文）

> In autonomous driving, end-to-end (E2E) driving systems that predict control commands directly from sensor data have achieved significant advancements. For safe driving in unexpected scenarios, these systems may additionally rely on human interventions such as natural language instructions. Using a multi-modal large language model (MLLM) facilitates human-vehicle interaction and can improve performance in such scenarios. However, this approach requires substantial computational resources due to its reliance on an LLM and numerous visual tokens from sensor inputs, which are limited in autonomous vehicles. Many MLLM studies have explored reducing visual tokens, but often suffer end-task performance degradation compared to using all tokens.
>   To enable efficient E2E driving while maintaining performance comparable to using all tokens, this paper proposes the first Supervised Token Reduction framework for multi-modal LLMs (SToRM). The proposed framework consists of three key elements. First, a lightweight importance predictor with short-term sliding windows estimates token importance scores. Second, a supervised training approach uses an auxiliary path to obtain pseudo-supervision signals from an all-token LLM pass. Third, an anchor-context merging module partitions tokens into anchors and context tokens, and merges context tokens into relevant anchors to reduce redundancy while minimizing information loss. Experiments on the LangAuto benchmark show that SToRM outperforms state-of-the-art E2E driving MLLMs under the same reduced-token budget, maintaining all-token performance while reducing computational cost by up to 30x.

