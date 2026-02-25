---
layout: default
title: Beyond Human Performance: A Vision-Language Multi-Agent Approach for Quality Control in Pharmaceutical Manufacturing
---

# Beyond Human Performance: A Vision-Language Multi-Agent Approach for Quality Control in Pharmaceutical Manufacturing
**arXiv**：[2602.20543v1](https://arxiv.org/abs/2602.20543) · [PDF](https://arxiv.org/pdf/2602.20543.pdf)  
**作者**：Subhra Jyoti Mandal, Lara Rachidi, Puneet Jain, Matthieu Duvinage, Sander W. Timmer  

**一句话要点**：提出结合深度学习与视觉语言模型的多智能体框架，以提升制药制造中菌落检测的自动化质量控制系统。

**关键词**：菌落检测, 视觉语言模型, 多智能体框架, 制药制造, 质量控制系统, 深度学习

## 3 点简述
- 核心问题：传统深度学习模型在菌落检测中受样本质量变化影响，准确率不足，难以满足制药行业高标准要求。
- 方法要点：开发多智能体框架，利用视觉语言模型分类样本，结合深度学习模型独立计数，通过预测一致性自动处理或专家审核。
- 实验或效果：集成视觉语言模型后，自动化减少人工验证85%，提供可扩展、可审计的解决方案，显著提升操作效率。

## 摘要（原文）

> Colony-forming unit (CFU) detection is critical in pharmaceutical manufacturing, serving as a key component of Environmental Monitoring programs and ensuring compliance with stringent quality standards. Manual counting is labor-intensive and error-prone, while deep learning (DL) approaches, though accurate, remain vulnerable to sample quality variations and artifacts. Building on our earlier CNN-based framework (Beznik et al., 2020), we evaluated YOLOv5, YOLOv7, and YOLOv8 for CFU detection; however, these achieved only 97.08 percent accuracy, insufficient for pharmaceutical-grade requirements. A custom Detectron2 model trained on GSK's dataset of over 50,000 Petri dish images achieved 99 percent detection rate with 2 percent false positives and 0.6 percent false negatives. Despite high validation accuracy, Detectron2 performance degrades on outlier cases including contaminated plates, plastic artifacts, or poor optical clarity. To address this, we developed a multi-agent framework combining DL with vision-language models (VLMs). The VLM agent first classifies plates as valid or invalid. For valid samples, both DL and VLM agents independently estimate colony counts. When predictions align within 5 percent, results are automatically recorded in Postgres and SAP; otherwise, samples are routed for expert review. Expert feedback enables continuous retraining and self-improvement. Initial DL-based automation reduced human verification by 50 percent across vaccine manufacturing sites. With VLM integration, this increased to 85 percent, delivering significant operational savings. The proposed system provides a scalable, auditable, and regulation-ready solution for microbiological quality control, advancing automation in biopharmaceutical production.

