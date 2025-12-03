---
layout: default
title: PPTBench: Towards Holistic Evaluation of Large Language Models for PowerPoint Layout and Design Understanding
---

# PPTBench: Towards Holistic Evaluation of Large Language Models for PowerPoint Layout and Design Understanding
**arXiv**：[2512.02624v1](https://arxiv.org/abs/2512.02624) · [PDF](https://arxiv.org/pdf/2512.02624.pdf)  
**作者**：Zheng Huang, Xukai Liu, Tianyu Hu, Kai Zhang, Ye Liu  

**一句话要点**：提出PPTBench以全面评估大语言模型在PowerPoint布局与设计理解中的多模态推理能力

**关键词**：多模态基准, 布局理解, 视觉结构推理, 幻灯片生成, 大语言模型评估

## 3 点简述
- 现有基准忽视布局中心挑战，PPTBench填补此空白，涵盖检测、理解、修改和生成四类任务
- 基于958个PPTX文件构建4,439个样本，实验揭示当前MLLMs在语义理解与视觉布局推理间存在显著差距
- 模型能解释内容但无法生成连贯空间排列，案例研究暴露对齐错误和元素重叠等系统布局问题

## 摘要（原文）

> PowerPoint presentations combine rich textual content with structured visual layouts, making them a natural testbed for evaluating the multimodal reasoning and layout understanding abilities of modern MLLMs. However, existing benchmarks focus solely on narrow subtasks while overlooking layout-centric challenges, which are central to real-world slide creation and editing. To bridge this gap, we introduce PPTBench, a comprehensive multimodal benchmark for evaluating LLMs on PowerPoint-related tasks. Leveraging a diverse source of 958 PPTX files, PPTBench evaluates models across four categories with 4,439 samples, including Detection, Understanding, Modification, and Generation. Our experiments reveal a substantial gap between semantic understanding and visual-layout reasoning in current MLLMs: models can interpret slide content but fail to produce coherent spatial arrangements. Ablation and further analysis show that current MLLMs struggle to combine visual cues with JSON-based layout structures and fail to integrate visual information into their API planning ability. And case studies visually expose systematic layout errors such as misalignment and element overlap. These findings provides a new perspective on evaluating VLLMs in PPT scenarios, highlighting challenges and directions for future research on visual-structural reasoning and coherent slide generation. All datasets and code are fully released to support reproducibility and future research.

