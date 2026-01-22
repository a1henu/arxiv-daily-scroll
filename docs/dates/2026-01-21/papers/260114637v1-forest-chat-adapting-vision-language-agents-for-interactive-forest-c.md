---
layout: default
title: Forest-Chat: Adapting Vision-Language Agents for Interactive Forest Change Analysis
---

# Forest-Chat: Adapting Vision-Language Agents for Interactive Forest Change Analysis
**arXiv**：[2601.14637v1](https://arxiv.org/abs/2601.14637) · [PDF](https://arxiv.org/pdf/2601.14637.pdf)  
**作者**：James Brock, Ce Zhang, Nantheera Anantrasirichai  

**一句话要点**：提出Forest-Chat，基于LLM驱动的智能体，用于交互式森林变化分析。

**关键词**：森林变化分析, 视觉语言模型, 零样本变化检测, 交互式界面, 遥感图像解释

## 3 点简述
- 核心问题：森林变化分析中像素级变化检测与语义解释的挑战，尤其在复杂森林动态下。
- 方法要点：结合多级变化解释视觉语言骨干与LLM编排，集成零样本变化检测和交互式点提示界面。
- 实验或效果：在Forest-Change和LEVIR-MCI-Trees数据集上表现优异，提升森林变化分析的可访问性和效率。

## 摘要（原文）

> The increasing availability of high-resolution satellite imagery, together with advances in deep learning, creates new opportunities for enhancing forest monitoring workflows. Two central challenges in this domain are pixel-level change detection and semantic change interpretation, particularly for complex forest dynamics. While large language models (LLMs) are increasingly adopted for data exploration, their integration with vision-language models (VLMs) for remote sensing image change interpretation (RSICI) remains underexplored, especially beyond urban environments. We introduce Forest-Chat, an LLM-driven agent designed for integrated forest change analysis. The proposed framework enables natural language querying and supports multiple RSICI tasks, including change detection, change captioning, object counting, deforestation percentage estimation, and change reasoning. Forest-Chat builds upon a multi-level change interpretation (MCI) vision-language backbone with LLM-based orchestration, and incorporates zero-shot change detection via a foundation change detection model together with an interactive point-prompt interface to support fine-grained user guidance. To facilitate adaptation and evaluation in forest environments, we introduce the Forest-Change dataset, comprising bi-temporal satellite imagery, pixel-level change masks, and multi-granularity semantic change captions generated through a combination of human annotation and rule-based methods. Experimental results demonstrate that Forest-Chat achieves strong performance on Forest-Change and on LEVIR-MCI-Trees, a tree-focused subset of LEVIR-MCI, for joint change detection and captioning, highlighting the potential of interactive, LLM-driven RSICI systems to improve accessibility, interpretability, and analytical efficiency in forest change analysis.

