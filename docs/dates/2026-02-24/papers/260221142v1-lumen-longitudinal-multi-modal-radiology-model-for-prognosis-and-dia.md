---
layout: default
title: LUMEN: Longitudinal Multi-Modal Radiology Model for Prognosis and Diagnosis
---

# LUMEN: Longitudinal Multi-Modal Radiology Model for Prognosis and Diagnosis
**arXiv**：[2602.21142v1](https://arxiv.org/abs/2602.21142) · [PDF](https://arxiv.org/pdf/2602.21142.pdf)  
**作者**：Zhifan Jiang, Dong Yang, Vishwesh Nath, Abhijeet Parida, Nishad P. Kulkarni, Ziyue Xu, Daguang Xu, Syed Muhammad Anwar, Holger R. Roth, Marius George Linguraru  

**一句话要点**：提出LUMEN框架以优化纵向胸部X光解读，通过多图像多任务指令微调提升预后与诊断性能。

**关键词**：纵向放射影像分析, 视觉语言模型, 指令微调, 预后任务, 胸部X光, 多模态学习

## 3 点简述
- 核心问题：纵向放射影像分析耗时，需自动化支持预后与诊断决策。
- 方法要点：采用多图像多任务指令微调，构建包含纵向研究的指令数据集。
- 实验或效果：在MIMIC-CXR数据集上优于基线，显示预后潜力。

## 摘要（原文）

> Large vision-language models (VLMs) have evolved from general-purpose applications to specialized use cases such as in the clinical domain, demonstrating potential for decision support in radiology. One promising application is assisting radiologists in decision-making by the analysis of radiology imaging data such as chest X-rays (CXR) via a visual and natural language question-answering (VQA) interface. When longitudinal imaging is available, radiologists analyze temporal changes, which are essential for accurate diagnosis and prognosis. The manual longitudinal analysis is a time-consuming process, motivating the development of a training framework that can provide prognostic capabilities. We introduce a novel training framework LUMEN, that is optimized for longitudinal CXR interpretation, leveraging multi-image and multi-task instruction fine-tuning to enhance prognostic and diagnostic performance. We conduct experiments on the publicly available MIMIC-CXR and its associated Medical-Diff-VQA datasets. We further formulate and construct a novel instruction-following dataset incorporating longitudinal studies, enabling the development of a prognostic VQA task. Our method demonstrates significant improvements over baseline models in diagnostic VQA tasks, and more importantly, shows promising potential for prognostic capabilities. These results underscore the value of well-designed, instruction-tuned VLMs in enabling more accurate and clinically meaningful radiological interpretation of longitudinal radiological imaging data.

