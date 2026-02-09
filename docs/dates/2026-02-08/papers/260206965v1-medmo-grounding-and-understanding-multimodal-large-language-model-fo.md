---
layout: default
title: MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images
---

# MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images
**arXiv**：[2602.06965v1](https://arxiv.org/abs/2602.06965) · [PDF](https://arxiv.org/pdf/2602.06965.pdf)  
**作者**：Ankan Deria, Komal Kumar, Adinath Madhavrao Dukre, Eran Segal, Salman Khan, Imran Razzak  

**一句话要点**：提出MedMO医学基础模型，通过多阶段训练解决医学图像多模态理解与空间定位问题。

**关键词**：医学多模态大语言模型, 跨模态预训练, 指令微调, 强化学习, 空间定位, 医学图像理解

## 3 点简述
- 核心问题：医学多模态大语言模型存在领域覆盖不足、模态对齐差和推理缺乏空间定位能力。
- 方法要点：采用跨模态预训练、多任务指令微调和强化学习，结合事实性检查与边界框奖励。
- 实验或效果：在VQA、文本QA和报告生成等任务上超越基线，空间定位IoU提升显著，支持多模态泛化。

## 摘要（原文）

> Multimodal large language models (MLLMs) have rapidly advanced, yet their adoption in medicine remains limited by gaps in domain coverage, modality alignment, and grounded reasoning. In this work, we introduce MedMO, a medical foundation model built upon a generalized MLLM architecture and trained exclusively on large-scale, domain-specific data. MedMO follows a multi-stage training recipe: (i) cross-modal pretraining to align heterogeneous visual encoders with a medical language backbone; (ii) instruction tuning on multi-task supervision that spans captioning, VQA, report generation, retrieval, and grounded disease localization with bounding boxes; and (iii) reinforcement learning with verifiable rewards that combine factuality checks with a box-level GIoU reward to strengthen spatial grounding and step-by-step reasoning in complex clinical scenarios. MedMO consistently outperforms strong open-source medical MLLMs across multiple modalities and tasks. On VQA benchmarks, MedMO achieves an average accuracy improvement of +13.7% over the baseline and performs within 1.9% of the SOTA Fleming-VL. For text-based QA, it attains +6.9% over the baseline and +14.5% over Fleming-VL. In medical report generation, MedMO delivers significant gains in both semantic and clinical accuracy. Moreover, it exhibits strong grounding capability, achieving an IoU improvement of +40.4 over the baseline and +37.0% over Fleming-VL, underscoring its robust spatial reasoning and localization performance. Evaluations across radiology, ophthalmology, and pathology-microscopy confirm MedMO's broad cross-modality generalization. We release two versions of MedMO: 4B and 8B. Project is available at https://genmilab.github.io/MedMO-Page

