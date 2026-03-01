---
layout: default
title: MM-NeuroOnco: A Multimodal Benchmark and Instruction Dataset for MRI-Based Brain Tumor Diagnosis
---

# MM-NeuroOnco: A Multimodal Benchmark and Instruction Dataset for MRI-Based Brain Tumor Diagnosis
**arXiv**：[2602.22955v1](https://arxiv.org/abs/2602.22955) · [PDF](https://arxiv.org/pdf/2602.22955.pdf)  
**作者**：Feng Guo, Jiaxiang Liu, Yang Li, Qianqian Shi, Mingkun Xu  

**一句话要点**：提出MM-NeuroOnco多模态基准与指令数据集，以提升基于MRI的脑肿瘤诊断理解。

**关键词**：脑肿瘤诊断, 多模态MRI, 指令数据集, 语义注释, 基准评估, 临床推理

## 3 点简述
- 现有脑肿瘤MRI数据集缺乏丰富注释和诊断语义，限制模型临床推理能力。
- 通过多模型协作管道自动生成语义注释，构建大规模多模态指令数据集。
- 评估显示基线模型诊断准确率低，而微调后模型性能显著提升，验证数据集有效性。

## 摘要（原文）

> Accurate brain tumor diagnosis requires models to not only detect lesions but also generate clinically interpretable reasoning grounded in imaging manifestations, yet existing public datasets remain limited in annotation richness and diagnostic semantics. To bridge this gap, we introduce MM-NeuroOnco, a large-scale multimodal benchmark and instruction-tuning dataset for brain tumor MRI understanding, consisting of 24,726 MRI slices from 20 data sources paired with approximately 200,000 semantically enriched multimodal instructions spanning diverse tumor subtypes and imaging modalities. To mitigate the scarcity and high cost of diagnostic semantic annotations, we develop a multi-model collaborative pipeline for automated medical information completion and quality control, enabling the generation of diagnosis-related semantics beyond mask-only annotations. Building upon this dataset, we further construct MM-NeuroOnco-Bench, a manually annotated evaluation benchmark with a rejection-aware setting to reduce biases inherent in closed-ended question formats. Evaluation across ten representative models shows that even the strongest baseline, Gemini 3 Flash, achieves only 41.88% accuracy on diagnosis-related questions, highlighting the substantial challenges of multimodal brain tumor diagnostic understanding. Leveraging MM-NeuroOnco, we further propose NeuroOnco-GPT, which achieves a 27% absolute accuracy improvement on diagnostic questions following fine-tuning. This result demonstrates the effectiveness of our dataset and benchmark in advancing clinically grounded multimodal diagnostic reasoning. Code and dataset are publicly available at: https://github.com/gfnnnb/MM-NeuroOnco

