---
layout: default
title: Assessing the Visual Enumeration Abilities of Specialized Counting Architectures and Vision-Language Models
---

# Assessing the Visual Enumeration Abilities of Specialized Counting Architectures and Vision-Language Models
**arXiv**：[2512.15254v1](https://arxiv.org/abs/2512.15254) · [PDF](https://arxiv.org/pdf/2512.15254.pdf)  
**作者**：Kuinan Hou, Jing Mi, Marco Zorzi, Lamberto Ballan, Alberto Testolin  

**一句话要点**：比较专用计数架构与视觉语言模型在视觉枚举任务中的性能

**关键词**：视觉枚举, 视觉语言模型, 专用计数架构, 开放集计数, 性能评估, 复杂场景

## 3 点简述
- 核心问题：视觉场景中物品计数是计算机视觉的基础挑战，传统方法依赖领域专用架构。
- 方法要点：系统比较专用计数架构与视觉语言模型在标准数据集和新基准上的表现。
- 实验或效果：视觉语言模型性能接近或超越专用架构，但复杂场景下均不可靠，需进一步研究。

## 摘要（原文）

> Counting the number of items in a visual scene remains a fundamental yet challenging task in computer vision. Traditional approaches to solving this problem rely on domain-specific counting architectures, which are trained using datasets annotated with a predefined set of object categories. However, recent progress in creating large-scale multimodal vision-language models (VLMs) suggests that these domain-general architectures may offer a flexible alternative for open-set object counting. In this study, we therefore systematically compare the performance of state-of-the-art specialized counting architectures against VLMs on two popular counting datasets, as well as on a novel benchmark specifically created to have a finer-grained control over the visual properties of test images. Our findings show that most VLMs can approximately enumerate the number of items in a visual scene, matching or even surpassing the performance of specialized computer vision architectures. Notably, enumeration accuracy significantly improves when VLMs are prompted to generate intermediate representations (i.e., locations and verbal labels) of each object to be counted. Nevertheless, none of the models can reliably count the number of objects in complex visual scenes, showing that further research is still needed to create AI systems that can reliably deploy counting procedures in realistic environments.

