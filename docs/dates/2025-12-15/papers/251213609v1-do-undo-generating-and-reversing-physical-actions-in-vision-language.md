---
layout: default
title: Do-Undo: Generating and Reversing Physical Actions in Vision-Language Models
---

# Do-Undo: Generating and Reversing Physical Actions in Vision-Language Models
**arXiv**：[2512.13609v1](https://arxiv.org/abs/2512.13609) · [PDF](https://arxiv.org/pdf/2512.13609.pdf)  
**作者**：Shweta Mahajan, Shreya Kadambi, Hoang Le, Munawar Hayat, Fatih Porikli  

**一句话要点**：提出Do-Undo任务与基准，以解决视觉语言模型在物理动作理解与生成中的可逆性挑战。

**关键词**：物理动作理解, 可逆性基准, 视觉语言模型, 具身AI, 物理感知生成

## 3 点简述
- 核心问题：现有模型缺乏对物理动作可逆性的理解，难以模拟真实世界中的因果变换。
- 方法要点：构建大规模可逆动作数据集，设计训练策略强化动作一致性与物理合理性。
- 实验或效果：实验显示当前模型在物理可逆任务上表现不佳，突显该任务对具身AI和物理感知生成的重要性。

## 摘要（原文）

> We introduce the Do-Undo task and benchmark to address a critical gap in vision-language models: understanding and generating physically plausible scene transformations driven by real-world actions. Unlike prior work focused on object-level edits, Do-Undo requires models to simulate the outcome of a physical action and then accurately reverse it, reflecting true cause-and-effect in the visual world. We curate a large-scale dataset of reversible actions from real-world videos and design a training strategy enforcing consistency for robust action grounding. Our experiments reveal that current models struggle with physical reversibility, underscoring the importance of this task for embodied AI, robotics, and physics-aware generative modeling. Do-Undo establishes an intuitive testbed for evaluating and advancing physical reasoning in multimodal systems.

