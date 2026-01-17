---
layout: default
title: CoGen: Creation of Reusable UI Components in Figma via Textual Commands
---

# CoGen: Creation of Reusable UI Components in Figma via Textual Commands
**arXiv**：[2601.10536v1](https://arxiv.org/abs/2601.10536) · [PDF](https://arxiv.org/pdf/2601.10536.pdf)  
**作者**：Ishani Kanapathipillai, Obhasha Priyankara  

**一句话要点**：提出CoGen系统，通过文本命令在Figma中生成可重用UI组件以提升设计效率。

**关键词**：UI组件生成, 自然语言处理, Figma集成, T5变换器, JSON映射

## 3 点简述
- 核心问题：当前UI设计工具缺乏高效生成可重用原子组件的方法，影响设计流程。
- 方法要点：集成Figma API数据提取、Seq2Seq模型和微调T5变换器，将自然语言提示映射为结构化JSON。
- 实验或效果：T5模型在提示生成上准确率达98%，BLEU分数0.2668；JSON生成成功率高达100%用于简单组件。

## 摘要（原文）

> The evolution of User Interface design has emphasized the need for efficient, reusable, and editable components to ensure an efficient design process. This research introduces CoGen, a system that uses machine learning techniques to generate reusable UI components directly in Figma, one of the most popular UI design tools. Addressing gaps in current systems, CoGen focuses on creating atomic components such as buttons, labels, and input fields using structured JSON and natural language prompts.
>   The project integrates Figma API data extraction, Seq2Seq models, and fine-tuned T5 transformers for component generation. The key results demonstrate the efficiency of the T5 model in prompt generation, with an accuracy of 98% and a BLEU score of 0.2668, which ensures the mapping of JSON to descriptive prompts. For JSON creation, CoGen achieves a success rate of up to 100% in generating simple JSON outputs for specified component types.

