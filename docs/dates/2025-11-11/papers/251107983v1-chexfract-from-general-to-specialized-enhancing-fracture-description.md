---
layout: default
title: ChexFract: From General to Specialized - Enhancing Fracture Description Generation
---

# ChexFract: From General to Specialized - Enhancing Fracture Description Generation
**arXiv**：[2511.07983v1](https://arxiv.org/abs/2511.07983) · [PDF](https://arxiv.org/pdf/2511.07983.pdf)  
**作者**：Nikolay Nechaev, Evgeniia Przhezdzetskaia, Dmitry Umerenkov, Dmitry V. Dylov  

**一句话要点**：提出骨折专用视觉语言模型以增强胸部X光骨折描述生成

**关键词**：骨折检测, 视觉语言模型, 胸部X光, 医学报告生成, 专用模型训练

## 3 点简述
- 核心问题：通用模型难以准确描述胸部X光中罕见但重要的骨折病理
- 方法要点：基于MAIRA-2和CheXagent编码器训练骨折专用视觉语言模型
- 实验或效果：模型在骨折描述准确性上显著优于通用模型，并公开最佳模型

## 摘要（原文）

> Generating accurate and clinically meaningful radiology reports from chest X-ray images remains a significant challenge in medical AI. While recent vision-language models achieve strong results in general radiology report generation, they often fail to adequately describe rare but clinically important pathologies like fractures. This work addresses this gap by developing specialized models for fracture pathology detection and description. We train fracture-specific vision-language models with encoders from MAIRA-2 and CheXagent, demonstrating significant improvements over general-purpose models in generating accurate fracture descriptions. Analysis of model outputs by fracture type, location, and age reveals distinct strengths and limitations of current vision-language model architectures. We publicly release our best-performing fracture-reporting model, facilitating future research in accurate reporting of rare pathologies.

