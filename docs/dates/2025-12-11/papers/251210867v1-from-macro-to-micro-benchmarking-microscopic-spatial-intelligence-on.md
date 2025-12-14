---
layout: default
title: From Macro to Micro: Benchmarking Microscopic Spatial Intelligence on Molecules via Vision-Language Models
---

# From Macro to Micro: Benchmarking Microscopic Spatial Intelligence on Molecules via Vision-Language Models
**arXiv**：[2512.10867v1](https://arxiv.org/abs/2512.10867) · [PDF](https://arxiv.org/pdf/2512.10867.pdf)  
**作者**：Zongzhao Li, Xiangzhe Kong, Jiahui Su, Zongyang Ma, Mingze Li, Songyou Li, Yuelin Zhang, Yu Rong, Tingyang Xu, Deli Zhao, Wenbing Huang  

**一句话要点**：提出MiSI-Bench基准框架，评估视觉语言模型在分子微观空间智能上的能力。

**关键词**：微观空间智能, 视觉语言模型, 分子结构, 基准评估, 空间变换, 氢键识别

## 3 点简述
- 核心问题：评估视觉语言模型在微观实体空间感知与推理（MiSI）上的潜力，这对科学发现至关重要。
- 方法要点：构建包含超16.3万问答对和58.7万图像的基准，覆盖九项互补任务，从基础空间变换到复杂关系识别。
- 实验或效果：当前先进模型表现显著低于人类，但微调7B模型在空间变换任务中超越人类，氢键识别等科学任务表现差，需整合领域知识。

## 摘要（原文）

> This paper introduces the concept of Microscopic Spatial Intelligence (MiSI), the capability to perceive and reason about the spatial relationships of invisible microscopic entities, which is fundamental to scientific discovery. To assess the potential of Vision-Language Models (VLMs) in this domain, we propose a systematic benchmark framework MiSI-Bench. This framework features over 163,000 question-answer pairs and 587,000 images derived from approximately 4,000 molecular structures, covering nine complementary tasks that evaluate abilities ranging from elementary spatial transformations to complex relational identifications. Experimental results reveal that current state-of-the-art VLMs perform significantly below human level on this benchmark. However, a fine-tuned 7B model demonstrates substantial potential, even surpassing humans in spatial transformation tasks, while its poor performance in scientifically-grounded tasks like hydrogen bond recognition underscores the necessity of integrating explicit domain knowledge for progress toward scientific AGI. The datasets are available at https://huggingface.co/datasets/zongzhao/MiSI-bench.

