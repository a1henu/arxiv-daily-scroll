---
layout: default
title: Can Agents Distinguish Visually Hard-to-Separate Diseases in a Zero-Shot Setting? A Pilot Study
---

# Can Agents Distinguish Visually Hard-to-Separate Diseases in a Zero-Shot Setting? A Pilot Study
**arXiv**：[2602.22959v1](https://arxiv.org/abs/2602.22959) · [PDF](https://arxiv.org/pdf/2602.22959.pdf)  
**作者**：Zihao Zhao, Frederik Hauke, Juliana De Castilhos, Sven Nebelung, Daniel Truhn  

**一句话要点**：提出基于对比裁决的多智能体框架，以提升零样本视觉难分疾病区分性能

**关键词**：零样本学习, 多模态大语言模型, 医学影像诊断, 视觉混淆疾病, 多智能体系统, 对比裁决

## 3 点简述
- 研究零样本下视觉特征高度混淆的疾病区分问题，如黑色素瘤与非典型痣
- 采用多智能体对比裁决方法，减少无支持主张并提升诊断准确性
- 实验显示准确率提升11个百分点，但整体性能仍不足以临床部署

## 摘要（原文）

> The rapid progress of multimodal large language models (MLLMs) has led to increasing interest in agent-based systems. While most prior work in medical imaging concentrates on automating routine clinical workflows, we study an underexplored yet clinically significant setting: distinguishing visually hard-to-separate diseases in a zero-shot setting. We benchmark representative agents on two imaging-only proxy diagnostic tasks, (1) melanoma vs. atypical nevus and (2) pulmonary edema vs. pneumonia, where visual features are highly confounded despite substantial differences in clinical management. We introduce a multi-agent framework based on contrastive adjudication. Experimental results show improved diagnostic performance (an 11-percentage-point gain in accuracy on dermoscopy data) and reduced unsupported claims on qualitative samples, although overall performance remains insufficient for clinical deployment. We acknowledge the inherent uncertainty in human annotations and the absence of clinical context, which further limit the translation to real-world settings. Within this controlled setting, this pilot study provides preliminary insights into zero-shot agent performance in visually confounded scenarios.

