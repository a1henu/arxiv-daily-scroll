---
layout: default
title: Part-Aware Bottom-Up Group Reasoning for Fine-Grained Social Interaction Detection
---

# Part-Aware Bottom-Up Group Reasoning for Fine-Grained Social Interaction Detection
**arXiv**：[2511.03666v1](https://arxiv.org/abs/2511.03666) · [PDF](https://arxiv.org/pdf/2511.03666.pdf)  
**作者**：Dongkeun Kim, Minsu Cho, Suha Kwak  

**一句话要点**：提出基于身体部位感知的自底向上群体推理框架，以解决细粒度社交交互检测问题。

**关键词**：社交交互检测, 细粒度分析, 身体部位感知, 自底向上推理, 群体推断, 人际关联

## 3 点简述
- 现有方法依赖整体个体表示，忽略细微社交线索，导致群体推断模糊。
- 方法使用身体部位特征和人际关联，通过相似性推理推断社交群体和交互。
- 在NVI数据集上实验，性能优于先前方法，达到新最优水平。

## 摘要（原文）

> Social interactions often emerge from subtle, fine-grained cues such as
> facial expressions, gaze, and gestures. However, existing methods for social
> interaction detection overlook such nuanced cues and primarily rely on holistic
> representations of individuals. Moreover, they directly detect social groups
> without explicitly modeling the underlying interactions between individuals.
> These drawbacks limit their ability to capture localized social signals and
> introduce ambiguity when group configurations should be inferred from social
> interactions grounded in nuanced cues. In this work, we propose a part-aware
> bottom-up group reasoning framework for fine-grained social interaction
> detection. The proposed method infers social groups and their interactions
> using body part features and their interpersonal relations. Our model first
> detects individuals and enhances their features using part-aware cues, and then
> infers group configuration by associating individuals via similarity-based
> reasoning, which considers not only spatial relations but also subtle social
> cues that signal interactions, leading to more accurate group inference.
> Experiments on the NVI dataset demonstrate that our method outperforms prior
> methods, achieving the new state of the art.

