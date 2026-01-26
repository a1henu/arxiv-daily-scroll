---
layout: default
title: Evaluating Large Vision-language Models for Surgical Tool Detection
---

# Evaluating Large Vision-language Models for Surgical Tool Detection
**arXiv**：[2601.16895v1](https://arxiv.org/abs/2601.16895) · [PDF](https://arxiv.org/pdf/2601.16895.pdf)  
**作者**：Nakul Poudel, Richard Simon, Cristian A. Linte  

**一句话要点**：评估大型视觉语言模型在手术工具检测任务中的性能，发现Qwen2.5表现最优。

**关键词**：手术工具检测, 视觉语言模型, 零样本学习, LoRA微调, 机器人手术

## 3 点简述
- 核心问题：当前AI系统多为单模态，难以全面理解手术场景，需通用型手术AI系统。
- 方法要点：在GraSP数据集上评估Qwen2.5、LLaVA1.5和InternVL3.5的零样本和LoRA微调性能。
- 实验或效果：Qwen2.5在检测中表现最佳，零样本泛化强于Grounding DINO，微调后性能相当。

## 摘要（原文）

> Surgery is a highly complex process, and artificial intelligence has emerged as a transformative force in supporting surgical guidance and decision-making. However, the unimodal nature of most current AI systems limits their ability to achieve a holistic understanding of surgical workflows. This highlights the need for general-purpose surgical AI systems capable of comprehensively modeling the interrelated components of surgical scenes. Recent advances in large vision-language models that integrate multimodal data processing offer strong potential for modeling surgical tasks and providing human-like scene reasoning and understanding. Despite their promise, systematic investigations of VLMs in surgical applications remain limited. In this study, we evaluate the effectiveness of large VLMs for the fundamental surgical vision task of detecting surgical tools. Specifically, we investigate three state-of-the-art VLMs, Qwen2.5, LLaVA1.5, and InternVL3.5, on the GraSP robotic surgery dataset under both zero-shot and parameter-efficient LoRA fine-tuning settings. Our results demonstrate that Qwen2.5 consistently achieves superior detection performance in both configurations among the evaluated VLMs. Furthermore, compared with the open-set detection baseline Grounding DINO, Qwen2.5 exhibits stronger zero-shot generalization and comparable fine-tuned performance. Notably, Qwen2.5 shows superior instrument recognition, while Grounding DINO demonstrates stronger localization.

