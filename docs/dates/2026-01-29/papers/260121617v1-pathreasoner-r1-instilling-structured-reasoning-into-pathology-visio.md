---
layout: default
title: PathReasoner-R1: Instilling Structured Reasoning into Pathology Vision-Language Model via Knowledge-Guided Policy Optimization
---

# PathReasoner-R1: Instilling Structured Reasoning into Pathology Vision-Language Model via Knowledge-Guided Policy Optimization
**arXiv**：[2601.21617v1](https://arxiv.org/abs/2601.21617) · [PDF](https://arxiv.org/pdf/2601.21617.pdf)  
**作者**：Songhan Jiang, Fengchun Liu, Ziyue Wang, Linghan Cai, Yongbing Zhang  

**一句话要点**：提出PathReasoner-R1，通过知识引导策略优化为病理视觉语言模型注入结构化推理能力

**关键词**：病理视觉语言模型, 结构化推理, 知识图谱, 强化学习, 全切片图像, 临床诊断

## 3 点简述
- 当前病理视觉语言模型缺乏可验证的证据链推理，限制临床信任
- 构建首个大规模全切片图像推理数据集，采用知识图谱引导生成高质量样本
- 结合轨迹掩码监督微调与推理导向强化学习，实现逻辑一致的结构化推理

## 摘要（原文）

> Vision-Language Models (VLMs) are advancing computational pathology with superior visual understanding capabilities. However, current systems often reduce diagnosis to directly output conclusions without verifiable evidence-linked reasoning, which severely limits clinical trust and hinders expert error rectification. To address these barriers, we construct PathReasoner, the first large-scale dataset of whole-slide image (WSI) reasoning. Unlike previous work reliant on unverified distillation, we develop a rigorous knowledge-guided generation pipeline. By leveraging medical knowledge graphs, we explicitly align structured pathological findings and clinical reasoning with diagnoses, generating over 20K high-quality instructional samples. Based on the database, we propose PathReasoner-R1, which synergizes trajectory-masked supervised fine-tuning with reasoning-oriented reinforcement learning to instill structured chain-of-thought capabilities. To ensure medical rigor, we engineer a knowledge-aware multi-granular reward function incorporating an Entity Reward mechanism strictly aligned with knowledge graphs. This effectively guides the model to optimize for logical consistency rather than mere outcome matching, thereby enhancing robustness. Extensive experiments demonstrate that PathReasoner-R1 achieves state-of-the-art performance on both PathReasoner and public benchmarks across various image scales, equipping pathology models with transparent, clinically grounded reasoning capabilities. Dataset and code are available at https://github.com/cyclexfy/PathReasoner-R1.

