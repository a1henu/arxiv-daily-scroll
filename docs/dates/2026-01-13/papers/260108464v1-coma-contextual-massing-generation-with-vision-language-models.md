---
layout: default
title: CoMa: Contextual Massing Generation with Vision-Language Models
---

# CoMa: Contextual Massing Generation with Vision-Language Models
**arXiv**：[2601.08464v1](https://arxiv.org/abs/2601.08464) · [PDF](https://arxiv.org/pdf/2601.08464.pdf)  
**作者**：Evgenii Maslov, Valentin Khrulkov, Anastasia Volkova, Anton Gusarov, Andrey Kuznetsov, Ivan Oseledets  

**一句话要点**：提出CoMa框架与数据集，利用视觉语言模型生成基于功能需求和场地环境的建筑体量

**关键词**：建筑体量生成, 视觉语言模型, 数据集构建, 条件生成, 建筑设计自动化

## 3 点简述
- 核心问题：建筑概念设计依赖直觉和手动，缺乏自动化方法和数据集。
- 方法要点：引入CoMa-20K数据集，包含体量几何、经济数据和场地视觉信息。
- 实验或效果：将体量生成作为条件任务，评估微调和零样本模型，展示模型潜力。

## 摘要（原文）

> The conceptual design phase in architecture and urban planning, particularly building massing, is complex and heavily reliant on designer intuition and manual effort. To address this, we propose an automated framework for generating building massing based on functional requirements and site context. A primary obstacle to such data-driven methods has been the lack of suitable datasets. Consequently, we introduce the CoMa-20K dataset, a comprehensive collection that includes detailed massing geometries, associated economical and programmatic data, and visual representations of the development site within its existing urban context. We benchmark this dataset by formulating massing generation as a conditional task for Vision-Language Models (VLMs), evaluating both fine-tuned and large zero-shot models. Our experiments reveal the inherent complexity of the task while demonstrating the potential of VLMs to produce context-sensitive massing options. The dataset and analysis establish a foundational benchmark and highlight significant opportunities for future research in data-driven architectural design.

