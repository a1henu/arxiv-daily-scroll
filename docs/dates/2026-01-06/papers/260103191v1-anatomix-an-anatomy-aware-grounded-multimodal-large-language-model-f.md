---
layout: default
title: AnatomiX, an Anatomy-Aware Grounded Multimodal Large Language Model for Chest X-Ray Interpretation
---

# AnatomiX, an Anatomy-Aware Grounded Multimodal Large Language Model for Chest X-Ray Interpretation
**arXiv**：[2601.03191v1](https://arxiv.org/abs/2601.03191) · [PDF](https://arxiv.org/pdf/2601.03191.pdf)  
**作者**：Anees Ur Rehman Hashmi, Numan Saeed, Christoph Lippert  

**一句话要点**：提出AnatomiX以解决胸部X光解读中解剖学对应不足的问题

**关键词**：胸部X光解读, 解剖学接地, 多模态大语言模型, 两阶段方法, 视觉问答

## 3 点简述
- 核心问题：现有多模态大语言模型在胸部X光解读中空间推理和解剖学理解不足
- 方法要点：采用两阶段方法，先识别解剖结构提取特征，再利用大语言模型执行下游任务
- 实验或效果：在多个基准测试中，解剖学推理表现优异，解剖学接地任务性能提升超25%

## 摘要（原文）

> Multimodal medical large language models have shown impressive progress in chest X-ray interpretation but continue to face challenges in spatial reasoning and anatomical understanding. Although existing grounding techniques improve overall performance, they often fail to establish a true anatomical correspondence, resulting in incorrect anatomical understanding in the medical domain. To address this gap, we introduce AnatomiX, a multitask multimodal large language model explicitly designed for anatomically grounded chest X-ray interpretation. Inspired by the radiological workflow, AnatomiX adopts a two stage approach: first, it identifies anatomical structures and extracts their features, and then leverages a large language model to perform diverse downstream tasks such as phrase grounding, report generation, visual question answering, and image understanding. Extensive experiments across multiple benchmarks demonstrate that AnatomiX achieves superior anatomical reasoning and delivers over 25% improvement in performance on anatomy grounding, phrase grounding, grounded diagnosis and grounded captioning tasks compared to existing approaches. Code and pretrained model are available at https://github.com/aneesurhashmi/anatomix

