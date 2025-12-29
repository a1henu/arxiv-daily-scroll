---
layout: default
title: LVLM-Aided Alignment of Task-Specific Vision Models
---

# LVLM-Aided Alignment of Task-Specific Vision Models
**arXiv**：[2512.21985v1](https://arxiv.org/abs/2512.21985) · [PDF](https://arxiv.org/pdf/2512.21985.pdf)  
**作者**：Alexander Koebler, Lukas Kuhn, Ingo Thon, Florian Buettner  

**一句话要点**：提出LVLM-VA方法，利用大视觉语言模型对齐小任务视觉模型与人类领域知识

**关键词**：视觉模型对齐, 大视觉语言模型, 虚假相关性, 任务特定模型, 人类领域知识, 模型解释

## 3 点简述
- 核心问题：小任务视觉模型依赖虚假相关性，与人类知识对齐差，部署时行为脆弱
- 方法要点：基于LVLM构建双向接口，将模型行为翻译为自然语言，人类规范映射为图像级批评
- 实验或效果：在合成和真实数据集上验证，显著提升对齐，减少虚假特征和群体偏见依赖

## 摘要（原文）

> In high-stakes domains, small task-specific vision models are crucial due to their low computational requirements and the availability of numerous methods to explain their results. However, these explanations often reveal that the models do not align well with human domain knowledge, relying instead on spurious correlations. This might result in brittle behavior once deployed in the real-world. To address this issue, we introduce a novel and efficient method for aligning small task-specific vision models with human domain knowledge by leveraging the generalization capabilities of a Large Vision Language Model (LVLM). Our LVLM-Aided Visual Alignment (LVLM-VA) method provides a bidirectional interface that translates model behavior into natural language and maps human class-level specifications to image-level critiques, enabling effective interaction between domain experts and the model. Our method demonstrates substantial improvement in aligning model behavior with human specifications, as validated on both synthetic and real-world datasets. We show that it effectively reduces the model's dependence on spurious features and on group-specific biases, without requiring fine-grained feedback.

