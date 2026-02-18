---
layout: default
title: Bridging Day and Night: Target-Class Hallucination Suppression in Unpaired Image Translation
---

# Bridging Day and Night: Target-Class Hallucination Suppression in Unpaired Image Translation
**arXiv**：[2602.15383v1](https://arxiv.org/abs/2602.15383) · [PDF](https://arxiv.org/pdf/2602.15383.pdf)  
**作者**：Shuwei Li, Lei Tan, Robby T. Tan  

**一句话要点**：提出基于类原型和双头判别器的框架，以抑制无配对图像翻译中的目标类语义幻觉。

**关键词**：无配对图像翻译, 语义幻觉抑制, 类原型, 双头判别器, 日到夜域适应, Schrodinger Bridge

## 3 点简述
- 核心问题：日到夜无配对图像翻译中，目标类对象和人工光效常出现语义幻觉，影响下游任务性能。
- 方法要点：使用双头判别器检测背景区域幻觉，并引入类原型作为语义锚点，在特征空间迭代抑制幻觉。
- 实验或效果：在BDD100K数据集上，日到夜域适应mAP提升15.5%，易幻觉类如交通灯增益达31.7%。

## 摘要（原文）

> Day-to-night unpaired image translation is important to downstream tasks but remains challenging due to large appearance shifts and the lack of direct pixel-level supervision. Existing methods often introduce semantic hallucinations, where objects from target classes such as traffic signs and vehicles, as well as man-made light effects, are incorrectly synthesized. These hallucinations significantly degrade downstream performance. We propose a novel framework that detects and suppresses hallucinations of target-class features during unpaired translation. To detect hallucination, we design a dual-head discriminator that additionally performs semantic segmentation to identify hallucinated content in background regions. To suppress these hallucinations, we introduce class-specific prototypes, constructed by aggregating features of annotated target-domain objects, which act as semantic anchors for each class. Built upon a Schrodinger Bridge-based translation model, our framework performs iterative refinement, where detected hallucination features are explicitly pushed away from class prototypes in feature space, thus preserving object semantics across the translation trajectory.Experiments show that our method outperforms existing approaches both qualitatively and quantitatively. On the BDD100K dataset, it improves mAP by 15.5% for day-to-night domain adaptation, with a notable 31.7% gain for classes such as traffic lights that are prone to hallucinations.

