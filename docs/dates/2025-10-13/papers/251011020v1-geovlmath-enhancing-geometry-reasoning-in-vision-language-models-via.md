---
layout: default
title: GeoVLMath: Enhancing Geometry Reasoning in Vision-Language Models via Cross-Modal Reward for Auxiliary Line Creation
---

# GeoVLMath: Enhancing Geometry Reasoning in Vision-Language Models via Cross-Modal Reward for Auxiliary Line Creation
**arXiv**：[2510.11020v1](https://arxiv.org/abs/2510.11020) · [PDF](https://arxiv.org/pdf/2510.11020.pdf)  
**作者**：Shasha Guo, Liang Pang, Xi Wang, Yanling Wang, Huawei Shen, Jing Zhang  

**一句话要点**：提出GeoVLMath以通过跨模态奖励增强视觉语言模型在几何辅助线推理中的性能

**关键词**：几何推理, 视觉语言模型, 强化学习, 跨模态对齐, 辅助线生成, 数据集构建

## 3 点简述
- 核心问题：大型视觉语言模型在几何问题中绘制辅助线时面临几何精度不足的挑战
- 方法要点：使用强化学习框架和跨模态奖励来优化辅助线文本描述与图表的对齐
- 实验或效果：在3B和7B规模上，GeoVLMath在辅助线推理基准上表现优于开源和专有模型

## 摘要（原文）

> Auxiliary lines are essential for solving complex geometric problems but
> remain challenging for large vision-language models (LVLMs). Rather than
> editing diagrams to draw auxiliary lines, which current image editing models
> struggle to render with geometric precision, we generate textual descriptions
> of auxiliary-line constructions to better align with the representational
> strengths of LVLMs. To bridge the gap between textual descriptions and spatial
> structure, we propose a reinforcement learning framework that enhances
> diagram-text alignment. At the core of our approach is a cross-modal reward
> that evaluates how well the generated auxiliary-line description for an
> original diagram matches a ground-truth auxiliary-line diagram. Built on this
> reward, we present GeoVLMath, an open-source LVLM tailored to auxiliary-line
> reasoning in solid geometry. This fine-grained signal drives a GRPO-based RL
> stage, yielding precise diagram-text alignment. To support training, we develop
> a scalable data creation pipeline and construct AuxSolidMath, a dataset of
> 3,018 real-exam geometry problems with paired diagrams and aligned textual
> fields. At the 3B and 7B scales, GeoVLMath achieves competitive and often
> superior performance compared with strong open-source and proprietary LVLMs on
> auxiliary-line reasoning benchmarks.

