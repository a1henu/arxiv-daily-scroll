---
layout: default
title: Enhancing Object Detection with Privileged Information: A Model-Agnostic Teacher-Student Approach
---

# Enhancing Object Detection with Privileged Information: A Model-Agnostic Teacher-Student Approach
**arXiv**：[2601.02016v1](https://arxiv.org/abs/2601.02016) · [PDF](https://arxiv.org/pdf/2601.02016.pdf)  
**作者**：Matthias Bartolo, Dylan Seychell, Gabriel Hili, Matthew Montebello, Carl James Debono, Saviour Formosa, Konstantinos Makantasis  

**一句话要点**：提出模型无关的师生架构，利用特权信息增强目标检测，提升精度而不增加推理复杂度。

**关键词**：目标检测, 特权信息学习, 师生架构, 模型无关方法, 精度提升

## 3 点简述
- 核心问题：如何在训练时利用细粒度特权信息（如掩码、深度）提升目标检测，而推理时无需这些信息。
- 方法要点：采用学习使用特权信息范式，通过师生架构将特权信息注入检测模型，模型无关且可适配多种检测器。
- 实验或效果：在多个基准测试中，LUPI训练的学生模型显著超越基线，尤其提升中大目标检测精度，推理复杂度不变。

## 摘要（原文）

> This paper investigates the integration of the Learning Using Privileged Information (LUPI) paradigm in object detection to exploit fine-grained, descriptive information available during training but not at inference. We introduce a general, model-agnostic methodology for injecting privileged information-such as bounding box masks, saliency maps, and depth cues-into deep learning-based object detectors through a teacher-student architecture. Experiments are conducted across five state-of-the-art object detection models and multiple public benchmarks, including UAV-based litter detection datasets and Pascal VOC 2012, to assess the impact on accuracy, generalization, and computational efficiency. Our results demonstrate that LUPI-trained students consistently outperform their baseline counterparts, achieving significant boosts in detection accuracy with no increase in inference complexity or model size. Performance improvements are especially marked for medium and large objects, while ablation studies reveal that intermediate weighting of teacher guidance optimally balances learning from privileged and standard inputs. The findings affirm that the LUPI framework provides an effective and practical strategy for advancing object detection systems in both resource-constrained and real-world settings.

