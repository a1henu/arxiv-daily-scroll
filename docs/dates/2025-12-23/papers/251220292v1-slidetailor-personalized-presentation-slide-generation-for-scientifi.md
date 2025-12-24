---
layout: default
title: SlideTailor: Personalized Presentation Slide Generation for Scientific Papers
---

# SlideTailor: Personalized Presentation Slide Generation for Scientific Papers
**arXiv**：[2512.20292v1](https://arxiv.org/abs/2512.20292) · [PDF](https://arxiv.org/pdf/2512.20292.pdf)  
**作者**：Wenzheng Zeng, Mingyu Ouyang, Langyuan Cui, Hwee Tou Ng  

**一句话要点**：提出SlideTailor框架，基于用户偏好个性化生成科学论文演示幻灯片

**关键词**：幻灯片生成, 个性化偏好, 代理框架, 链式语音机制, 基准数据集

## 3 点简述
- 核心问题：现有幻灯片生成方法未考虑用户偏好，导致结果不符合个性化需求
- 方法要点：使用论文-幻灯片示例对和视觉模板隐式编码用户偏好，通过代理框架逐步生成可编辑幻灯片
- 实验或效果：构建基准数据集，实验显示框架有效提升生成幻灯片质量

## 摘要（原文）

> Automatic presentation slide generation can greatly streamline content creation. However, since preferences of each user may vary, existing under-specified formulations often lead to suboptimal results that fail to align with individual user needs. We introduce a novel task that conditions paper-to-slides generation on user-specified preferences. We propose a human behavior-inspired agentic framework, SlideTailor, that progressively generates editable slides in a user-aligned manner. Instead of requiring users to write their preferences in detailed textual form, our system only asks for a paper-slides example pair and a visual template - natural and easy-to-provide artifacts that implicitly encode rich user preferences across content and visual style. Despite the implicit and unlabeled nature of these inputs, our framework effectively distills and generalizes the preferences to guide customized slide generation. We also introduce a novel chain-of-speech mechanism to align slide content with planned oral narration. Such a design significantly enhances the quality of generated slides and enables downstream applications like video presentations. To support this new task, we construct a benchmark dataset that captures diverse user preferences, with carefully designed interpretable metrics for robust evaluation. Extensive experiments demonstrate the effectiveness of our framework.

