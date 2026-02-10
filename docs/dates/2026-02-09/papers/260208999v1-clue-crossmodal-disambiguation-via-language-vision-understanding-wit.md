---
layout: default
title: CLUE: Crossmodal disambiguation via Language-vision Understanding with attEntion
---

# CLUE: Crossmodal disambiguation via Language-vision Understanding with attEntion
**arXiv**：[2602.08999v1](https://arxiv.org/abs/2602.08999) · [PDF](https://arxiv.org/pdf/2602.08999.pdf)  
**作者**：Mouad Abrini, Mohamed Chetouani  

**一句话要点**：提出CLUE模型，通过跨模态注意力解决机器人交互视觉定位中的歧义问题

**关键词**：交互视觉定位, 跨模态注意力, 歧义检测, 参数高效微调, 机器人交互

## 3 点简述
- 核心问题：现有交互视觉定位模型缺乏显式机制决定何时提问澄清，依赖隐式表示导致歧义处理不足。
- 方法要点：提取视觉语言模型的跨模态注意力图，经轻量CNN检测指代歧义，结合LoRA微调解码器进行对话和定位。
- 实验或效果：在真实交互数据集上训练，模型超越现有方法，歧义检测器优于基线，实现参数高效微调。

## 摘要（原文）

> With the increasing integration of robots into daily life, human-robot interaction has become more complex and multifaceted. A critical component of this interaction is Interactive Visual Grounding (IVG), through which robots must interpret human intentions and resolve ambiguity. Existing IVG models generally lack a mechanism to determine when to ask clarification questions, as they implicitly rely on their learned representations. CLUE addresses this gap by converting the VLM's cross-modal attention into an explicit, spatially grounded signal for deciding when to ask. We extract text to image attention maps and pass them to a lightweight CNN to detect referential ambiguity, while a LoRA fine-tuned decoder conducts the dialog and emits grounding location tokens. We train on a real-world interactive dataset for IVG, and a mixed ambiguity set for the detector. With InViG-only supervision, our model surpasses a state-of-the-art method while using parameter-efficient fine-tuning. Similarly, the ambiguity detector outperforms prior baselines. Overall, CLUE turns the internal cross-modal attention of a VLM into an explicit, spatially grounded signal for deciding when to ask. The data and code are publicly available at: mouadabrini.github.io/clue

