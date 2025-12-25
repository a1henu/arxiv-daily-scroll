---
layout: default
title: Model Merging via Multi-Teacher Knowledge Distillation
---

# Model Merging via Multi-Teacher Knowledge Distillation
**arXiv**：[2512.21288v1](https://arxiv.org/abs/2512.21288) · [PDF](https://arxiv.org/pdf/2512.21288.pdf)  
**作者**：Seyed Arshan Dalili, Mehrdad Mahdavi  

**一句话要点**：提出SAMerging方法，通过多教师知识蒸馏解决模型合并中的泛化问题。

**关键词**：模型合并, 知识蒸馏, 泛化理论, 平坦优化, 多任务学习, SAMerging

## 3 点简述
- 核心问题：模型合并缺乏理论保证，系数缩放依赖启发式方法，导致性能脆弱。
- 方法要点：建立平坦感知PAC-Bayes泛化界，将合并视为多教师知识蒸馏，使用SAM优化。
- 实验或效果：在视觉和NLP基准上达到新SOTA，代码已开源。

## 摘要（原文）

> Model merging has emerged as a lightweight alternative to joint multi-task learning (MTL), yet the generalization properties of merged models remain largely unexplored. Establishing such theoretical guarantees is non-trivial, as the merging process typically forbids access to the original training data and involves combining fine-tuned models trained on fundamentally heterogeneous data distributions. Without a principled understanding of these dynamics, current methods often rely on heuristics to approximate the optimal combination of parameters. This dependence is most critical in coefficient scaling, the weighting factors that modulate the magnitude of each fine-tuned model's contribution to the shared parameter. However, without a principled objective to guide their selection, these methods lead to brittle performance and are highly sensitive to scaling initialization. We address this gap by (i) establishing a novel flatness-aware PAC-Bayes generalization bound specifically for the model merging setting. This analysis introduces a "cross-task heterogeneity" term that formally captures the mismatch between diverse fine-tuned model priors and the target multi-task distributions. Guided by this theoretical insight, (ii) we frame model merging as multi-teacher knowledge distillation on scarce, unlabeled data. We formally demonstrate that minimizing the student-teacher Kullback-Leibler divergence directly tightens the upper bound on the merged model's excess risk. Guided by the flatness-aware bound derived, (iii) we operationalize this objective via SAMerging, a method that employs Sharpness-Aware Minimization (SAM) to find flat minima. Empirically, SAMerging establishes a new state of the art across vision and NLP benchmarks, achieving remarkable performance. The code is available at https://github.com/arshandalili/SAMerging.

